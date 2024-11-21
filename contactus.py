from fastapi import APIRouter
from db import supabase
from pydantic import BaseModel

contact_router = APIRouter(prefix="/messages")

class DeleteMessage(BaseModel):
    uid: str

@contact_router.get("/all")
def fetch_all_messages():
    return

@contact_router.delete("/delete_message")
def delete_message(request: DeleteMessage):
    return