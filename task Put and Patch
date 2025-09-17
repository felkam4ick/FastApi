import uvicorn
from fastapi import FastAPI, Body, Query

app = FastAPI()


homes = [
    {"id" : 1, "city" : "Донецк" ,"street" : "Прожекторная", "number" : 8},
    {"id" : 2, "city" : "Макеевка" ,"street" : "Щетинина", "number" : 3},
    {"id" : 3, "city" : "Донецк" ,"street" : "Бульвар-Шевченко", "number" : 10},
]




@app.get("/home")
async def get_homes(city : str | None = None):
    homes_append = []
    if city != None:
        for i in homes:
            if i["city"] == city:
                homes_append.append(i)
        return homes_append

    return homes


@app.delete("/home/{home_id}")
async def delete_home(home_id : int):
    for i in homes:
        if i["id"] == home_id:
            homes.remove(i)
    return {"status" : "OK", "homes" : homes}


@app.post("/home")
async def post_home(city : str = Body(description = "Город дома"), street : str = Body(), number : int = Body()):

    homes.append({
        "id" : homes[-1]["id"] + 1,
        "city" : city,
        "street" : street,
        "number" : number})
    return {"homes" : homes}


@app.put("/home/{home_id}")
async def put_home(
                home_id : int,
                city : str = Body(),
                street : str = Body(),
                number : int = Body()
):
    for i in homes:
        if i["id"] == home_id and city != None and street != None and number != None:
            i["city"] = city
            i["street"] = street
            i["number"] = number

    return {"homes" : homes}


@app.patch("/home/{home_id}")
async def patch_home(
        home_id : int,
        city: str | None = Body(None),
        street: str | None = Body(None),
        number: int | None = Body(None)
):
    for i in homes:
        if i["id"] == home_id:
            if city:
                i["city"] = city
            if street:
                i["street"] = street
            if number:
                i["number"] = number
    return {"homes" : homes}
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)
