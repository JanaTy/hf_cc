from flask_jwt import jwt_required
from flask_restful import Resource, request

from coding_challenge import container
from coding_challenge.modules.schema import ShopSchema
from coding_challenge.core.session_scope import session_scope
from coding_challenge.modules.model import User, Shop, preferred_shops
from coding_challenge.modules.auth.jwt_manager import decode_auth_token


class GetShops(Resource):

    @jwt_required()
    def get(self):
        user_id = decode_auth_token(
            request.headers.__dict__['environ']['HTTP_AUTHORIZATION']
            .split(' ')[1]
        ).get('identity')

        with session_scope(container.config['URL_DB']) as session:
            to_exclude = session.query(preferred_shops).filter_by(
                user_id=int(user_id)
            ).all()

            final_list = [
                shop for shop in session.query(
                    Shop
                ).all() if shop.shop_id not in [i.shop_id for i in to_exclude]
            ]
            sorted_list = GetShops.sort_shops_by_distance(
                session.query(User).get(user_id),
                final_list
            )
            return ShopSchema(many=True).dump([item for item in sorted_list])

    @staticmethod
    def sort_shops_by_distance(user, shops):
        return sorted(
                shops, key=lambda x: abs(user.user_location - x.shop_location)
            )
