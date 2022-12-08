from fastapi import APIRouter

userapi = APIRouter()

@userapi.get("/index")
async def index_page():
    return "This is USERAPI URL page!"