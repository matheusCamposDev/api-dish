import os
from datetime import timedelta


class Config:
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)


class DevelopmentConfig(Config):
    TESTING = False
    SECRET_KEY = "dev"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory"  # Banco de dados para testes
