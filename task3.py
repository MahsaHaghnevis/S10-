class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    def get_month_name(self):
        month_names = [
            "farvardin", "ordibehesth", "khordad", "tir", "mordad", "shahrivar",
            "mehr", "aban", "azar", "dey", "bahman", "esfand"
        ]
        return month_names[self.month - 1]

    def add(self, other_date):
        carry = 0

        new_day = self.day + other_date.day
        if new_day > 30:
            new_day -= 30
            carry = 1

        new_month = self.month + other_date.month + carry
        if new_month > 12:
            new_month -= 12
            carry = 1
        else:
            carry = 0

        new_year = self.year + other_date.year + carry

        return Date(new_year, new_month, new_day)

    def subtract(self, other_date):
        year_diff = self.year - other_date.year
        month_diff = self.month - other_date.month
        day_diff = self.day - other_date.day

        if day_diff < 0:
            month_diff -= 1
            day_diff += 30

        if month_diff < 0:
            year_diff -= 1
            month_diff += 12

        return Date(year_diff, month_diff, day_diff)

a=int(input("enter the 1st date year = "))
b=int(input("enter the 1st date month = "))
c=int(input("enter the 1st date day = "))
d=int(input("enter the 2nd date year = "))
e=int(input("enter the 2nd date month = "))
f=int(input("enter the 2nd date day = "))
# Create two Date objects
date1 = Date(a, b, c)
date2 = Date(d, e, f)
opttion=int(input("enter what u wanna do : 1-add 2-subtract 3-month name"))
if opttion==1:
    # Add the two dates
    result_add = date1.add(date2)
    print(f"Addition: {date1} + {date2} = {result_add}")
elif opttion==2:
# Subtract the second date from the first date
    result_subtract = date1.subtract(date2)
    print(f"Subtraction: {date1} - {date2} = {result_subtract}")
elif opttion==3:
    # Get month name of the first date
    month_name = date1.get_month_name()
    print(f"Month Name: {month_name}")
else:
    print("wrong input")
