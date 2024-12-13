from flask import Blueprint, request, jsonify
from app.services.langflow_api_client import run_flow, run_flow_historia

bp = Blueprint("flows", __name__)

@bp.route("/run_langflow", methods=["POST"])
def run_langflow_route():
    try:
        data = request.get_json()
        input_message = data.get("input_message")

        if not input_message:
            return jsonify({"error": "input_message is required"}), 400

        result = run_flow(message=input_message, endpoint="9fff23d3-2565-4305-8544-b8adb39a1627") # O usa data.get("endpoint") si quieres pasar el endpoint dinámicamente
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/run_langflow_historia", methods=["POST"])
def run_langflow_route():
    try:
        data = request.get_json()
        input_message = data.get("input_message")

        if not input_message:
            return jsonify({"error": "input_message is required"}), 400

        result = run_flow_historia(message=input_message, endpoint="aa641b6d-318c-405e-af68-665bd64eee6f") # O usa data.get("endpoint") si quieres pasar el endpoint dinámicamente
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500