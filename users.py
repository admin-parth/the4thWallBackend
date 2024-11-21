from fastapi import APIRouter
from db import supabase
from pydantic import BaseModel
from typing import Optional

user_router = APIRouter(prefix="/users")

class DeleteUser(BaseModel):
    uid: str

class UpdateUser(DeleteUser):
    name: str
    role: str
    email: str

    def to_json(self):
        return {
            'id': self.uid,
            'name': self.name,
            'role': self.role,
            'email': self.email,
        }

class AddUser(UpdateUser):
    uid: Optional[str] = None
    password: str

@user_router.get('/all')
async def get_users():
    response = supabase.table('users').select('*').execute()
    return response.data

@user_router.post('/update')
async def update_user(request: UpdateUser):
    response = supabase.table('users').update(request.to_json(), count='exact').eq('id', request.uid).execute()
    return response

@user_router.delete('/delete')
async def delete_user(request: DeleteUser): 
    response = supabase.table('users').delete(count="exact").eq('id', request.uid).execute()
    return response

@user_router.post('/add')
async def add_user(request: AddUser): 
    # add user to supabase auth to create a user and then populate id in request with UUID
    user = supabase.auth.sign_up({"email": request.email, "password": request.password})
    request.uid = user.user.id
    response = supabase.table('users').insert(request.to_json(), count='exact').execute()
    return response
