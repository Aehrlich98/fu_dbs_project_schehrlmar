#!/usr/bin/env python3


#   DB client by Aaron and Pirin:
#   To run this successfully, you'll need the psycopg2 module for python:
#   install with:   pip install psycopg2
#   you might also need the binaries:   pip install psycopg2-binaries   ;   libpq-dev   ;   or more...

import sys
import psycopg2
from psycopg2 import sql


def connect():
    #allow user to enter a single string containing all login data separated by spaces TODO allow save to file for auto login.
    connect_data=None
    connect_data=input("Enter Database Data to connect to:\n-- Format for input --\n-- host database_name user password\n")
    if(connect_data.casefold() == "quit"):
        end_it(None)#QUIT

    conArray=connect_data.split(' ')

    connection=psycopg2.connect(
    host=conArray[0],
    database=conArray[1],
    user=conArray[2],
    password=conArray[3]
    )
    return connection

def end_it(connection=None):
   if(connection is not None):
      connection.close()
      print("Connection closed.\n")
   print("Quitting...")
   sys.exit()


def main():
   print("Starting up connection to PostgreSQL...\n ...To quit enter 'quit'\n'")

   #Connect to DB via psycopg2
   connection = connect()


   cursor = connection.cursor()

   while(True):
      #wait for user input
      statement= input("Please enter command:\n")
      if(statement.casefold() == "quit"):
          print("Quitting...")
          break
      if(statement.casefold() == "select version;"):
          cursor.execute("select version;")
      #handle input to make it usable for the DB
      #Query DB
      print("Executing statement:")
      cursor.execute(statement)    #query)
      db_reply = cursor.fetchall()     #retrieve all data
      #manipulate reply: simply reverse the string reply, because why not ;)
      db_reply = db_reply[::-1]

      print("PostgreSQL says: ...\n")
      print(db_reply)

   #END while


if __name__ == "__main__":
    main()
