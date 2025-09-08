# AI Chatbot using LangGraph

A modular, LangGraph-powered AI chatbot with a Streamlit frontend and Python backend, designed for scalability, experimentation, and real-world usability. This project demonstrates how to integrate LangGraph for conversational AI workflows, with database persistence and a clean UI.

## Features

- LangGraph Integration – Build and manage conversational flows with ease.
- Streamlit Frontend – Interactive, browser-based UI for chatting with the bot.
- Threaded Frontend Option – Improved responsiveness with `streamlit_frontend_threading.py`.
- Database Support – Store and retrieve conversation history using SQLite.
- Modular Backend – Separate logic for app, database, and LangGraph processing.
- Customizable – Easily extend prompts, logic, and UI components.

## Project Structure

| File / Folder | Description |
|---------------|-------------|
| app.py | Main application entry point. |
| app_database.py | Handles database operations for the app. |
| chatbot.db | SQLite database storing chat history. |
| langgraph_backend.py | Core LangGraph chatbot logic. |
| langgraph_database_backend.py | LangGraph + database integration layer. |
| requirements.txt | Python dependencies. |
| streamlit_frontend.py | Streamlit-based chatbot UI. |
| streamlit_frontend_threading.py | Threaded version of the Streamlit UI for better performance. |

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/sriKritarth/AI-chatbot.git
cd AI-chatbot

### 2. Create and activate virtual envviroment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
