from fastapi import APIRouter
from db import supabase
from pydantic import BaseModel

inquires_router = APIRouter(prefix="/inquires")

class DeleteInquiry(BaseModel):
    uid: str

@inquires_router.get("/all")
def fetch_all_inquires():
    return

@inquires_router.delete("/delete_inquiry")
def delete_inquiry(request: DeleteInquiry):
    return