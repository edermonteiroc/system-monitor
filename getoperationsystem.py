import platform

def get_os():
    """Gets the operation system informations
    """
    return (platform.system() + " "+ platform.version())

def get_os_filtered_version():
    """Gets the operation system informations and filter it
    """
    sofversion = int(platform.version().split('.')[0])
    return sofversion 

