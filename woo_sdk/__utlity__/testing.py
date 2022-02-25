'''
dt
# datetime.datetime(2022, 2, 3, 17, 44, 56, 659595)

round_time(dt)
# datetime.datetime(2022, 2, 3, 17, 44, 57)

round_time(dt, timedelta(seconds=5))
# datetime.datetime(2022, 2, 3, 17, 44, 55)

round_time(dt, timedelta(seconds=0.25))
# datetime.datetime(2022, 2, 3, 17, 44, 56, 750000)

round_time(dt, timedelta(minutes=1))
# datetime.datetime(2022, 2, 3, 17, 45)

round_time(dt, timedelta(minutes=30))
# datetime.datetime(2022, 2, 3, 17, 30)

round_time(dt, timedelta(hours=1))
# datetime.datetime(2022, 2, 3, 18, 0)

round_time(dt, timedelta(hours=12))
# datetime.datetime(2022, 2, 3, 12, 0)

round_time(dt, timedelta(days=1))
# datetime.datetime(2022, 2, 4, 0, 0)
'''

def round_time(dt_obj: dt.datetime, unit=dt.timedelta(seconds=1)):
    seconds = (dt_obj - dt.datetime.min).total_seconds()
    unit_seconds = unit.total_seconds()
    half_over = seconds + unit_seconds / 2
    rounded_seconds = half_over - half_over % unit_seconds
    print(dt.timedelta(seconds=rounded_seconds))
    return dt.datetime.min + dt.timedelta(seconds=rounded_seconds)