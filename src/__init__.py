import os

from dotenv import load_dotenv
from flask import Flask

from src.config.config import Config
from src.constants import ENV_MODE

load_dotenv(override=True)

app = Flask(__name__)

mode = os.environ.get(ENV_MODE)

config = Config().production_config if mode == Config().production_config.ENV else Config().development_config
