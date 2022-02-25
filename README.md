# woo algo trading sdk
A python developer kit for rapid algo trading development, notably the use of event callbacks.

## Logging Usage
- woo_sdk includes rotational logger (deletes log past one day)
- DAILY, HOURLY, EOD processes logged by default
- logger can be used anywhere else in code
```
sdk.logger.debug("text)
sdk.logger.info("text)
sdk.logger.warning("text)
sdk.logger.error("text)
sdk.logger.critical("text)
```

## Scheduler Usage
- CACHER, DAILY, HOURLY, EOD point to function references (remove parenthesis)
- STOP_TIME takes a (str) time to stop and run the EOD process
> Note : scheduler may ommit certain process if not needed (i.e. ommiting DAILY, HOURLY, or EOD)
```
import woo_sdk as sdk

def caching_process():
    sdk.logger.info('* i am caching')

def hourly_process(return_data, strategy_name):
    sdk.logger.info(f"({strategy_name}) i am hourly")

def daily_process(return_data, strategy_name):
    sdk.logger.info(f"({strategy_name}) i am daily")

def eod_process(return_data, strategy_name):
    sdk.logger.info(f"({strategy_name}) i am eod")

sdk.scheduler.run(
    DAILY  = daily_process,
    HOURLY = hourly_process,
    EOD    = eod_process,
    ########################
    STOP_TIME = "16:00",
    CACHER    = caching_process
)
```
## Sleep usage
- allows computer to sleep until "nextMinute" or "nextHour" or half hour when "HALF=True"
```
import woo_sdk as sdk

sdk.sleep.nextMinute()
sdk.sleep.nextHour()
sdk.sleep.nextHour(HALF=True)
```
