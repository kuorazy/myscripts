from fastapi import FastAPI

from src.dtos.ISayHelloDto import ISayHelloDto

from src.service.network_util import PythonPing

app = FastAPI()


@app.get("/")
async def root():
    # PythonPing.execute()
    # ans = PythonPing.execute_http()

    return {"message": "ans"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    if name == "fangshua":
        PythonPing.execute_send_message()
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
