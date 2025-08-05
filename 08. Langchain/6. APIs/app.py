from fastapi import FastAPI
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn

app = FastAPI(
    title="Gemma LangServe API",
    version="1.0",
    description="FastAPI server using Gemma 2B via Ollama"
)

# Load Gemma model via Ollama
llm = Ollama(model="gemma:2b")

# Prompt Template
prompt = ChatPromptTemplate.from_template("Write a poem about {topic} for a 5-year-old child with 100 words.")

# Add LangChain runnable route
add_routes(
    app,
    prompt | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
