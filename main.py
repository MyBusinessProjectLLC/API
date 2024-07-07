from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from models import User
from sqlalchemy.orm import Session


async def get_db():
    db = SessionLocal()  # Assuming SessionLocal is defined elsewhere
    try:
        yield db
    finally:
        db.close()
        
app = FastAPI()

@app.on_event("startup")
def startup():
    SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)
    yield SessionLocal

@app.on_event("shutdown")
def shutdown(session: SessionLocal):
    session.close()

@app.get("/", summary="Main info")
def read_item():
    
    return {"data": "Hello"}