#5. Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt.

import time 
import schedule
from datetime import datetime

def timeX():
    now = datetime.now()
    a = open("Marvellous.txt",'a')
    a.write(now.strftime("%d-%m-%Y %I:%M %p")+"\n")

def main():
    schedule.every(2).seconds.do(timeX)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()