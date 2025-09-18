from fastapi import  Body, APIRouter,Depends
from schemas.house import HomePUT, HomePATCH, HomePagination
from pydantic import BaseModel

class HomePUT(BaseModel):
    city : str 
    street : str
    number : int

class HomePATCH(BaseModel):
    city : str | None = None
    street : str | None = None
    number : int | None = None

class HomePagination(BaseModel):
    page : int | None = None
    per_page : | None = None

route = APIRouter(prefix="/house", tags=["Дома"])


homes = [
    {"id" : 1, "city" : "Донецк" ,"street" : "Прожекторная", "number" : 8},
    {"id" : 2, "city" : "Макеевка" ,"street" : "Щетинина", "number" : 3},
    {"id" : 3, "city" : "Торез" ,"street" : "Мурманская", "number" : 19},
    {"id" : 4, "city" : "Зугрес" ,"street" : "Победы", "number" : 2},
    {"id" : 5, "city" : "Амросиевка" ,"street" : "Ватутина", "number" : 1},
    {"id" : 6, "city" : "Снежное" ,"street" : "Кокинаки", "number" : 18},
    {"id" : 7, "city" : "Шахтерск" ,"street" : "Иванова", "number" : 7},
    {"id" : 8, "city" : "Торез" ,"street" : "Театральная", "number" : 2},
    {"id" : 9, "city" : "Донецк" ,"street" : "Бульвар-Шевченко", "number" : 10},
    {"id" : 10, "city" : "Донецк" ,"street" : "Марии-Ульяновой", "number" : 6},
    {"id" : 11, "city" : "Макеевка" ,"street" : "Щетинина", "number" : 3},
    {"id" : 12, "city" : "Харцызск" ,"street" : "Лебедя", "number" : 19},
]





@route.get("/h",summary="Вывод по страницам")
async def get_page_homes(home_data : HomePagination = Depends()):
        if home_data.page != None and home_data.per_page != None:
            start = (home_data.per_page * home_data.page) - home_data.per_page
            end = start + home_data.per_page
            return homes[start:end ]
        elif home_data.page != None and home_data.per_page == None:
            start = (3 * home_data.page) - 3
            end = start + 3
            return homes[start:end ]
        elif home_data.page == None and home_data.per_page != None:
            start = (home_data.per_page * 1) - home_data.per_page
            end = start + home_data.per_page
            return homes[start:end ]
        elif home_data.page == None and home_data.per_page == None:
            return homes[0:3]





@route.get("", summary="Вывод по айди или всех домов")
async def get_homes(city : str | None = None):
    homes_append = []
    if city != None:
        for i in homes:
            if i["city"] == city:
                homes_append.append(i)
        return homes_append

    return homes


@route.delete("/{home_id}", summary="Удаление по айди" )
async def delete_home(home_id : int):
    for i in homes:
        if i["id"] == home_id:
            homes.remove(i)
    return {"status" : "OK", "homes" : homes}


@route.post("", summary="Добавление дома")
async def post_home(home_data : HomePUT):

    homes.append({
        "id" : homes[-1]["id"] + 1,
        "city" : home_data.city,
        "street" : home_data.street,
        "number" : home_data.number})
    return {"homes" : homes}


@route.put("/{home_id}", summary="Полное обновление дома")
async def put_home(home_id : int, home_data : HomePUT = Body(openapi_examples={
    "1" : {"summary" : "Донецк", "value" : {
    "city" : "Донецк",
    "street" : "Чижика",
    "number" : 27
}},
    "2" : {"summary" : "Торез", "value" : {
    "city" : "Торез",
    "street" : "Ульяновой",
    "number" : 12
}},

})
):
    for i in homes:
        if i["id"] == home_id and home_data.city != None and home_data.street != None and home_data.number != None:
            i["city"] = home_data.city
            i["street"] = home_data.street
            i["number"] = home_data.number

    return {"homes" : homes}


@route.patch("/{home_id}", summary="Частичное обновление дома")
async def patch_home(home_id : int, home_data : HomePATCH = Body(openapi_examples={
    "1" : {"summary" : "Без улицы", "value" : {
        "city" : "Торез",
        "number" : 33
    }
},
    "2" : {
    "summary" : "Без города", "value" : {
        "street" : "Чижика",
        "number" : 21
    }
}

})):
    for i in homes:
        if i["id"] == home_id:
            if home_data.city:
                i["city"] = home_data.city
            if home_data.street:
                i["street"] = home_data.street
            if home_data.number:
                i["number"] = home_data.number
    return {"homes" : homes}
