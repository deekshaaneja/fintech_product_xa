from sqlalchemy import MetaData, INTEGER, Table, Column, text, VARCHAR, FLOAT, desc
import mysqlconnect
from Config import conf
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
Session = None
class Transaction(Base):
    __tablename__ = conf['table']
    id = Column('id', INTEGER, primary_key=True, autoincrement=True)
    currency = Column('currency', VARCHAR(100), nullable=False)
    amount = Column('amount', FLOAT, nullable=False)
    currency_rate = Column('currency_rate', FLOAT, nullable=False)
    amount_in_usd = Column('amount_in_usd', FLOAT, nullable=False)


def insert_transaction(transaction = None):
    global Session
    session = Session()
    row = Transaction(currency=transaction.currency, amount=transaction.amount, currency_rate=transaction.currency_rate, amount_in_usd=transaction.amount_in_usd)
    session.add(row)
    session.commit()

def query_database(currency, NumberOfRows):
    global Session
    session = Session()
    if currency is None:
        row = session.query(Transaction).order_by(desc(Transaction.id)).limit(NumberOfRows)
    elif currency is not None:
        row = session.query(Transaction).filter(Transaction.currency == currency).order_by(desc(Transaction.id)).limit(NumberOfRows)
    rows = row.all()
    session.commit()
    return rows

try:
    engine = mysqlconnect.get_engine()
    Session = sessionmaker()
    Session.configure(bind=engine)
    table = conf['table']
    if not engine.dialect.has_table(engine, table):
        Base.metadata.create_all(bind=engine)

    # insert_transaction()
    # query_database()

except Exception as e:
    raise e



