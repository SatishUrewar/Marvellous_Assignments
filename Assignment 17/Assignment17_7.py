#7. Schedule a function that performs file backup every hour and writes a log entry into backup_log.txt.

import schedule
import time
from datetime import datetime

def backup():
    source = open("demo.txt",'r+b')
    destination = open("backup.txt",'w+b')
    destination.write(source.read())

    f = open("backup_log.txt",'a')
    f.write("Backup successfully at:" + datetime.now().strftime("%d-%m-%Y %I:%M %p")+"\n")

def main():
    schedule.every(1).hour.do(backup)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()