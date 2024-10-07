
import datetime
x = datetime.datetime.now()

def dagens_dato():
    return (x.strftime("%d-%m-%Y"))

def nåværende_tid():
    return (x.strftime("%H:%M:%S"))

def er_helg():
    helg = (x.strftime("%w"))
    if helg > 5:
        return True
    else:
        return False