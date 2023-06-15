import jwt
import json
import hashlib
from datetime import datetime, timedelta
from core.database.dto import DbDtoUser
from core.utils.settings import settings

def sign_json_web_token(db_dto_user: DbDtoUser) -> str:
    hash_string = hash_db_dto_user(db_dto_user=db_dto_user)
    payload = {
        "user_id": db_dto_user.id,
        "hash": hash_string,
        "iat": datetime.utcnow(),  # Issued at time
        "exp": datetime.utcnow() + timedelta(days=1)  # Expiration time
    }
    token = jwt.encode(payload, settings.jwt_signature, algorithm="HS256")
    return token

def verify_json_web_token(access_token: str):
    decoded = jwt.decode(jwt=access_token, key=settings.jwt_signature, algorithms=["HS256"])
    return decoded

def hash_db_dto_user(db_dto_user: DbDtoUser):
    filtered_data = {
        "id": db_dto_user.id,
        "email": db_dto_user.email,
        "hash": db_dto_user.password_hash
    }
    jsonString = json.dumps(filtered_data, sort_keys=True)
    hash_string = hashlib.md5(jsonString.encode()).hexdigest()
    return hash_string
