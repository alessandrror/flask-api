from src.config.development import DevelopmentConfig
from src.config.production import ProductionConfig


class Config:
    def __init__(self):
        self.development_config = DevelopmentConfig()
        self.production_config = ProductionConfig()
