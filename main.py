from  fastapi import FastAPI
from fastapi_admin.factory import app as admin_app

from pydantic import BaseModel
app=FastAPI()
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)

app.mount('/admin', admin_app)

@fast_app.on_event('startup')
async def startup():
    await admin_app.init(
        admin_secret="test",
        permission=True,
        site=Site(
            name="FastAPI-Admin DEMO",
            login_footer="FASTAPI ADMIN - FastAPI Admin Dashboard",
            login_description="FastAPI Admin Dashboard",
            locale="en-US",
            locale_switcher=True,
            theme_switcher=True,
        ),
    )
db=[]

class City(BaseModel):
    name:str
    timezone:str

@app.get('/')
def index():
    return {'key':'value'}

@app.get('/cities')
def get_cities():
    return db

#@app.get('/cities/{city_id}')
@app.post('/cities')
def create_city(city:City):
    db.append(city.dict())
    return db[-1]
#@app.delete('/cities')