#2. Schedule a task that displays the current date and time every minute using the datetime module.

import schedule
import time
from datetime import datetime

def timeX():
    now = datetime.now()
    print("Current Date and Time:", now.strftime("%d-%m-%Y %I:%M %p"))

def main():
    schedule.every(1).minutes.do(timeX)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
