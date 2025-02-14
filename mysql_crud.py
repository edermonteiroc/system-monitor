from mysqlcon import *
from getsystem import *
from getmotherboard import *
import sys

def insert_data(dbcon, val,tablename):
        """Establishes a new connection to the database

        Inserts into the database table
        """
        mycursor = dbcon.cursor()
        sql = "INSERT INTO {0} \
        (usuario , hostname , cpu_model , cpu_frequency , ram_total ,\
              ram_usage , ram_usage_porcentage , disk_size_total , disk_used_size , disk_used_porcentage ,\
                  ip_address , motherboard, osversion) \
            VALUES \
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(tablename)
        try:
            mycursor.execute(sql, val)
            dbcon.commit()
            print(mycursor.rowcount, "record inserted.")
            dbcon.close()
        except Exception as ex:
             print(f"❌ Error inserting records: {ex}")


def select_data(dbcon, table):
    """Selects all data from the table and prints a list of it.
    """
    mycursor = dbcon.cursor()
    mycursor.execute("SELECT * FROM {0} where hostname = '{1}'".format(table, get_hostname()))
    myresult = mycursor.fetchall()
    for x in myresult:
        print (x)

def verify_value_exists(dbcon, table, hostname):
    """Selects all data from the table and prints a list of it.
    """
    mycursor = dbcon.cursor()
    mycursor.execute("SELECT * FROM {0} where hostname = '{1}'".format(table,hostname))
    myresult = mycursor.fetchall()
    for x in myresult:
        print (x)

def select_all_data(dbcon, tablename):
    """Fetch all system records from the database."""
    try:
        mycursor = dbcon.cursor(dictionary=True)
        mycursor.execute(f"SELECT * FROM {tablename}")
        results = mycursor.fetchall()
        return results
    except Exception as ex:
        print(f"❌ Error fetching system records: {ex}")
        return []


