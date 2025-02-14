import os
from dotenv import load_dotenv

# Load environment variables from .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')  # Use default if not set
    JSON_DATA_FILE = os.path.join(basedir, 'static', 'data', 'sample_products.json')  # Path to JSON file
