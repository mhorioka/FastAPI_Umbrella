from fastapi import FastAPI
import uvicorn

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello World"}


@api.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

uvicorn.run(api)
