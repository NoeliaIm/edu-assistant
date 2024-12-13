import requests
from typing import Dict, Any
from fastapi import HTTPException


class LangflowService:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def query_flow(self, flow_id: str, request_data: Dict[str, Any]) -> Dict:
        """
        Procesa una petición POST hacia Langflow

        Args:
            flow_id: ID del flujo de Langflow
            request_data: Datos recibidos en la petición POST
        """
        url = f"{self.base_url}/api/v1/run/{flow_id}"

        try:
            response = requests.post(
                url,
                json=request_data,
                params={"stream": request_data.get("stream", False)}
            )
            response.raise_for_status()
            return response.json()

        except requests.RequestException as e:
            raise HTTPException(
                status_code=response.status_code if response else 500,
                detail=f"Error al comunicarse con Langflow: {str(e)}"
            )

    async def upload_file(self, flow_id: str, file_data) -> Dict:
        """
        Sube un archivo a Langflow
        """
        url = f"{self.base_url}/api/v1/files/upload/{flow_id}"

        try:
            files = {"file": file_data}
            response = requests.post(url, files=files)
            response.raise_for_status()
            return response.json()

        except requests.RequestException as e:
            raise HTTPException(
                status_code=response.status_code if response else 500,
                detail=f"Error al subir archivo a Langflow: {str(e)}"
            )