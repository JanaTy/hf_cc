from sqlalchemy import Table, Column, Integer, String, ForeignKey
from coding_challenge.core.meta import meta

tables = list()

user = Table(
    'user',
    meta,
    Column('user_id', Integer, primary_key=True),
    Column('username', String(20), nullable=False),
    Column('password', String(20), nullable=False),
    Column('first_name', String(20)),
    Column('last_name', String(20)),
    Column('user_location', Integer, nullable=False)
)
tables.append(user)

shop = Table(
    'shop',
    meta,
    Column('shop_id', Integer, primary_key=True),
    Column('shop_name', String(20)),
    Column('shop_location', Integer, nullable=False),
    Column('description', String, nullable=True)
)
tables.append(shop)

preferred_shops = Table(
    'preferred_shops',
    meta,
    Column('user_id', Integer, ForeignKey('user.user_id'), primary_key=True),
    Column('shop_id', Integer, ForeignKey('shop.shop_id'), primary_key=True)
)
tables.append(preferred_shops)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    for table in tables:
        table.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    for table in tables:
        table.drop()
