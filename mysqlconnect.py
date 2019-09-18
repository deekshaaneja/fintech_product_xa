import sqlalchemy as db
from Config import conf
from BaseError import ConnectionError
engine = None

def get_engine():
    global engine
    if engine is None:
        try:
            init_connection()
        except Exception as e:
            raise e
    return engine

def init_connection():
    global engine
    database = conf['database']
    if engine is None:
        try:
            engine = db.create_engine('mysql+pymysql://root:admin1234@mysql:3306/')
            engine.connect()
            existing_databases = engine.execute("SHOW DATABASES;")
            existing_databases = [d[0] for d in existing_databases]
            if database not in existing_databases:
                engine.execute("CREATE DATABASE {0}".format(database))
            engine = db.create_engine('mysql+pymysql://root:admin1234@mysql:3306/'+database)
            engine.connect()

        except Exception as e:
            raise ConnectionError("Failed to connect to mysql")


