from jose import jwt , JWTError
from datetime import datetime , timedelta

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_access_token(data : dict):
    to_ecode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=30)

    to_ecode.update({"exp":expire})

    token = jwt.encode(
        to_ecode,
        SECRET_KEY,
        ALGORITHM
    )

    return token


def verify_token(token : dict):

    try:
        payload = jwt.decode(
            token,SECRET_KEY,algorithms=[ALGORITHM]
        )

        print("Payload:", payload)

    
        return payload
    except JWTError:
        return None



