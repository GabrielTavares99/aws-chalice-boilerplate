import json

from sqlalchemy import create_engine, pool
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from chalicelib.config.settings import (ENV, PROD, DATABASE)


class ConferenceDatabaseConnection:
    ENGINE = None

    @staticmethod
    def engine(default_database=None):
        if default_database is None:
            default_database = DATABASE['db']

        string_conn = "mysql+pymysql://{}:{}@{}:{}/{}".format(
            DATABASE['user'],
            DATABASE['password'],
            DATABASE['host'],
            DATABASE['port'],
            default_database
        )

        engine = create_engine(
            string_conn,
            echo=False,
            poolclass=pool.StaticPool
        )
        if ENV != PROD:
            engine.echo = True
        return engine

    @staticmethod
    def get_engine():
        if ConferenceDatabaseConnection.ENGINE is None:
            ConferenceDatabaseConnection.ENGINE = ConferenceDatabaseConnection.engine()
        return ConferenceDatabaseConnection.ENGINE

    @staticmethod
    def get_session(session=None):
        try:
            if session is not None:
                return session
            engine = ConferenceDatabaseConnection.get_engine()
            db_session = sessionmaker(bind=engine)
            db_session = db_session()
            return db_session
        except Exception as e:
            print('ERROR TO GET SESSION:: {}'.format(e))
            raise e

    @staticmethod
    def close_session(session, close_session=True):
        try:
            if close_session:
                print('CLOSING SESSION::')
                session.close()
        except Exception as e:
            print('ERROR TO CLOSE SESSION:: {}'.format(e))
            raise e

    @staticmethod
    def alchemy_entity_to_dict(alchemy_entity):
        if isinstance(alchemy_entity.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(alchemy_entity) if not x.startswith('_') and x != 'metadata']:
                data = alchemy_entity.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
