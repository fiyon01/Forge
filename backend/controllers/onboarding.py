
from fastapi import HTTPException
from schemas.auth import SignupRequest
from config.database import supabase



def onboard_user(payload):
    # Check if user with the given email already exists
    existing_user = supabase.table("profiles").select("id").eq("email", payload.email).execute()

    if existing_user.data:
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    # Create a new user in Supabase Auth
    auth_response = supabase.auth.sign_up({
        "email": payload.email,
        "password": payload.password
    })

    user_id = auth_response.user.id

    # Create a matching profile for the user
    forge_id = payload.name.lower().replace(" ", "_")  # Generate forge_id by replacing spaces with underscores and converting to lowercase

    supabase.table("profiles").insert({
        "id": user_id,
        "name": payload.name,
        "role": payload.role,
        "forge_id": forge_id
    }).execute()

    return {"message": "User onboarded successfully", "user_id": user_id}