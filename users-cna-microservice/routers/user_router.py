from typing import List, Optional

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from db.dals.user_dal import UserDAL
from db.models.user import User
from dependencies import get_user_dal

router = APIRouter()

# Pydantic model for the response
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    mobile: int

    class Config:
        orm_mode = True

@router.post("/users")
async def create_user(name: str, email: str, mobile: str, user_dal: UserDAL = Depends(get_user_dal)):
    return await user_dal.create_user(name, email, mobile)

@router.put("/users/{user_id}")
async def update_user(user_id: int, name: Optional[str] = None, email: Optional[str] = None, mobile: Optional[str] = None,
                      user_dal: UserDAL = Depends(get_user_dal)):
    return await user_dal.update_user(user_id, name, email, mobile)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, user_dal: UserDAL = Depends(get_user_dal)):
    user = await user_dal.get_user(user_id)
    return user

@router.get("/users", response_model=List[UserResponse])
async def get_all_users(user_dal: UserDAL = Depends(get_user_dal)):
    users = await user_dal.get_all_users()
    return users
