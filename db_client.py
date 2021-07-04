#!/usr/bin/env python3


#   DB client
#   To run this successfully, you'll need the psycopg2 module for python:
#   install with:   pip install psycopg2
#   you might also need the binaries:   pip install psycopg2-binaries   ;   libpq-dev   ;   or more...

import sys
import psycopg2
from psycopg2 import sql
import json


def main():
	
	connection=psycopg2.connect(
	host="localhost",
	database="datbas",
	user="postgres",
	password="Metze16L"
	)
	
	cursor = connection.cursor()
	
	
	tables = sys.argv[1]
	data = sys.argv[2]
	
	query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(dec_dat["table"]))
		
	
	
	cursor.execute(query)
	
	db_reply = cursor.fetchall()#retrieve all data
	
	if(connection is not None):
		connection.close()
	#print(db_reply)
	#return db_reply
	
	return json.dumps(params)

if __name__ == "__main__":
    main()
