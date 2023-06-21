from fastapi import FastAPI

app = FastAPI()


# @ decorator for path operator 
# then fastapi instance follow by the http verb
@app.get("/")
def root():
    return {"message": "welcome to my API!!!"}


@app.get("/posts")
def get_posts():
    return {"data": "this is your post"}

@app.post("/createpost")
def get_createpost():
    return {"message": "sucefully created post"}