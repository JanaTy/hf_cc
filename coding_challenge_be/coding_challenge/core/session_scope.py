from contextlib import contextmanager
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


@contextmanager
def session_scope(conn_str, autoflash_state=True):
    session = Session(bind=create_engine(conn_str), autoflush=autoflash_state)
    try:
        yield session
        session.commit()
    except ():
        session.rollback()
        raise
    finally:
        session.close()
