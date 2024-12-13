import os
from werkzeug.utils import secure_filename
from config.config import config

UPLOAD_FOLDER = config["development"].UPLOAD_FOLDER

def save_file(flow_id, file):
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, flow_id, filename)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    file.save(file_path)

    return file_path