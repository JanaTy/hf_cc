class AuthException(Exception):
    pass


class AuthException(Exception):
    """Base Exception in PxG Auth"""
    pass


class NoAuthorizationError(AuthException):
    status_code = 403

    def __init__(self, msg):
        AuthException.__init__(self)
        self.message = msg

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv


class InvalidHeaderError(AuthException):
    status_code = 403

    def __init__(self, msg):
        AuthException.__init__(self)
        self.message = msg

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv


class InvalidTokenError(AuthException):
    status_code = 403

    def __init__(self, msg):
        AuthException.__init__(self)
        self.message = msg

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv
