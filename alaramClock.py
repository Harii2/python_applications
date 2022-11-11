import datetime
import win32api     #pip install pywin32

class Alarm_clock :

    def __init__(self,day_of_the_week = None,time=None):
        self.day_of_the_week = None
        self.time = None
        self.snoozed = True

    def get_current_time(self):
        time = datetime.datetime.now()
        return time

    def start_alarm(self):
        alarm_hour = self.time.strftime("%H")
        alarm_minutes = self.time.strftime("%M")
        alarm_seconds = self.time.strftime("%S")

        while True:
            curr_date_and_time = datetime.datetime.now()
            curr_hour = curr_date_and_time.strftime("%H")
            curr_minutes = curr_date_and_time.strftime("%M")
            curr_seconds = curr_date_and_time.strftime("%S")
            curr_day = curr_date_and_time.strftime("%A")

            # print(alarm_hour, ":", alarm_minutes, ":", alarm_seconds, " ", curr_date_and_time.strftime("%H:%M:%S"))
            if alarm_hour == curr_hour and alarm_minutes == curr_minutes and alarm_seconds == curr_seconds and curr_day == self.day_of_the_week:
                for i in range(5):
                    win32api.Beep(3000, 1000)

                self.snoozed_alarm()
                break

    def snoozed_alarm(self):
        n = 1
        while n <= 3  :
            if self.snoozed :
                curr_time = datetime.datetime.now()
                user_alarm_time_date = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,int(self.time.strftime("%H")),int(self.time.strftime("%M")),int(self.time.strftime("%S")))
                diff = curr_time - user_alarm_time_date
                seconds = diff.seconds
                if(seconds > 300*n) :
                    for i in range(5):
                        win32api.Beep(3000, 1000)

                    n += 1
            else:
                break

    def delete_alarm(self):
        self.day_of_the_week= None
        self.time=None
        print("Alarm Deleted Succesfully")




    def create_alarm(self,day_of_the_week,time):
        self.day_of_the_week = day_of_the_week
        self.time = datetime.time(int(time[:2]),int(time[3:5]),int(time[6:]))
        self.start_alarm()
        print("Alarm created")




c = Alarm_clock()

#Day of week start with capital
day_of_the_week = input()

#Enter time in HH:MM:SS
t = input()

c.create_alarm(day_of_the_week,t)
c.delete_alarm()

