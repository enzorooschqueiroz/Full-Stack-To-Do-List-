from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
import redis
from .routes.assignment_routes import assignment_bp
from .routes.user_routes import user_bp
from .config import Config

db = MongoEngine()

redis_client = redis.StrictRedis(
    host= config.get('REDIS_HOST'),
    port= config.get('REDIS_PORT'),
    db = 0
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    jwt = JWTManager(app)

    app.register_blueprint(assignment_bp)
    app.register_blueprint(user_bp)

    app.redis_client = redis_client

    return app
