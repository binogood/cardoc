from typing import Union, NoReturn

from sqlalchemy import Column, Integer, Unicode, DateTime, func, Boolean

from core.db.session import Base
from core.db.timestamp_mixin import TimestampMixin
import bcrypt


class User(Base, TimestampMixin):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Integer, nullable=False, unique=True)
    password = Column(Unicode(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(
                        DateTime,
                        nullable=False,
                        default=func.utc_timestamp(),
                        onupdate=func.utc_timestamp(),
                )
    updated_at = Column(
                        DateTime,
                        nullable=False,
                        default=func.utc_timestamp(),
                        onupdate=func.utc_timestamp(),
                )

    def create(
            self,
            name: str,
            password: str,
            is_admin: bool,
    ) -> Union["User", NoReturn]:
        password = self._hashing_password(password=password)
        return User(name=name, password=password, is_admin=is_admin)

    def _hashing_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")