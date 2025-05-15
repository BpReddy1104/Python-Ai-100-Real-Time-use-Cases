from fastapi import FastAPI
from app.routers import blog
from app.database.database import engine, Base
from app.models import blog as blog_model

Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(blog.router)