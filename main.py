from fastapi import FastAPI
from configs.Environment import get_environment_variables
from models.base_model import init
from routers.v1.card_router import CardRouter
from routers.v1.columns_router import ColumnRouter
from routers.v1.aplication_router import AplicationRouter
from routers.v1.attachments_router import AttachmentsRouter
from routers.v1.challenge_router import ChallengeRouter
from routers.v1.comments_router import CommentsRouter
from routers.v1.startup_router import StartupRouter
from routers.v1.tasks_router import TaskRouter
from routers.v1.user_router import UserRouter


env = get_environment_variables()
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)

app.include_router(CardRouter)
app.include_router(ColumnRouter)
app.include_router(AplicationRouter)
app.include_router(AttachmentsRouter)
app.include_router(ChallengeRouter)
app.include_router(CommentsRouter)
app.include_router(StartupRouter)
app.include_router(TaskRouter)
app.include_router(UserRouter)




init()





