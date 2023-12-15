from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def root() -> dict[str, str]:
    """
    Root endpoint.
    """
    from app.version import __version__
    return {'version': __version__}


@app.get('/health')
async def health() -> dict[str, str]:
    """
    Health check.
    """
    return {'msg': "I'm healthy!"}
