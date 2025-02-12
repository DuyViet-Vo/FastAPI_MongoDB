from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, TokenData
from app.models.user import User
from app.db.database import users_collection
from app.core.security import hash_password, verify_password, create_access_token
from datetime import timedelta

auth_router = APIRouter()

@auth_router.post("/register", response_model=TokenData)
async def register(user_data: UserCreate):
    existing_user = await users_collection.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user_data.password)
    new_user = User(email=user_data.email, hashed_password=hashed_password)
    await users_collection.insert_one(new_user.dict())

    access_token = create_access_token(data={"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post("/login", response_model=TokenData)
async def login(user_data: UserCreate):
    user = await users_collection.find_one({"email": user_data.email})
    if not user or not verify_password(user_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
