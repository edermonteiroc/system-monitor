import subprocess
from getoperationsystem import *
def get_motherboard_model():
    """Executes a powershell comand to get the motherboard.
    Adds to a String.

    Uses try catch to avoid untreated exceptions

    Filters the string and return it with the essential information.
    """
    try:
        querystr = "Get-WmiObject win32_baseboard | Format-List Product"
        result = subprocess.run(['powershell', querystr], shell=True, capture_output=True, check=True).stdout
        s = str(result)
        sub_string = s.split(":")[1]
        sub2_string = sub_string.split("\\")[0].strip()
        return sub2_string
    except Exception as ex:
        print ("Get motherboard exception: " + ex)
        return ""

def get_motherboard_manufacturer():
    """Executes a powershell comand to get the motherboard manufacturer.
    Adds to a String.

    Uses try catch to avoid untreated exceptions

    Filters the string and return it with the essential information.
    """
    try:
        querystr = "Get-WmiObject win32_baseboard | Format-List Manufacturer"
        result = subprocess.run(['powershell', querystr], shell=True, capture_output=True, check=True).stdout
        s = str(result)
        sub_string = s.split(":")[1]
        sub2_string = sub_string.split("\\")[0].strip()
        return sub2_string
    except Exception as ex:
        print ("Get motherboard exception: " + ex)
        return ""

def get_motherboard_info():
    """Executes the functions responsible for get motherboard \
    informations and return them.
    """
    return (get_motherboard_manufacturer() + " " + get_motherboard_model())
