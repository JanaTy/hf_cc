from flask_jwt import jwt
from coding_challenge import container


def decode_auth_token(auth_token):
    return jwt.decode(
        auth_token,
        key=container.config['JWT_SECRET'],
        algorithms=container.config['JWT_ALGORITHM']
    )
