import os

class Config:

    SECRET_KEY = '@BLESSEDcate2021'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cate:cate1234@localhost/catherine'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres://dnszuspxfadque:ac02ef3308d20113910971fa7f111e4b8b668d65916702706843eeec4c281a1f@ec2-52-200-215-149.compute-1.amazonaws.com:5432/daav9iahhurm5f'


    #  email configurations
    MAIL_SERVER = 'kuicatherine7@gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
     if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

        SQLALCHEMY_DATABASE_URI=uri
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # or other relevant config var
    # if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #   SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    # # rest of connection code using the connection string `uri`
    pass
class TestConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}