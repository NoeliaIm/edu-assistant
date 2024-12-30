import os
import tempfile

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from app.services.langflow_api_client import (
    run_flow,
    run_flow_historia,
    TWEAKS,
    BASE_API_URL,
    FLOW_ID_HISTORIA,
    upload_file
)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/run_langflow")
async def run_langflow_endpoint(input_message: str):
    try:
        result = run_flow(message=input_message, endpoint="9fff23d3-2565-4305-8544-b8adb39a1627")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/run_langflow_historia")
async def run_langflow_endpoint(input_message:  str = Form(...), file: UploadFile = File(None)):
    try:
        temp_file_path = None
        tweaks = TWEAKS

        if file:  # Solo procesamos el archivo si se ha proporcionado
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                temp_file_path = temp_file.name
                content = await file.read()
                temp_file.write(content)

            # Definir la ruta final
            output_dir = "C:/Users/noe/PycharmProjects/venv_assistant/uploads"
            final_path = os.path.join(output_dir, file.filename)

            # Configurar tweaks con ambas rutas
            tweaks = {
                "CustomComponent-2TrrY": {
                    "path": temp_file_path
                }
            }

        result = run_flow_historia(
            message=input_message,
            endpoint=FLOW_ID_HISTORIA,
            tweaks=tweaks
        )

        return result.get('outputs')[0]['outputs'][0]['outputs']['message']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Este bloque es opcional pero recomendado para ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.__main__:app", host="0.0.0.0", port=8000, reload=True)