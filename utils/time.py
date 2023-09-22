from datetime import datetime
import pytz
    
def getTime(tz='Europe/Istanbul'):
    datetime_now = datetime.now(pytz.timezone(tz))
    return datetime_now.strftime("%H:%M:%S")
