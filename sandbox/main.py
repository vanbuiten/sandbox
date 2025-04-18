from fastapi import FastAPI
from pydantic import BaseModel

from sandbox.utils import get_version

app = FastAPI()


class RootResponse(BaseModel):
    status: str = "ok"
    version: str


@app.get("/")
def read_root() -> RootResponse:
    """
    Root path
    """
    version = get_version()
    return RootResponse(version=version)
