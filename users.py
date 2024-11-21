from fastapi import APIRouter
from db import supabase

user_router = APIRouter(prefix="/users")

@user_router.get('/all')
async def get_users():
    response = supabase.table('users').select('*').execute()
    return response.data