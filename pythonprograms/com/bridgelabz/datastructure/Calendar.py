"""
purpose   : To create calender from given day,month and year

@Author   : Rohini Zade
@version  : 1.0
@since    : 2-12-2018

"""

from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *
from datetime import date, timedelta

if __name__ == "__main__":
    calendar_obj=Calendar()
    utility_obj = Utility()

    print("Enter the month(1-12):")
    month = utility_obj.inputIntiger()
    print("Enter the year:")
    year = utility_obj.inputIntiger()

    d_years = 0
    d_months = 0

    firstday=calendar_obj.get_first_day(year,month,d_years, d_months)
    #print(firstday)
    firstday_of_month = utility_obj.calculateDayOfWeek(firstday.day,firstday.month,firstday.year)
    daylist = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    #print("firstday_of_month:",firstday_of_month)
    #print(daylist[firstday_of_month])

    calendar_obj.calanderlogic(firstday_of_month,month,year)


