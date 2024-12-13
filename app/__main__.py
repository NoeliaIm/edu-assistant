from http.client import HTTPException

from fastapi import FastAPI

from app.services.langflow_api_client import run_flow, run_flow_historia

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
async def run_langflow_endpoint(input_message: str):
    try:
        result = run_flow_historia(message=input_message, endpoint="aa641b6d-318c-405e-af68-665bd64eee6f")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Este bloque es opcional pero recomendado para ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.__main__:app", host="0.0.0.0", port=8000, reload=True)