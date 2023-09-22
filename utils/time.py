from datetime import datetime
import pytz
    
def getTime(tz='Europe/Istanbul'):
    datetime_now = datetime.now(pytz.timezone(tz))
    return datetime_now.strftime("%H:%M:%S")

def isWorkingHours(tz='Europe/Istanbul'):
    now = datetime.now(pytz.timezone(tz))
    start_time = now.replace(hour=10, minute=0, second=0)
    end_time = now.replace(hour=18, minute=0, second=0)
    return (start_time <= now <= end_time) and isWorkingDays()

def isWorkingDays():
    now = datetime.now(pytz.timezone('Europe/Istanbul'))
    return (now in (0, 1, 2, 3, 4))