from flask_restful import Resource, reqparse

from coding_challenge import container
from coding_challenge.modules.model import User, Shop
from coding_challenge.core.session_scope import session_scope
from coding_challenge.modules.auth.jwt_manager import decode_auth_token


class GetUserLocation(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('jwt')
        args = parser.parse_args()
        if args['jwt'] is not None:
            try:
                user_id = decode_auth_token(args['jwt']).get('identity')
            except ():
                return {'msg': 'error'}
        with session_scope(container.config['URL_DB']) as session:
            user_location = session.query(User).get(user_id).user_location
            return {'user': user_location}
