from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import version
from app.core.config import settings

app = FastAPI(
    version=version.__version__
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def root() -> dict[str, str]:
    """
    Root endpoint.
    """
    return {'version': version.__version__}


@app.get('/health')
async def health() -> dict[str, str]:
    """
    Health check.
    """
    return {'msg': "I'm healthy!"}
