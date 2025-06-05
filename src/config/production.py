"""Production Configuration."""


class ProductionConfig:
    """Create the Production Configuration Class."""

    def __init__(self):
        """Initialize self production configuration properties."""
        self.ENV = "production"
        self.DEBUG = False
        self.PORT = 80
        self.HOST = "0.0.0.0"
