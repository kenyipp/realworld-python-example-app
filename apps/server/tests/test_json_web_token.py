from server.utils.json_web_token import sign_json_web_token, verify_json_web_token
from uuid import uuid4
from core.database.dto import DbDtoUser
from faker import Faker
from datetime import datetime

faker = Faker()

def test_sign_json_web_token():
    db_dto_user = DbDtoUser(
        id=str(uuid4()),
        email=faker.email(),
        username=faker.user_name(),
        password_hash=str(uuid4()),
        bio=None,
        image=None,
        record_status="normal",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    access_token = sign_json_web_token(db_dto_user=db_dto_user)
    assert type(access_token) == str

def test_verify_json_web_token():
    db_dto_user = DbDtoUser(
        id=str(uuid4()),
        email=faker.email(),
        username=faker.user_name(),
        password_hash=str(uuid4()),
        bio=None,
        image=None,
        record_status="normal",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    access_token = sign_json_web_token(db_dto_user=db_dto_user)
    assert type(access_token) == str

    decoded = verify_json_web_token(access_token)
    assert decoded.get("hash") is not None
    assert decoded.get("non_exist") is None
    assert decoded.get("iat") is not None
    assert decoded.get("exp") is not None
