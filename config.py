class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    # MONGODB_SETTINGS = {
    #     'db': 'local',
    #     'host': 'localhost',
    #     'port': 27017
    # }
