from  schema.user import User
from fastapi import  HTTPException
async def get_users(db):
    return  db.query(User).all()
async def get_usersby_id(db,user_id):
    return  db.query(User).filter(User.id == user_id).first()
async def create_users(db,user):
    db_user =  User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
async def update_users(db,user,user_id):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    return {"message": "User updated successfully"}
async def delete_users(db,user_id):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}