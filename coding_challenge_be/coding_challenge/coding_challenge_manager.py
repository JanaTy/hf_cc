import os

class AbstractConfigManager:

    def __init__(self):
        self.config = {}

    def __getitem__(self, item):
        return self.config[item]

    def __setitem__(self, key, value):
        self.config[key] = value

    def __contains__(self, item):
        return item in self.config


class ConfigManager(AbstractConfigManager):

    def __init__(self):
        DB_DIR = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'coding_challenge.db'
        )
        super().__init__()
        self.config = {
            "URL_DB":

                'sqlite:///' + DB_DIR,
            'JWT_SECRET': 'secret',
            'JWT_ALGORITHM': 'HS256'

        }


class DebugConfig(AbstractConfigManager):

    def __init__(self):
        super().__init__()

        self.config = {
            "URL_DB":
                'postgresql://postgres:123456@localhost:5433/coding_challenge',
        }


class TestConfig(AbstractConfigManager):

    def __init__(self):
        super().__init__()

        self.config = {
            "URL_DB":
                'postgresql://postgres:123456@localhost:5433/coding_challenge',
        }
