"""Import configuration files."""

from src.config.development import DevelopmentConfig
from src.config.production import ProductionConfig


class Config:
    """Create the Config Class."""

    def __init__(self):
        """Initialize self config classes as Config properties."""
        self.development_config = DevelopmentConfig()
        self.production_config = ProductionConfig()
