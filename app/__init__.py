from flask import Flask
from app.routes import main  # Importing Blueprint
from app.config import Config  # Import the Config class

def create_app():
    """Factory function to create the Flask application."""
    app = Flask(__name__)

    # Load configurations from Config class
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(main)

    return app