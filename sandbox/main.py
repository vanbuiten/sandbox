from fastapi import FastAPI
from pydantic import BaseModel

from sandbox.utils import get_version

app = FastAPI()


class RootResponse(BaseModel):
    status: str = "ok"
    version: str


@app.get("/")
def read_root() -> RootResponse:
    version = get_version()
    return RootResponse(version=version)


class GreetingsRequest(BaseModel):
    name: str


class GreetingResponse(BaseModel):
    hello: str


@app.post("/greetings")
def post_greetings(request: GreetingsRequest) -> GreetingResponse:
    return GreetingResponse(hello=request.name)
