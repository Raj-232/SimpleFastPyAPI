from fastapi import APIRouter
from fastapi import  HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from modal.user import UserCreate, UserUpdate,GetUser
from service.user import get_users,get_usersby_id,create_users,update_users,delete_users

userrouter=APIRouter()

@userrouter.get("/users", response_model=list[GetUser])
async def read_users( db: Session = Depends(get_db)):
    try:
        return await get_users(db)
    except:
        raise HTTPException(status_code=500,detail="internal server error")
    

@userrouter.get("/users/{user_id}",response_model=GetUser)
async def get_user_by_email(user_id: int, db: Session = Depends(get_db)):
    try:
        user = await get_usersby_id(db,user_id)
        if user:
            return user
        raise HTTPException(status_code=404, detail="User not found")
    except:
        raise HTTPException(status_code=500,detail="internal server error")


@userrouter.post("/users",response_model=GetUser)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return await create_users(db,user)
    except:
        raise HTTPException(status_code=500,detail="internal server error")

@userrouter.put("/users/{user_id}")
async def update_user_by_email(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    try:
        return await update_users(db,user,user_id)
    except:
        raise HTTPException(status_code=500,detail="internal server error")


@userrouter.delete("/users/{user_id}")
async def delete_user_by_email(user_id: int, db: Session = Depends(get_db)):
    try:
        return await delete_users(db,user_id)
    except:
        raise HTTPException(status_code=500,detail="internal server error")