from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.Int()
    username = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    user_location = fields.Int()


class ShopSchema(Schema):
    shop_id = fields.Int()
    shop_name = fields.String()
    shop_location = fields.Int()
    description = fields.String()
