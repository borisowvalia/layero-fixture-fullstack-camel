"""Бэкенд фикстуры. Все маршруты объявлены под /api — edge уводит туда
именно этот префикс и не срезает его."""
import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hello")
def hello():
    return {"message": "привет от fastapi"}


@app.get("/api/health")
def health():
    return {"ok": True, "port": os.environ.get("PORT")}
