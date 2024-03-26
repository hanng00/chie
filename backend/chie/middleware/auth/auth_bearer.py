import os
from typing import Optional

from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from chie.middleware.auth.jwt_token_handler import decode_access_token, verify_token
from chie.modules.user.entity.user_identity import UserIdentity
from chie.config import bypass_authentication

class AuthBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(
        self,
        request: Request,
    ):
        credentials: Optional[HTTPAuthorizationCredentials] = await super().__call__(
            request
        )
        self.check_scheme(credentials)
        token = credentials.credentials  # pyright: ignore reportPrivateUsage=none
        return await self.authenticate(
            token,
        )

    def check_scheme(self, credentials):
        if credentials and credentials.scheme != "Bearer":
            raise HTTPException(status_code=401, detail="Token must be Bearer")
        elif not credentials:
            raise HTTPException(
                status_code=403, detail="Authentication credentials missing"
            )

    async def authenticate(
        self,
        token: str,
    ) -> UserIdentity:
        if bypass_authentication():
            return self.get_test_user()
        elif verify_token(token):
            return decode_access_token(token)
        else:
            raise HTTPException(status_code=401, detail="Invalid token or api key.")

    def get_test_user(self) -> UserIdentity:
        return UserIdentity(
            email="test@example.com", id="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"  # type: ignore
        )  # replace with test user information


def get_current_user(user: UserIdentity = Depends(AuthBearer())) -> UserIdentity:
    return user
