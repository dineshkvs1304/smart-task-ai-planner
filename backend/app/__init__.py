from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.utils.logger import setup_logger

db = SQLAlchemy()
logger = setup_logger()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)

    logger.info("Starting Smart Task AI Backend")

    from app.routes.task_routes import task_bp
    app.register_blueprint(task_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app