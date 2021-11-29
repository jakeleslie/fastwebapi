from fastapi import FastAPI, status, Response

app = FastAPI()

users = {
    "Serdar": {
        "id" : 32,
        "full_name" : "Serdar Yegulalp"
    },
    "Jake": {
        "id": 21,
        "full_name" : "Jake Leslie"
    }
}

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/user/{username}")
async def get_user(username, response: Response):
    try:
        result = users[username]
    except KeyError:
        result = {"err":f"No such user: {username}"}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result
