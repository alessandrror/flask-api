"""Development Configuration."""


class DevelopmentConfig:
    """Create the Development Configuration Class."""

    def __init__(self):
        """Initialize self development configuration properties."""
        self.ENV = "development"
        self.DEBUG = True
        self.PORT = 5000
        self.HOST = "localhost"
