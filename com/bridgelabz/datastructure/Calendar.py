from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *

if __name__ == "__main__":
    calendar_obj=Calendar()
    utility_obj = Utility()
    print("Enter the day:")
    day = utility_obj.inputIntiger()
    print("Enter the month:")
    month = utility_obj.inputIntiger()
    print("Enter the year:")
    year = utility_obj.inputIntiger()

    weekday = utility_obj.calculateDayOfWeek(day, month, year)

    calendar_obj.calanderlogic(year,month,weekday)


