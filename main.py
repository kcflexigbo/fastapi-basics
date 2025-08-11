from fastapi import FastAPI
from fastapi.middleware import cors
from api import user, book

app = FastAPI(
    title="Database Setup",
    description="Fast API for Database Setup",
    version="0.1.0",
)

allow_origins = ["*"]

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.user_api, tags=["user"], prefix="/user")
app.include_router(book.router, tags=["book"], prefix="/book")

app.get(
    "/root",
    tags=["root"],
    summary="Root endpoint",
    description="Root endpoint",
)
def root():
    return {"message": "Hello World"}