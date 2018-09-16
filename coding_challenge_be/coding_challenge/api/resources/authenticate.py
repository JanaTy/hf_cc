from datetime import datetime, timedelta

import jwt
from flask_restful import Resource, request

from coding_challenge import container
from coding_challenge.modules.auth.jwt_validator import verify


class Authenticate(Resource):
    def __init__(self):
        pass

    def get(self):
        instance = verify(
            request.authorization['username'], request.authorization['password']
        )
        if instance is not None:
            payload = {
                'identity': instance.user_id,
                'exp': datetime.utcnow() + timedelta(
                    seconds=3600),
                'iat': 1516239022,
                'nbf': 2,
            }
            try:
                jwt_token = jwt.encode(
                    payload,
                    container.config['JWT_SECRET'],
                    container.config['JWT_ALGORITHM']
                )
                return {'token': jwt_token.decode('utf-8',)}
            except():
                return
