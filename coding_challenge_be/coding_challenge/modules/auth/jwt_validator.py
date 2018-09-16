from coding_challenge import container
from coding_challenge.core.session_scope import session_scope
from coding_challenge.modules.model import User


def verify(username, password):
    with session_scope(container.config['URL_DB']) as session:
        user_data = session.query(User).filter(User.username == username).first()
        if user_data.password == password:
            session.expunge(user_data)
            return user_data


def identity(payload):
    return {'user_id': payload['identity']}
