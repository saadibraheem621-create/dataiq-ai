from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()

    df = pd.read_csv(io.BytesIO(content))

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "columns_names": list(df.columns)
    }