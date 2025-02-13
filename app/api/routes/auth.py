from fastapi import APIRouter, HTTPException, status

from app.core.security import create_access_token, hash_password, verify_password
from app.db.database import users_collection
from app.models.user import User
from app.schemas.user import TokenData, UserCreate

auth_router = APIRouter()


@auth_router.post("/register", response_model=TokenData)
async def register(user_data: UserCreate):
    existing_user = await users_collection.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",  # noqa
        )

    hashed_password = hash_password(user_data.password)
    new_user = User(email=user_data.email, hashed_password=hashed_password)
    await users_collection.insert_one(new_user.dict())

    access_token = create_access_token(data={"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post("/login", response_model=TokenData)
async def login(user_data: UserCreate):
    user = await users_collection.find_one({"email": user_data.email})
    if not user or not verify_password(
        user_data.password, user["hashed_password"]
    ):  # noqa
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password",  # noqa
        )

    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
