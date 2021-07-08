#!/usr/bin/env python3


#   DB client for local database connection. 
#   To run this successfully, you'll need the psycopg2 module for python:
#   install with:   pip install psycopg2
#   you might also need the binaries:   pip install psycopg2-binaries   ;   libpq-dev   ;   or more...

#	Features no visualisation but allows connection to local Database

import psycopg2
from psycopg2 import sql

import pandas as pd
import pathlib
import sys

def main():
   print("Starting up connection to PostgreSQL...\n ...To quit enter 'quit' on the next promt...\n\nTo shopw a visualisation and comparison based on the DBs data type 'visualize'...\n")
	
   print("Enter connection data. Format:")
   conn_data = input("host database_name database_user user_password\n")
   
   conn_field = conn_data.split(" ")
   
   connection = psycopg2.connect(
   host=conn_field[0],
   database=conn_field[1],
   user=conn_field[2],
   password= conn_field[3],
   )

   cursor = connection.cursor()
   
   while(True):
      statement= input("Please enter command:\n")
      if(statement.lower() == "quit"):
          print("Quitting...") 
          break
      #BEGIN Visualize Data:      
      if(statement.lower() == "visualize"):
          print("Starting Visualization...")
          
          this_path = pathlib.Path(__file__).parent.resolve()
          print("Exporting CSVs...")
		  
          for table in ["co2", "gdp", "population", "world_happiness_index"]:
             #print(table)
             cursor.execute(
             sql.SQL("Select * from {}")
        	 .format(sql.Identifier(table))
             )
             db_reply = cursor.fetchall()
             df = pd.DataFrame(db_reply)
			 
			 #set filepath for exported CSVs
             if ("win" in sys.platform):
                target_path = r'{}\{}.csv'.format(this_path, table)	#uses '\'
             else: #assume whatever OS uses '/'
                target_path = r'{}/{}.csv'.format(this_path, table)	#uses '/'
			 #print(target_path)
             df.to_csv(target_path, index = False)
          break
	  #END Visualize Data
	  
      print("Executing statement:")
       
      cursor.execute(statement)
      db_reply = cursor.fetchall()
	  
      print("PostgreSQL says: ...\n")
      print(db_reply)
   #END while  
   
   if(connection is not None):
      connection.close()
      print("Connection closed.\n")
   
   return
   
   
if __name__ == "__main__":
	main()