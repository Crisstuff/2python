
import datetime
x = datetime.datetime.now()

def dagens_dato():
    return (x.strftime("%d-%m-%Y"))

def nåværende_tid():
    return (x.strftime("%H:%M:%S"))

def er_helg():
    helg = datetime.datetime.now()
    return helg