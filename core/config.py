import os

from pydantic import BaseSettings
from my_settings import DB_URL


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DB_URL: str = f"mysql+pymysql://{DB_URL['user']}:{DB_URL['password']}@{DB_URL['host']}:{DB_URL['port']}/{DB_URL['db']}"
    JWT_SECRET_KEY: str = "cardoc"
    JWT_ALGORITHM: str = "HS256"


class DevelopmentConfig(Config):
    DB_URL: str = f"mysql+pymysql://{DB_URL['user']}:{DB_URL['password']}@{DB_URL['host']}:{DB_URL['port']}/{DB_URL['db']}"


class LocalConfig(Config):
    DB_URL: str = f"mysql+pymysql://{DB_URL['user']}:{DB_URL['password']}@{DB_URL['host']}:{DB_URL['port']}/{DB_URL['db']}"


def get_config():
    env = os.getenv("EVN", "development")
    config_type = {
        "development": DevelopmentConfig(),
        "local": LocalConfig(),
    }
    return config_type[env]


config = get_config()

