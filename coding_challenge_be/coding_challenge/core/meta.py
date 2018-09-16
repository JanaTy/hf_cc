from sqlalchemy import MetaData, create_engine
from coding_challenge import container

meta = MetaData(bind=create_engine(container.config['URL_DB']))
