from fastapi import FastAPI
import uvicorn

from app.resolver import random_genres_items
from resolver import random_items

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello MovieR"}

@app.get("/all")
async def all_movies():
    result = random_items()
    return {"result": result}
@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_genres_items(genre)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
