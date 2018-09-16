from datetime import timedelta

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from coding_challenge import container
from coding_challenge.api.resources.like_shop import LikeShop
from coding_challenge.api.resources.get_shop_by_distance import GetShops
from coding_challenge.api.resources.authenticate import Authenticate
from coding_challenge.modules.auth.jwt_validator import verify, identity
from coding_challenge.api.resources.get_preferred_shops import GetPreferredShops
from coding_challenge.api.resources.dislike_shop import DislikeShop
from coding_challenge.api.resources.get_user_location import GetUserLocation


def create_app():
    """
    create and configure the api instance
    :return: api
    """

    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = container.config['URL_DB']
    app.config['ENV'] = 'prod'
    app.config['JSON_AS_ASCII'] = True
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'secret'
    app.config['JWT_LEEWAY'] = timedelta(seconds=10)
    db = SQLAlchemy(app)
    db.init_app(app)

    jwt = JWT(app, verify, identity)

    resources = {
        LikeShop: '/like',
        GetShops: '/get_shops',
        GetPreferredShops: '/preferred',
        Authenticate: '/auth',
        DislikeShop: '/dislike',
        GetUserLocation: '/location'
    }

    for res, url in resources.items():
        api.add_resource(res, url)
    return app


class AppKernel:

    @staticmethod
    def start_server(debug=False):
        """
        run the application server
        :param debug: False
        """
        app = create_app()
        app.run(debug=debug)
