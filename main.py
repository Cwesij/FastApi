from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# pydantic base model
class Post(BaseModel):
    title: str
    author: str
    published: bool = False
    rating: Optional[int] = None


my_posts = [{"title": "Story of Peter Pan", "author": "Jeremy Lin", "id": 1}, {"title": "Harry Potter", "author": "Drake Miles", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == int(id):
            return p
    

@app.get("/posts")
def get_posts():
    return {"Posts": my_posts}


@app.post("/posts")
def create_posts(new_post: Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(2, 10000000)
    my_posts.append(post_dict)
    return {"Data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"Data": post}