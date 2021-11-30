from fastapi import FastAPI, status, Response
import simplejson as json

app = FastAPI()

with open('pokedex.json') as fin:
    content = fin.read()
    obj = json.loads(content)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/id/{id}")
async def get_id(id, response: Response):
    try:
        res = [x for x in obj if x['id'] == int(id)]

        if len(res) == 0:
            return 401
        else:
            
            return res[0]

    except KeyError:
        result = {"err":f"No such {id}"}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result
# returns the type of a specific id
@app.get("/id/{id}/type")
async def get_type(id, response: Response):
    try:
        res = [x['type'] for x in obj if x['id'] == int(id)]

        return res[0]
    except KeyError:
        result = {"err":f"No such {id} "}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result

