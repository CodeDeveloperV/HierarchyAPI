import os


class Config(object):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')


class Development(Config):
    """
    Development environment configuration
    """

    DEBUG = True
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = "5000"


class Production(Config):
    """
    Production environment configurations
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = "6000"


app_config = {
    "development": Development,
    "production": Production
}
