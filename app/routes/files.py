from flask import Blueprint, request, jsonify
from app.services.file_service import save_file

bp = Blueprint("files", __name__)

@bp.route("/upload", methods=["POST"])
def upload_file():
    try:
        flow_id = request.form.get("flow_id")
        file = request.files.get("file")

        if not flow_id or not file:
            return jsonify({"error": "Se requiere 'flow_id' y un archivo"}), 400

        # Guardar el archivo
        file_path = save_file(flow_id, file)

        return jsonify({"file_path": file_path}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500