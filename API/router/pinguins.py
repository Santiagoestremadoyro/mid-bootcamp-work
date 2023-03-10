from fastapi import APIRouter
from mongo.conexion import db
from bson import json_util
from json import loads
import plotly.express as px
from fastapi.responses import JSONResponse
from bson.objectid import ObjectId

router = APIRouter()

def res(result):
    return loads(json_util.dumps(result))



@router.get("/all/pinguins")
def get_pinguins():
    result = db["pinguinos"].aggregate([
        {"$match":{"sex": {"$ne":None}}},
        {"$group": {"_id": "$sex", "count": {"$sum": 1}}}
    ])
    return res(result)

@router.get("/information/{penguin_id}")
def get_penguin_by_id(penguin_id):
    result= db.pinguinoss.find_one({"Individual ID": penguin_id})
    if not result:
        return {"error": "Penguin not found"}
    return res(result)



@router.get("/info/graph/{ind_id}")
def get_info_graph(ind_id):
    result = db["pinguinoss"].aggregate([
        {"$match":{"Individual ID": ind_id}},
        {"$group":{"_id": "$Individual ID"}}

    ])
    return res(result)



@router.get("/information/2/{ind_id}")
def get_penguin_by_id(ind_id):
    projection = {"_id": 0, "Delta 15 N (o/oo)": 0, "Delta 13 C (o/oo)": 0}
    result = db.pinguinoss.find_one({"Individual ID": ind_id}, projection)
    
    return res(result)



@router.get("/information/track/{ind_id}")
def get_penguin_by_id(ind_id):
    projection = {"_id": 0, "Delta 15 N (o/oo)": 0, "Delta 13 C (o/oo)": 0}
    result = db.pinguinoss.find({"Individual ID": ind_id}, projection)
    
    return res(result)



@router.get("/all/pinguins/specie")
def get_pinguins_s():
    result = db["pinguinos"].aggregate([
        {"$match":{"species": {"$ne":None}}},
        {"$group": {"_id": "$species", "count": {"$sum": 1}}}
    ])
    return res(result)

@router.get("/all/pinguins/islan")
def get_pinguins_i():
    result = db["pinguinos"].aggregate([
        {"$match":{"island": {"$ne":None}}},
        {"$group": {"_id": "$island", "count": {"$sum": 1}}}
    ])
    return res(result)





#separar pinguinos por sexo
@router.get("/pinguins/sex")
def penguins_by_sex():
    result = []
    for penguin in db["pinguinos"].find({}):
        result.append(penguin)
    return res(result)


#separar pinguinos por especies
@router.get("/pinguins/species/{species}")
def penguins_by_species(species: str):
    result = []
    for penguin in db["pinguinos"].find({"species": species}):
        result.append(penguin)
    return res(result)

#separar pinguinos por islas de donde provienen
@router.get("/pinguins/island/{island}")
def penguins_by_island(island: str):
    result = []
    for penguin in db["pinguinos"].find({"island": island}):
        result.append(penguin)
    return res(result)



