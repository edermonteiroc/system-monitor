import platform
import cpuinfo
import psutil
import os
import datetime
import socket




def get_CPU_model():
    """Gets the CPU model.
    """
    cpumodel = cpuinfo.get_cpu_info()['brand_raw']
    return cpumodel

def get_CPU_frequency():
    """Gets the CPU frequency.
    """
    cpufrequency = cpuinfo.get_cpu_info()['hz_advertised_friendly']
    return cpufrequency

def get_hostname():
    """Gets the hostname of the host.
    """
    return platform.node()

def get_total_ram():
    """Gets the total ram.
    """
    try:
        ram_info = psutil.virtual_memory()
        strval = "" + f"{ram_info.total / 1024 / 1024 / 1024:.2f}"
        return strval
    except FileNotFoundError:
        return "Ram info not available on this system"

def get_used_ram():
    """Gets the used RAM.
    """
    try:
        ram_info = psutil.virtual_memory()
        strval = "" + f"{ram_info.used / 1024 / 1024 / 1024:.2f}"
        return strval
    except FileNotFoundError:
        return "Ram info not available on this system"

def get_used_ram_percentage():
    """Gets the used RAM in percentage.
    """
    try:
        ram_info = psutil.virtual_memory()
        strval = "" + f"{ram_info.percent}"
        return strval
    except FileNotFoundError:
        return "RAM info not available on this system"

def get_disk_total():
    """Gets the total size of the disk.

    Converts it to the ideal format.
    Returns the total size of the disk or an \
        information message when an error occurs.
    """
    try:
        disk_info = psutil.disk_usage("/")
        strval = "" + (f"{disk_info.total / 1024 / 1024 / 1024:.2f}")
        return  strval
    except FileNotFoundError:
        return "Disk info not available on this system"


def get_used_disk():
    """Gets the total used space of the disk.

    Converts it to the ideal format.
    Returns the total used space of the disk or\
        an error message when an error occurs.
    """
    try:
        disk_info = psutil.disk_usage("/")
        strval = "" + (f"{disk_info.used / 1024 / 1024 / 1024:.2f}")
        return strval
    except FileNotFoundError:
        return "Disk info not available on this system"

def get_used_disk_percentage():
    """Gets the total used space of the disk in percentage.

    Converts it to the ideal format.
    Returns the total used space of the disk in percentage or\
        an error message when an error occurs.
    """
    useddisk = float(get_used_disk())
    totaldisk = float(get_disk_total())
    a = (useddisk / totaldisk) * 100
    strval = "" + "%.2f" % a
    return strval

def get_user():
    """Gets the username and returns it.
    """
    return (os.getlogin())

def get_date_and_time():
    """Gets the date and time and returns it.
    """
    atual = datetime.datetime.now()
    date = atual.strftime("%d/%m/%Y, %H:%M:%S")
    strval = "" + date
    return strval

def get_ip_address():
    """Gets ip address and returns it.
    """
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    strval = "" + IPAddr
    return strval
