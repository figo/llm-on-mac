from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
#import multiprocessing
from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.prompts import ChatPromptTemplate

# Replace with your local model file location
local_model=".../Meta-Llama-3.1-8B-Instruct-IQ2_M.gguf"

llm_local = ChatLlamaCpp(
    temperature=0.8,
    model_path=local_model,
    n_batch=8,  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
    max_tokens=10240,
    repeat_penalty=1,
    streaming=True,
    top_p=0.9,
    n_ctx=40960,
    verbose=False,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant like a teacher will guide the human on how to solve the problem, and guide on how to break the problem into small pieces, please try provide real world examples, but you can not provide direct answer.",
        ),
        ("human", "{text}"),
    ]
)

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(
    app,
    prompt | llm_local,
    path="/ask",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
