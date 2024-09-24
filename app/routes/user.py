from sqlalchemy import select
from .. import app
from ..db import Session, User
from ..schemas import UserData
from ..exceptions import UserAlreadyExistsException, UserNotFoundException



@app.post("/users", status_code=201)
async def create_user(data: UserData):
    """
    Create New User
    """
    try:
        async with Session.begin() as session:
            user = User(**data.model_dump())
            session.add(user)
            return {"message": "User added successfully."}
    except:
        raise UserAlreadyExistsException()


@app.get("/users")
async def all_users():
    """
    Retrieve all users
    """
    async with Session.begin() as session:
        users = await session.scalars(select(User))
        users = [UserData.model_validate(user) for user in users]
        return users


@app.delete("/users/{username}")
async def delete_user(username: str):
    """
    Delete a user by username
    """
    async with Session.begin() as session:
        user_to_delete = await session.scalar(select(User).where(User.name == username))
        if user_to_delete:
            await session.delete(user_to_delete)
            return {"message": "User deleted successfully."}
        else:
            raise UserNotFoundException()