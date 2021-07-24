from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Optional
from pydantic import BaseModel



app=FastAPI()
template=Jinja2Templates("htmlfiles")

class AssignmentData(BaseModel):
    user_name: str
    assign_no: int
    description: str



#@app.get("/home")                             #get request
#def home():
 #   return "AM not  HOME yoooo"

@app.post("/home/assignment",response_class=HTMLResponse)
def submit_assign(request:Request,assign_d: AssignmentData):
    return template.TemplateResponse("home.html",{"request":request})

    
    #return {
        #"user":assign_d.user_name,
        #"number": assign_d.assign_no,
        #"submit":"Success"
        
    #}
#Query parameter also handles by get request
#     /home/queries/suyog?query="FAQs"
@app.get("/home/queries/{user}")
def handl_query(user:str,query: Optional[str]):
    return {
        "username":user,
        "query":query
    }


@app.get("/",response_class=HTMLResponse)
def base_home(request:Request):
    print("I am goint to return html file")
    return template.TemplateResponse("home.html",{"request":request})



@app.get("/home/{user}")                             #get request
def home(user:str):
    return {
        "username":user
    }


