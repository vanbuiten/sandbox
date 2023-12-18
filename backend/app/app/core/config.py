import secrets
from typing import Any, List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @field_validator('BACKEND_CORS_ORIGINS', mode='before')
    def assemble_cors_origins(cls, v: str) -> Union[List[str], str]:  # noqa N805
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @field_validator('SQLALCHEMY_DATABASE_URI', mode='before')
    def assemble_db_connection(cls, v: Optional[str], info: FieldValidationInfo) -> Any:  # noqa N805
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql',
            username=info.data.get('POSTGRES_USER'),
            password=info.data.get('POSTGRES_PASSWORD'),
            host=info.data.get('POSTGRES_SERVER'),
            path=f"{info.data.get('POSTGRES_DB') or ''}",
        )

settings = Settings()
