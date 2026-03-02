import os

class Config:
    SECRET_KEY = "smart-task-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False