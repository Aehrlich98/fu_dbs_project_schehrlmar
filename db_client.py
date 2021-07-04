#!/usr/bin/env python3


#   DB client for local database connection. 
#   To run this successfully, you'll need the psycopg2 module for python:
#   install with:   pip install psycopg2
#   you might also need the binaries:   pip install psycopg2-binaries   ;   libpq-dev   ;   or more...

#	Features no visualisation but allows connection to local Database

import psycopg2
from psycopg2 import sql


def main():
   print("Sarting up connection to PostgreSQL...\n ...To quit enter 'quit' on the next promt...\n'")
	
	
   connection = psycopg2.connect(
   host="localhost",
   database="datbas",
   user="postgres",
   password="Metze16L!"    #TODO remove Psswd before sharing!!!!!!
   )

   cursor = connection.cursor()
   
   while(True):
       statement= input("Please enter command:\n")
       if(statement == "quit" or statement == "Quit"):
          print("Quitting...") 
          break 
	   
       print("Executing statement:")
       
      try:
       cursor.execute(statement)
       db_reply = cursor.fetchall()

       print("PostgreSQL says: ...\n")
       print(db_reply)

   if(connection is not None):
      connection.close()
      print("Connection closed.\n")
   
   return