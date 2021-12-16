from typing import Optional, Tuple

import jwt
from starlette.authentication import AuthenticationBackend
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware
)
from starlette.requests import HTTPConnection

from core.config import config
from ..schemas.current_user import CurrentUser


class AuthBackend(AuthenticationBackend):
    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[bool, Optional[CurrentUser]]:
        current_user = CurrentUser()
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user

        try:
            payload = jwt.decode(
                authorization, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM],
            )
            user_id = payload.get("user")
        except jwt.exceptions.PyJWTError:
            return False, current_user

        current_user.id = user_id
        return True, current_user


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass