from fastapi import FastAPI, UploadFile, File, Form
from fastapi_backend.rag_pipeline import process_query
from pathlib import Path 

app = FastAPI()
 
@app.post("/api/query")
async def query(file: UploadFile = File(...), prompt: str = Form(...)):
    content = await file.read()
    filename = Path(file.filename).name #secure the clean filename
    print(f"[DEBUG] Received file: {filename}")
    result = process_query(filename, content, prompt)
    return {"result": result}
