from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class FormData(BaseModel):
    username: str
    password: str


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/items")
async def read_item1(body: Item):
    return body


@app.post("/login")
async def login(data: Annotated[FormData, Form()]):
    return data


# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    print(file, 123)
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# venv\Scripts\activate.bat
