from fastapi import FastAPI, UploadFile
from azure.storage.blob import BlobServiceClient

app=FastAPI()

conn_str=""
container="uploads"

blob_service=BlobServiceClient.from_connection_string(conn_str)

@app.post("/upload")

async def upload(file: UploadFile):
    blob_client=blob_service.get_blob_client(container=container, blob=file.filename)
    data=await file.read()
    blob_client.upload_blob(data, overwrite=True)
    return {"status":"uploaded"}