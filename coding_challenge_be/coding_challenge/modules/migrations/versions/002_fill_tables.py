from sqlalchemy import Table, MetaData

meta = MetaData()

users = [
    {
        'username': 'janatii',
        'password': 'password',
        'first_name': 'Med',
        'last_name': 'Janati Idrissi',
        'user_location': 5
     },
    {
        'username': 'user',
        'password': 'hidden',
        'first_name': 'fname',
        'last_name': 'lname',
        'user_location': 3
    }
]

shops = [
    {
        'shop_name': 'that_shop',
        'shop_location': 7,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'this_shop',
        'shop_location': 9,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'a_shop',
        'shop_location': 15,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'le_shop',
        'shop_location': 3,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'far_shop',
        'shop_location': 19,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'near_shop',
        'shop_location': 1,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'shop_shop',
        'shop_location': 20,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'shopy',
        'shop_location': 20,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'shopashop',
        'shop_location': 22,
        'description': 'lorem ipsum'
    },
    {
        'shop_name': 'shopishops',
        'shop_location': 12,
        'description': 'lorem ipsum'
    },
]


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    migrate_engine.connect().execute(
        Table('user', meta, autoload=True).insert().values(users)
    )
    migrate_engine.connect().execute(
        Table('shop', meta, autoload=True).insert().values(shops)
    )


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    migrate_engine.connect().execute(
        Table('user', meta, autoload=True).delete()
    )
    migrate_engine.connect().execute(
        Table('shops', meta, autoload=True).delete()
    )
