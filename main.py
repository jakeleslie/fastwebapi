# Imports so my API can work properly
from fastapi import FastAPI, status, Response
import simplejson as json

# Setting app to be my initialization of fast api
app = FastAPI()

# Storing my JSON file into a variable so that I can work with the file. 
with open('pokedex.json') as fin:
    content = fin.read()
    obj = json.loads(content)

# On the homepage it displays a welcome message
@app.get("/")
async def read_root():
    return {"Welcome to Poke-API!"}

# Allows the user to enter in a parameter for the ID, and it will display all the information for a pokemon. Ex: localhost:8000/id/12
@app.get("/id/{id}")
async def get_id(id, response: Response):
    try:
        res = [x for x in obj if x['id'] == int(id)] #since our parameter is a a number we have to write a list comprehension to check if it exists

        if len(res) == 0: #if nothing is entered return an error
            return 401
        else:
            return res[0] #if there is something return the response

    except KeyError: #catching our errors, and returning if there is an internal server error
        result = {"err":f"No such {id}"}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result

# returns the name of a specific id in english, japanese, chinese, and french. Same code layout as the others
@app.get("/id/{id}/name")
async def get_name(id, response: Response):
    try:
        res = [x['name'] for x in obj if x['id'] == int(id)] #Difference here is that we check for the name subset of the ID but we are still checking the ID with the comprehension
        return res[0]
    except KeyError:
        result = {"err":f"No such {id} "}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result

# Shows the type of a specific ID. 
@app.get("/id/{id}/type")
async def get_type(id, response: Response):
    try:
        res = [x['type'] for x in obj if x['id'] == int(id)] #Same as above but instead of name we use type. 

        return res[0]
    except KeyError:
        result = {"err":f"No such {id} "}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result

# Returns the base stats of a pokemon with specific ID.  
@app.get("/id/{id}/base")
async def get_base(id, response: Response):
    try:
        res = [x['base'] for x in obj if x['id'] == int(id)] # Same as above but instead of name we check for base stats. 

        return res[0]
    except KeyError:
        result = {"err":f"No such {id} "}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result

