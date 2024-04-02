import os

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOSTNAME')}/{os.environ.get('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False