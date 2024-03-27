from fastapi import FastAPI

from src.dtos.ISayHelloDto import ISayHelloDto

from src.service.network_util import PythonPing

app = FastAPI()


@app.get("/")
async def root():
    # PythonPing.execute()
    # ans = PythonPing.execute_http()

    return {"message": "ans"}


@app.get("/hello/{password}")
async def say_hello(password: str):
    PythonPing.execute_send_message(password)
    return {"message": f"Hello {password}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
