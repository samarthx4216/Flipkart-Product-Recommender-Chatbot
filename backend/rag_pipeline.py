import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from backend.data_ingestion import get_vector_store
from backend.logger import setup_logger

load_dotenv()
logger = setup_logger("rag_pipeline")

# Store chat history
chat_history = []

def get_llm():
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile",
        temperature=0.3,
    )

def chat(user_message: str) -> dict:
    logger.info(f"User query: {user_message}")
    try:
        # Get relevant products
        vector_store = get_vector_store()
        retriever = vector_store.as_retriever(search_kwargs={"k": 4})
        docs = retriever.invoke(user_message)

        # Build context
        context = "\n\n".join([doc.page_content for doc in docs])
        sources = [doc.metadata.get("name", "") for doc in docs]

        # Build history string
        history_str = ""
        for msg in chat_history[-6:]:
            if isinstance(msg, HumanMessage):
                history_str += f"Customer: {msg.content}\n"
            else:
                history_str += f"Assistant: {msg.content}\n"

        # Prompt
        prompt = f"""You are a helpful Flipkart shopping assistant.
Use the following product information to answer customer queries.
Always recommend specific products with their prices and ratings.
Be friendly, helpful and concise.

Context from product database:
{context}

Chat History:
{history_str}

Customer Question: {user_message}

Helpful Assistant Response:"""

        # Get response
        llm = get_llm()
        response = llm.invoke(prompt)
        answer = response.content

        # Update history
        chat_history.append(HumanMessage(content=user_message))
        chat_history.append(AIMessage(content=answer))

        logger.info(f"Response generated. Sources: {sources}")
        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        logger.error(f"RAG pipeline error: {e}")
        return {
            "answer": "Sorry, I encountered an error. Please try again!",
            "sources": []
        }