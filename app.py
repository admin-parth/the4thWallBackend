from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users import user_router
from contactus import contact_router
from inquires import inquires_router

origins = [
    "https://the4th-wall-admin.vercel.app"
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="http://localhost.*",
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(user_router, prefix="/api", tags=['Users'])
app.include_router(contact_router, prefix="/api", tags=['Messages'])
app.include_router(inquires_router, prefix="/api", tags=['Inquiries'])
