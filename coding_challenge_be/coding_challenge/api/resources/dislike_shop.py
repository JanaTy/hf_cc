from flask_restful import Resource, reqparse

from coding_challenge.core.session_scope import session_scope
from coding_challenge import container
from coding_challenge.modules.model import preferred_shops
from coding_challenge.modules.auth.jwt_manager import decode_auth_token


class DislikeShop(Resource):

    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('shop_id')
        parser.add_argument('jwt')
        args = parser.parse_args()
        if args['jwt'] is not None:
            try:
                user_id = decode_auth_token(args['jwt']).get('identity')
            except ():
                return {'msg': 'error'}

            with session_scope(container.config['URL_DB']):
                try:
                    preferred_shops.delete(
                        preferred_shops.c.shop_id == args['shop_id'] and
                        preferred_shops.c.user_id == user_id
                    ).execute()
                    return {'msg': 'deleted'}
                except ():
                    return {'msg': 'error'}
