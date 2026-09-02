from fastapi import HTTPException, status
from config.database import supabase
from schemas.auth import SignupRequest, LoginRequest

def check_user_exists(email:str) -> bool:
    existing_user = supabase.table("profiles").select("id").eq("email", email).execute()
    return bool(existing_user.data)

def create_user(payload: SignupRequest):
    user_exists = check_user_exists(payload.email)
    if user_exists:
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    auth_response = supabase.auth.sign_up({
        "email": payload.email,
        "password": payload.password
    })

    user_id = auth_response.user.id

    #create matching profile for the user

    forge_id = payload.name.lower().replace(" ", "_")  # Generate forge_id by replacing spaces with underscores and converting to lowercase

    supabase.table("profiles").insert({
        "id": user_id,
        "name": payload.name,
        "role": payload.role,
        "forge_id": forge_id
    }).execute()

    return {"message": "User created successfully", "user_id": user_id}

def login_user(payload: LoginRequest):
    try:
        auth_response = supabase.auth.sign_in_with_password({
            "email": payload.email,
            "password": payload.password
        })
   
        if auth_response.user is None:
            raise HTTPException(status_code=401, detail="Invalid email or password.")

        return {"user_id": auth_response.user.id,
            "access_token": auth_response.session.access_token,
            "refresh_token": auth_response.session.refresh_token
            }


    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


