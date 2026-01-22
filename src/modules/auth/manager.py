import uuid
from fastapi import HTTPException
from src.store import users
from src.modules.auth.schema import UserCreate, UserRead


class AuthManager:
    def create_user(self, user_data: UserCreate) -> UserRead:
        for user in users.values():
            if user["name"] == user_data.name:
                raise HTTPException(status_code=400, detail="User with this name already exists")

        new_id = str(uuid.uuid4())
        new_user = UserRead(id=new_id, **user_data.dict())
        users[new_id] = new_user.dict()
        return new_user
