from flask import Flask
from flask_cors import CORS
from config.config import config
from config.logging_config import setup_logging

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    setup_logging()

    CORS(app)  # Habilitar CORS

    # Registrar las rutas
    from app.routes import flows, files, subjects, configs
    app.register_blueprint(flows.bp, url_prefix="/api/flows")
    app.register_blueprint(files.bp, url_prefix="/api/files")
    app.register_blueprint(subjects.bp, url_prefix="/api/subjects")
    app.register_blueprint(configs.bp, url_prefix="/api/configs")

    return app