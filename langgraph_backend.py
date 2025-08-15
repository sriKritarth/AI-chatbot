from langgraph.graph import StateGraph , START ,END ,add_messages
from typing import TypedDict , Annotated
from langchain_core.messages import BaseMessage ,HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()


llm = ChatOpenAI()
class chatState(TypedDict) :

    messages : Annotated[list[BaseMessage] , add_messages]


def chat_state(state : chatState) :

    query = state['messages']

    prompt = f"Answer to the question of the given {query}"

    response = llm.invoke(prompt)

    return {'messages' : [response]}


checkpointer = InMemorySaver()
graph = StateGraph(chatState)

graph.add_node('chat_state' , chat_state)


graph.add_edge(START , 'chat_state')
graph.add_edge('chat_state' ,END)

chatbot = graph.compile(checkpointer=checkpointer)

config = {'configurable' : {'thread_id' : 'thread-1'}}

chatbot.invoke(
                {'messages': [HumanMessage(content="Hi! My name is Kritarth")]},
                config= config,
)

print(chatbot.get_state(config=config).values['messages'])