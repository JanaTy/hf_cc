from sqlalchemy import Table, Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from coding_challenge.core.meta import meta


db = SQLAlchemy(metadata=meta)


class Shop(db.Model):
    shop_id = Column('shop_id', Integer, primary_key=True)
    shop_name = Column('shop_name', String, nullable=False)
    shop_location = Column('shop_location', Integer)
    description = Column('description', String)


preferred_shops = Table(
    'preferred_shops', meta,
    Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True,),
    Column('shop_id', Integer, ForeignKey('shop.shop_id'), primary_key=True,),
)


class User(db.Model):
    user_id = Column('user_id', Integer, primary_key=True)
    username = Column('username', String, nullable=False)
    password = Column('password', String, nullable=False)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    user_location = Column('user_location', Integer)
    shops = relationship('Shop', secondary=preferred_shops)

