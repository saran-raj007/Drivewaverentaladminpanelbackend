from fastapi import FastAPI,Request,Depends
from fastapi.middleware.cors import CORSMiddleware
#from router import router
from sqlalchemy.orm import Session
import models
#from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 
from starlette.middleware.sessions import SessionMiddleware
from datetime import datetime
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse,RedirectResponse
app = FastAPI()

app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key="e8Lj5R$Zv@n8!sWm3P#q")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request:Request):
    return {"hello": "Drive Wave"}

#app.include_router(router, prefix='')
@app.get("/login")
def get_Dashboard(request:Request):
    
    total_orders=0
    completed_orders=0
    return templates.TemplateResponse('login.php', context={'request': request,"total_orders":total_orders,"completed_orders":completed_orders})

@app.get("/Dashboard")
def get_Dashboard(request:Request):
    
    total_orders=0
    completed_orders=0
    return templates.TemplateResponse('dashboard.php', context={'request': request,"total_orders":total_orders,"completed_orders":completed_orders})


@app.get("/bike")
def get_Dashboard(request:Request):
    total_orders=0
    completed_orders=0
    return templates.TemplateResponse('bike.php', context={'request': request,"total_orders":total_orders,"completed_orders":completed_orders})

@app.get("/add_bikes")
def get_Dashboard(request:Request):
    total_orders=0
    completed_orders=0
    return templates.TemplateResponse('add_bike.php', context={'request': request,"total_orders":total_orders,"completed_orders":completed_orders})

@app.get("/car")
def get_Dashboard(request:Request):
    total_orders=0
    completed_orders=0
    return templates.TemplateResponse('car.php', context={'request': request,"total_orders":total_orders,"completed_orders":completed_orders})

@app.get("/add_cars")
def get_Dashboard(request:Request):
    total_orders=0
    completed_orders=0
    return templates.TemplateResponse('add_cars.php', context={'request': request,"total_orders":total_orders,"completed_orders":completed_orders})



@app.get("/rent_request")
def get_Dashboard(request:Request):
    total_orders=0
    completed_orders=0
    return templates.TemplateResponse('rentrequest.php', context={'request': request,"total_orders":total_orders,"completed_orders":completed_orders})

@app.get("/query_request")
def get_Dashboard(request:Request):
    total_orders=0
    completed_orders=0
    return templates.TemplateResponse('query.php', context={'request': request,"total_orders":total_orders,"completed_orders":completed_orders})
   
    


