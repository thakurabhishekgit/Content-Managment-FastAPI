from fastapi import FastAPI
from api import content , users , collab

app = FastAPI()

app.include_router(content.router)
app.include_router(users.router)
app.include_router(collab.router)