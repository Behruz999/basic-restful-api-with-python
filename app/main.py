from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)
    return app


app = create_app()

# from fastapi import FastAPI, Form, File, UploadFile, staticfiles
# from pydantic import BaseModel
# from typing import Annotated
# from pathlib import Path

# app = FastAPI()
# Staticfiles = staticfiles.StaticFiles


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class FormData(BaseModel):
#     username: str
#     password: str


# BASE_DIR = Path(__file__).resolve().parent
# app.mount(
#     "/static", Staticfiles(directory=BASE_DIR / "static", html=True), name="static"
# )


# @app.get("/")
# async def read_root():
#     return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}


# @app.post("/items")
# async def read_item1(body: Item):
#     return body


# @app.post("/login")
# async def login(data: Annotated[FormData, Form()]):
#     return data


# # async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
# #     return {"username": username}


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     print(file, 123)
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}


# # venv\Scripts\activate.bat
