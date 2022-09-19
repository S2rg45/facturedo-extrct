import os
from dotenv import dotenv_values
from sqlalchemy import create_engine


def connection():
  config = dotenv_values(".env") 
  dictionary_config = dict(config)
  host = dictionary_config["PG_HOST_"]
  port = dictionary_config["PG_PORT_"]
  user = dictionary_config["PG_USERNAME_"]
  password = dictionary_config["PG_PASSWORD_"]
  db = dictionary_config["PG_DB_"]
  conn_string = 'postgresql://{}:{}@{}:{}/{}'.format(user, password,host,port,db)
  db = create_engine(conn_string)
  conn = db.connect()
  return ["connection", conn]