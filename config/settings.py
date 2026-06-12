import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://reqres.in/api")
REQRES_API_KEY = os.getenv("REQRES_API_KEY", "")

STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
STANDARD_PASSWORD = os.getenv("STANDARD_PASSWORD", "secret_sauce")
LOCKED_OUT_USER = os.getenv("LOCKED_OUT_USER", "locked_out_user")
