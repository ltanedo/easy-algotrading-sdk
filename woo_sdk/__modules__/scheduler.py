from ..__utlity__ import callback
from . import sleep
from . import logger
import datetime      as dt 
from pytz import timezone
import time

def run(
    DAILY  = None,
    HOURLY = None,
    EOD    = None,
    ######################
    STOP_TIME = "16:00",
    CACHER = None,
):

    date = dt.datetime.now((timezone("America/New_York"))).strftime("%Y-%m-%d")
    STOP_TIME = (dt.datetime.fromisoformat(f"{date} {STOP_TIME}:00") ).replace(tzinfo=timezone("America/New_York"))

    if DAILY != None:
        logger.info("=====DAILY_STARTING=====")
        if CACHER != None: 
            logger.info("* caching ... ")
            CACHER()
            time.sleep(2)
        callback.run_folder({}, folder_name="__DAILY__", callback=DAILY)

    while dt.datetime.now(timezone("America/New_York")) < STOP_TIME:
        # FIXME: Use Rotational Logger
        sleep.nextHour()
        logger.info("=====HOURLY_STARTING=====")
        if HOURLY != None:
            if CACHER != None: 
                logger.info("* caching ... ")
                CACHER()
                time.sleep(2)
            callback.run_folder({}, folder_name="__HOURLY__", callback=HOURLY)

    if EOD != None:
        logger.info("=====EOD_STARTING=====")        
        callback.run_folder({}, folder_name="__EOD__", callback=EOD)

