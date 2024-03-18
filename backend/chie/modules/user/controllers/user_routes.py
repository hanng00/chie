from fastapi import APIRouter, Depends, HTTPException, Request
from chie.logger import get_logger
from chie.middleware.auth.auth_bearer import AuthBearer, get_current_user
from chie.modules.user.dto.inputs import SignInInput, SignUpInput
from chie.modules.user.entity import UserIdentity
from chie.settings.supabase import supabase_client

logger = get_logger(__name__)

user_router = APIRouter()


@user_router.post("/signup")
async def sign_up(sign_up_data: SignUpInput):
    current_user = supabase_client.auth.get_user()
    if current_user:
        # User already exists. Return appropriate error message saying email in use.
        raise HTTPException(status_code=400, detail="Email already in use")

    try:
        res = supabase_client.auth.sign_up(
            {"email": sign_up_data.email, "password": sign_up_data.password}
        )
    except Exception as e:
        logger.error(f"Error signing up user: {e}")
        raise HTTPException(status_code=500, detail="Error signing up user")
    return res


@user_router.post("/signin")
async def sign_in(sign_in_data: SignInInput):
    try:
        res = supabase_client.auth.sign_in_with_password(
            {"email": sign_in_data.email, "password": sign_in_data.password}
        )
    except Exception as e:
        if "Invalid login" in str(e):
            raise HTTPException(status_code=401, detail="Invalid login credentials")
        raise HTTPException(status_code=500, detail="Error signing in user")
    return res


@user_router.post("/signout")
async def sign_out():
    try:
        res = supabase_client.auth.sign_out()
    except Exception as e:
        logger.error(f"Error signing out user: {e}")
        raise HTTPException(status_code=500, detail="Error signing out user")
    return res


@user_router.get("/me", dependencies=[Depends(AuthBearer())])
async def me(request: Request, current_user: UserIdentity = Depends(get_current_user)) -> UserIdentity:
    if current_user is None:
        raise HTTPException(status_code=401, detail="User not authenticated")
    return current_user
