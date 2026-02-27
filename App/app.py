from fastapi import FastAPI , HTTPException
from App.schema import PostCreate ,PostResponse
app = FastAPI()



@app.get("/hello world")
def hello_world():
    return {"message": "Hello World"} #json response 


text_posts = {
    1: {"title": "First Post", "content": "This is the very first post in our collection. Welcome!"},
    2: {"title": "Getting Started", "content": "Here's how to get started with posting content."},
    3: {"title": "Daily Tips", "content": "Tip #1: Always proofread before posting your content."},
    4: {"title": "Weekend Plans", "content": "What are your plans for the weekend? Share below!"},
    5: {"title": "Midweek Motivation", "content": "Keep pushing forward - you're halfway through the week!"},
    6: {"title": "Tech News", "content": "Latest updates in AI and machine learning technology."},
    7: {"title": "Cooking Recipes", "content": "Try this simple pasta recipe for dinner tonight."},
    8: {"title": "Book Recommendations", "content": "Top 5 books everyone should read this year."},
    9: {"title": "Fitness Journey", "content": "Day 9 of my 30-day fitness challenge update."},
    10: {"title": "Final Thoughts", "content": "Wrapping up our first 10 posts. What's next?"}
}

            
                    
@app.get("/posts")
def get_posts(limists: int = None):
   if limists :
       return list(text_posts.values())[:limists]
   return text_posts 

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts :
       raise HTTPException(status_code=404, detail="Post not found") 
    return text_posts.get(id)

@app.post("/posts")
def create_post(post:PostCreate) -> PostResponse : 
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys())+1]= new_post
    return new_post

    