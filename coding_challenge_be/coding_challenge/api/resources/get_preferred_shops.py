from flask_jwt import jwt_required
from flask import jsonify, make_response
from flask_restful import Resource, request

from coding_challenge import container
from coding_challenge.modules.schema import ShopSchema
from coding_challenge.core.session_scope import session_scope
from coding_challenge.modules.model import preferred_shops, Shop
from coding_challenge.modules.auth.jwt_manager import decode_auth_token


class GetPreferredShops(Resource):

    @jwt_required()
    def get(self):

        user_id = decode_auth_token(
            request.headers.__dict__['environ']['HTTP_AUTHORIZATION']
            .split(' ')[1]
        ).get('identity')

        with session_scope(container.config['URL_DB']) as session:
            return make_response(
                jsonify(
                    ShopSchema(many=True).dump(
                        [session.query(Shop).filter(
                            Shop.shop_id == shop_id
                        ).first() for shop_id in [
                            shop.shop_id for shop in session.query(
                                preferred_shops).filter(
                                preferred_shops.c.user_id == user_id
                            ).all()
                        ]
                        ]
                    ).data
                ),
                200
            )
