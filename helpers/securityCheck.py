from typing import Dict

from passlib.context import CryptContext
from dataclasses import dataclass
from logic_layer.backend import authenticateUser


@dataclass
class UserInfoVerification:
    username: str
    password: str
    password_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_password_hash(self):
        return self.password_context.hash(self.password)

    async def authenticate(self):
        user_verification: str | None = await authenticateUser(self.username)
        if user_verification:
            if self.verify_password(self.password, user_verification):
                return True
        return False

    def verify_password(self, plain_password, hashed_password):
        return self.password_context.verify(plain_password, hashed_password)
