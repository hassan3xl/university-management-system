import os
from pathlib import Path
from dotenv import load_dotenv

# Path to .env file relative to this file
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

if os.path.exists(env_path):
    load_dotenv(env_path)

def get_env_variable(var_name, default=None):
    """Get the environment variable or return default."""
    return os.getenv(var_name, default)
