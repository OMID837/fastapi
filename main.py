# from fastapi import FastAPI,Body
# from pydantic import BaseModel
# import uvicorn

# class CreatePostIn(BaseModel):
#     title:str
#     content:str

# app = FastAPI()

# @app.get('/')
# async def root():
#     return {'message': 'hello omid'}

# @app.get('/test1/{slug}')
# async def test1(slug):
#     return {'test1': 'omid'}


# @app.post('/create')
# async def create_post(Post:CreatePostIn = Body()):
#     return Post

# @app.get('/create')
# async def create_post(Get:CreatePostIn):
#     return Get


# from fastapi import FastAPI, Body
# from pydantic import BaseModel
# import uvicorn

# class CreatePostIn(BaseModel):
#     title: str
#     content: str

# app = FastAPI()

# @app.get('/')
# async def root():
#     return {'message': 'hello omid'}

# @app.get('/test1/{slug}')
# async def test1(slug: str):
#     return {'test1': slug}

# @app.post('/create')
# async def create_post(post: CreatePostIn = Body()):
#     return post

# @app.get('/create_post')
# async def get_create_post(get: CreatePostIn):
#     return get

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI

from db.engine import Base, engine
from routers.users import router as user_router

app = FastAPI()


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(user_router, prefix="/users")