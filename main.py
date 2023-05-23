from fastapi import FastAPI
from configs.Environment import get_environment_variables
from models.base_model import init
from routers.v1.card_router import CardRouter


env = get_environment_variables()
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)

app.include_router(CardRouter)


init()




