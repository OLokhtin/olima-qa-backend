from fastapi import APIRouter, HTTPException, status, Response
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.models.auth import UserModel
from src.schemas.auth import UserScheme, AuthScheme
from src.security import security, config
from src.repository.auth import verify_password, hash_password

router = APIRouter()

@router.post("/api/register",
             tags=["auth-controller"],
             summary="register_user"
             )
async def register_user(
        data: UserScheme,
        session: SessionDep
):
    new_user = UserModel(
        user_email = data.user_email,
        user_password = hash_password(data.user_password),
        user_phone=data.user_phone,
        user_name = data.user_name,
        user_surname = data.user_surname,
        user_birthday = data.user_birthday
    )
    session.add(new_user)
    await session.commit()
    return {"message": "Successfully registered"}

@router.post("/api/login",
             tags=["auth-controller"],
             summary="login_user"
             )
async def login_user(
        creds: AuthScheme,
        session: SessionDep,
        response: Response
):
    query = (select(UserModel)
             .filter(UserModel.user_email == creds.user_email)
             )
    result = await session.execute(query)
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect credentials"
                            )
    else:
        if verify_password(creds.user_password, user.user_password):
            token = security.create_access_token(uid=str(user.user_id))
            response.set_cookie(key=config.JWT_ACCESS_COOKIE_NAME,
                                value=token
                                )
            return {"message": "Successfully logged in"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Incorrect credentials"
                                )

@router.post("/api/logout",
             tags=["auth-controller"],
             summary="logout_user"
             )
async def logout_user(response: Response):
    response.delete_cookie(key=config.JWT_ACCESS_COOKIE_NAME)
    return {"message": "Successfully logged out"}