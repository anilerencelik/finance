from datetime import datetime, timedelta
import pytz
    
def getTime(tz='Europe/Istanbul'):
    datetime_now = datetime.now(pytz.timezone(tz))
    return datetime_now.strftime("%H:%M:%S")

def getDates(tz='Europe/Istanbul', delta=10):
    date_now = datetime.now(pytz.timezone(tz))
    if date_now.weekday() == 6:
        date_now -= timedelta(2)
    elif date_now.weekday() == 5:
        date_now -= timedelta(1)
    if date_now.weekday() == 0:
        delta += 2
    date_yestarday = date_now - timedelta(delta)
    return (date_now.strftime("%Y-%m-%d"), date_yestarday.strftime("%Y-%m-%d"))

def isWorkingHours(tz='Europe/Istanbul'):
    now = datetime.now(pytz.timezone(tz))
    start_time = now.replace(hour=10, minute=0, second=0)
    end_time = now.replace(hour=18, minute=20, second=0)
    return (start_time <= now <= end_time) and isWorkingDays()

def isWorkingDays(now=None):
    if now == None:
        now = datetime.now(pytz.timezone('Europe/Istanbul'))
    return (now.weekday() in (0, 1, 2, 3, 4))