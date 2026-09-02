from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.database import supabase
from schemas.auth import SignupRequest
from routes.auth import router as auth_router
app = FastAPI(title="Forge API", version="1.0.0", description="API for Forge application")

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_root():
    return{ "message":"welcome home"}

@app.get("/test_db_connection")
def test_db_connection():
    return {"message": "Database connection successful", "connection": True, "type": str(type(supabase))}

