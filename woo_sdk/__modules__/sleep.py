import datetime as dt
import time
import pytz

tz = pytz.timezone("America/New_York")

def nextMinute():
    wait_seconds = 60 - dt.datetime.now().second
    print(f"[sleep.min] {wait_seconds}s")
    time.sleep(wait_seconds)
    print('[+1 min] ', dt.datetime.now(tz).strftime("%H:%M"))

def nextHour(
        HALF = False,
    ):
    
    now = dt.datetime.now()
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30

    if HALF == True and now.minute < 30:
        snapped_time = (now.replace(second=0, microsecond=0, minute=30, hour=now.hour)
                            + dt.timedelta(hours=now.minute//30))
    else:
        NEW_HOUR = now.hour if now.minute >= 30 else now.hour + 1
        snapped_time = (now.replace(second=0, microsecond=0, minute=0, hour=NEW_HOUR)
                            + dt.timedelta(hours=now.minute//30))
    
    secs = ( snapped_time - now ).seconds
    print(f"[sleep.hr] {secs}s")
    time.sleep(secs)
    print('[+1 hr] ', dt.datetime.now(tz).strftime("%H:%M"))

