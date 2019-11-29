def init_log(path):
    """
    Ininitial logs file with path parameter.
    """
    file = open(path, 'w+')
    file.close()


def reten_log(path):
    """
    Try to truncate logs file when logs file has lines more then 200 lines.
    """
    try:
        file = open(path, 'r+')
        lines = file.readlines()
        if lines > 200:
            file.truncate()
            file.close()
        else:
            file.close()
    except:
        pass
