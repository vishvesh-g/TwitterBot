from pydantic.main import BaseModel
from sqlalchemy.sql.sqltypes import String
from dm import ats
from fastapi import FastAPI, HTTPException
from starlette import status
from fastapi.params import Body, Depends
from starlette.responses import Response
import schemas
import models
from database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session, session
from twitterAPI import TwitterAPI
models.Base.metadata.create_all(engine)
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, status

class UpadteData(BaseModel):
    data:str

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/input', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Twitter, db: Session = Depends(get_db)):
    temp = models.Twitter(title=request.title)
    db.add(temp)
    db.commit()
    db.refresh(temp)
    return temp

@app.post('/update/{title}')
def update(title:str, data:UpadteData, response: Response, db: Session = Depends(get_db)):
    ##print(data,title)
    x=db.query(models.Twitter).filter(models.Twitter.title == title).first()
    x.accounts=data.data
    db.commit()


@app.get('/send/{title}')
def send(title,response: Response, db: Session = Depends(get_db)):
    x = db.query(models.Twitter).filter(models.Twitter.title == title).first()
    ##print(x.title)
    ats(x.accounts)
    
@app.get('/accounts/{title}')
def show(title, response: Response, db: Session = Depends(get_db)):
    x = db.query(models.Twitter).filter(models.Twitter.title == title).first()
    print(x.title)
    acc, id = TwitterAPI(x.title)
    print(acc)
    temp = db.query(models.Twitter).filter(models.Twitter.title == title).update(
        {'accounts': json.dumps({"acc":acc}), 'accountsId': json.dumps({"id":id})}, synchronize_session=False)
    db.commit()
    x = db.query(models.Twitter).filter(models.Twitter.title == title).first()
    return x

@app.get('/home')
def all(db: Session = Depends(get_db)):
    data = db.query(models.Twitter).all()
    return data

