import os

class Config:
    LANGFLOW_URL = os.getenv("LANGFLOW_URL", "http://127.0.0.1:7860")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "../uploads/")
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MB
    DEBUG = os.getenv("DEBUG", True)

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}