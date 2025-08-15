from langgraph.graph import StateGraph , START ,END ,add_messages
from typing import TypedDict , Annotated
from langchain_core.messages import BaseMessage ,HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

load_dotenv()


llm = ChatOpenAI()

class chatState(TypedDict) :

    messages : Annotated[list[BaseMessage] , add_messages]


def chat_state(state : chatState) :

    query = state['messages']

    prompt = f"Answer to the question of the given {query}"

    response = llm.invoke(prompt)

    return {'messages' : [response]}


#Connection between db and backend
conn = sqlite3.connect(database='chatbot.db' , check_same_thread= False)


checkpointer = SqliteSaver(conn=conn)
graph = StateGraph(chatState)

graph.add_node('chat_state' , chat_state)


graph.add_edge(START , 'chat_state')
graph.add_edge('chat_state' ,END)

chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_thread_id():
    
    all_threads = set()

    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return (list(all_threads))

