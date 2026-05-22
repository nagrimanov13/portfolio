from pydantic_settings import BaseSettings
from pydantic import Field, computed_field

class Settings(BaseSettings):
    postgres_user: str = Field("rooted", env="POSTGRES_USER")
    postgres_password: str = Field("rooted", env="POSTGRES_PASSWORD")
    postgres_db: str = Field("rooted", env="POSTGRES_DB")
    postgres_host: str = Field("127.0.0.1", env="POSTGRES_HOST")

    class Config:
        env_file = '.env'

    @computed_field
    @property
    def database_url(self: object) -> str:
        return f'postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:5432/{self.postgres_db}'

settings = Settings()
