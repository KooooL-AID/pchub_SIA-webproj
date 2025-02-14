from flask import Flask
from app.routes import main  # Importing Blueprint

def create_app():
    """Factory function to create the Flask application."""
    app = Flask(__name__)

    # Load configurations
    app.config.from_pyfile('config.py')

    # Register Blueprints
    app.register_blueprint(main)

    return app
