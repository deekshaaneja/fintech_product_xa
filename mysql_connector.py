import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser
import os

def get_db_params():
    db_params_parser = ConfigParser()
    db_params_file = (os.path.join(os.getcwd(),'config','mysql_config.ini'))
    db_params_parser.read(db_params_file)
    host = db_params_parser.get('mysql_db', 'host')
    database = db_params_parser.get('mysql_db', 'database')
    user = db_params_parser.get('mysql_db', 'user')
    password = db_params_parser.get('mysql_db', 'password')
    return host,database,user,password

def get_table_name():
    db_params_parser = ConfigParser()
    db_params_file = (os.path.join(os.getcwd(),'config','mysql_config.ini'))
    db_params_parser.read(db_params_file)
    table_name = db_params_parser.get('mysql_db', 'table_name')
    return table_name

def commit_query(query):
    host,database,user,password = get_db_params()
    mySQLconnection = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = mySQLconnection.cursor()
    cursor.execute(query)
    mySQLconnection.commit()
    cursor.close()
    return 'done'

def fetch_query(query):
    host,database,user,password = get_db_params()
    mySQLconnection = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = mySQLconnection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    return records
