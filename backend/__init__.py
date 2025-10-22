from flask import Flask
from backend.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')
    db.init_app(app)
    return app