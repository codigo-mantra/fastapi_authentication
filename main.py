# code originally from - https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from typing import Union
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
import pyotp, uvicorn
from sqlalchemy.orm import Session
from userapi import models
from resources import schemas
from settings.database import SessionLocal, engine
from settings.security import pwd_context
from settings.database import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from services import user_service
from services.auth_service import *
from fastapi.responses import JSONResponse


models.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

@app.get("/")
def home_api():
    response = {"message": "It's working!"}
    return response

@app.post("/api/user/login/", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email},
                                       expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/user/logout/", response_model=schemas.User)
async def logout(current_user: schemas.User = Depends(get_current_active_user)):
    token_response = expires_access_token(data={"sub": current_user.email})
    return JSONResponse(content={"message": "Logged out successfully!", "status":status.HTTP_301_MOVED_PERMANENTLY})
    # return token_response


@app.get("/api/user/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_active_user)):
    return current_user


@app.put("/api/user/me/", response_model=schemas.User)
def user_update_own_record(user_update: schemas.UserUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    db_user = user_service.update_user_self(db, current_user, user_update)
    return db_user


@app.get("/api/user/{user_id}", response_model=schemas.User)
def get_user_by_id(user_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_admin_user)):
    db_user = user_service.get_user(db, user_id)
    return db_user


@app.post("/api/user/register/", response_model=schemas.User)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    is_user_already_registred = user_service.get_user_by_email(db, email=user.email)
    if is_user_already_registred:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = user_service.create_user(db, user)
    return db_user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)