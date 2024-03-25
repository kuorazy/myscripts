from fastapi import FastAPI

from src.dtos.ISayHelloDto import ISayHelloDto

from src.service.network_util import PythonPing

app = FastAPI()


@app.get("/")
async def root():
    # PythonPing.execute()
    PythonPing.execute_native()
    return {"message": "res1 + res2 + res3"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
