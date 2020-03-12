from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from time import time
x=0

def some_job():
    global x
    now = datetime.datetime.now()
    print(str(x) + ": " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    x = x + 1


def test():
    exec(open("screenShare.py").read())

scheduler = BlockingScheduler()
scheduler.add_job(test, 'cron', second='0,20,40')
scheduler.add_job(test, 'cron', second='10,30,50')
scheduler.start()