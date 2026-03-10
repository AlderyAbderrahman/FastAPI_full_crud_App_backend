from fastapi import FastAPI , HTTPException , File, UploadFile, Depends , Form
from App.schema import PostCreate ,PostResponse
from .db import create_db_and_tables, get_async_session, post
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    caption: str = Form(...), 
    db: AsyncSession = Depends(get_async_session)
    ):
             Post=post(caption=caption, url="fake_url",
             file_type="image",
             file_name="fake_name"
             )

             db.add(Post)
             await db.commit()

@app.get("/feed")
async def get_feed(db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(post).order_by(post.created_at.desc()))
    posts=[row[0] for row in result.all()]
    posts_data=[]
    for Post in posts:
        posts_data.append(
              {
                    "id": Post.id,
                    "caption": Post.caption,
                    "url": Post.url,
                    "file_type": Post.file_type,
                    "file_name": Post.file_name,
                    "created_at": Post.created_at
              }
        ) 
    return {"posts": posts_data}


