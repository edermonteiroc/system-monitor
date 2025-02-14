from mysqlcon import *
def checkTableExists(dbcon, tablename):
    """Cheks if table exists
    Returns true or false
    """
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

def create_table(dbcon,tablename):
    """Creates the table for the data insertion
    """
    mycursor = dbcon.cursor()
    mycursor.execute("CREATE TABLE {0} \
                     ( id INT NOT NULL AUTO_INCREMENT ,\
                      usuario VARCHAR(104) NULL ,\
                      hostname VARCHAR(253) NOT NULL UNIQUE ,\
                      cpu_model VARCHAR(100) NULL ,\
                      cpu_frequency VARCHAR(50) NULL ,\
                      ram_total VARCHAR(50) NULL ,\
                      ram_usage VARCHAR(50) NULL ,\
                      ram_usage_porcentage VARCHAR(50) NULL ,\
                      disk_size_total VARCHAR(50) NULL ,\
                      disk_used_size VARCHAR(50) NULL ,\
                      disk_used_porcentage VARCHAR(50) NULL ,\
                      ip_address VARCHAR(50) NULL ,\
                      motherboard VARCHAR(50) NULL ,\
                      osversion VARCHAR(50) NULL ,\
                      PRIMARY KEY (id))".format(tablename))
    dbcon.commit()
    mycursor.close()

def create_tables_if_missing(dbcon, tablename):
    """Ensures the required table exists in the database."""
    if dbcon is None:
        print("❌ Database connection failed.")
        return

    if not checkTableExists(dbcon, tablename):
        print(f"Table `{tablename}` does not exist. Creating table...")
        try:
            create_table(dbcon, tablename)
            dbcon.commit()  # Ensure the changes are saved
            print(f"Table `{tablename}` created successfully.")
        except mysql.connector.Error as err:
            print(f"Error creating table `{tablename}`: {err}")
        finally:
            dbcon.close()
    else:
        print(f"Table `{tablename}` already exists.")
        dbcon.close()

