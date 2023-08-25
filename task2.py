#
##
### time counter
##
#

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60

    @staticmethod
    def from_seconds(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return Time(hours, minutes)

    def add(self, other_time):
        total_minutes = self.hours * 60 + self.minutes + other_time.hours * 60 + other_time.minutes
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)

    def subtract(self, other_time):
        total_minutes = self.hours * 60 + self.minutes - (other_time.hours * 60 + other_time.minutes)
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)

# Create two Time objects
a= int(input("hour of 1st time = "))
b=int(input("minute of 1st time = "))
c=int(input("hour of 2nd time = "))
d=int(input("minute of 2nd time = "))

time1 = Time(a, b)
time2 = Time(c, d)
opt=int(input("what u wanna do ? 1-add times 2-subtract 3- time to second 4-second to time"))
if opt==1:
    
    # Add the two times
    result_add = time1.add(time2)
    print(f"Addition: {time1} + {time2} = {result_add}")
elif opt==2:
    # Subtract the second time from the first time
    result_subtract = time1.subtract(time2)
    print(f"Subtraction: {time1} - {time2} = {result_subtract}")
elif opt==3:
# Convert time to seconds
    time_seconds = time1.to_seconds()
    print(f"{time1} in seconds: {time_seconds}")
elif opt==4:
# Convert seconds to time
    seconds = 10000
    time_from_seconds = Time.from_seconds(seconds)
    print(f"{seconds} seconds in time: {time_from_seconds}")
else:
    print("wrong input!")
