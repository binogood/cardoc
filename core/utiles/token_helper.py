from datetime import datetime, timedelta

import jwt

from core.config import config


class TokenHelper:
    @staticmethod
    def create_token(payload: dict, expire_period: int = 3600) -> str:
        token = jwt.encode(
            payload={
                **payload,
                "exp": datetime.utcnow() + timedelta(seconds=expire_period),
            },
            key=config.JWT_SECRET_KEY,
            algorithm=config.JWT_ALGORITHM,
        )
        return token