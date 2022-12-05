import os

import yaml
from dotenv import dotenv_values
from pymongo import MongoClient

dbConf = {
    **dotenv_values('.env'),
    **dotenv_values('.env.devs'),
    **os.environ,
}


def get_db():
    mongoURI = 'mongodb://{username}:{password}@{host}:{port}/'.format(
        username=dbConf['MONGODB_USERNAME'],
        password=dbConf['MONGODB_PASSWORD'],
        host=dbConf['MONGODB_HOST'],
        port=dbConf['MONGODB_PORT'],
    )
    client = MongoClient(mongoURI)
    return client[dbConf['MONGODB_DB']]


if __name__ == "__main__":
    db = get_db()
