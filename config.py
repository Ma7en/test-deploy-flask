import os 

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(32))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI','sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False