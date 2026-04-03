from fastapi import FastAPI
from api import content

app = FastAPI()

app.include_router(content.router)