import sys
from getsystem import *
from mysqlcon import *
from mysql_crud import *
from getoperationsystem import *
from mysqloperations import *
tablename = ""
# ---------------------------------------------
def main(args):
    tablename = args[0]+ "_devices"
    create_tables_if_missing(connect_db(), tablename)
    val = (get_user(), get_hostname(), get_CPU_model(), get_CPU_frequency(), get_total_ram(),\
        get_used_ram(), get_used_ram_percentage(), get_disk_total(), get_used_disk() , get_used_disk_percentage(),\
        get_ip_address(), get_motherboard_info(), get_os())
    insert_data(connect_db(), val,tablename)
    select_data(connect_db(), tablename)

# ---------------------------------------------    

# ---------------------------------------------    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))