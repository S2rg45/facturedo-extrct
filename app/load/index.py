from app.connection.db import connection
from dotenv import dotenv_values



def load_data(data):
		config = dotenv_values(".env") 
		dictionary_config = dict(config)
		name_table = dictionary_config["NAME_TABLE"]
		name_schema = dictionary_config["NAME_SCHEMA"]
		engine = connection()
		dataframe_sql = data.to_sql(f'{name_table}', engine[1], if_exists='replace', index=False, schema="facturedo")
		connection_postgres = connection()      
		connection_postgres[0].autocommit = True
		cursor = connection_postgres[0].cursor()
		sql1 = 'select count(*) from {}.{};'.format(name_schema, name_table)
		cursor.execute(sql1)
		for i in cursor.fetchall():
				print(i)
		# connection_postgres[0].commit()
		connection_postgres[0].close()
		return {"messagees": "count "+str(i[0])}
