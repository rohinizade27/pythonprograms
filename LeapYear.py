year=input("Enter the year:")
flag=0
def leapYearFunction(year):
    if len(year)<4:
        print("please ensure you have entered 4 digit number")
        newyear=input("Enter The Year:")
        leapYearFunction(newyear)
    else:
        if(int(year)%400==0):
            if(int(year)%100==0):
                if(int(year)%4==0):
                    print("Entered year is leap year")

                else:
                    print("Entered year is not leap year")
            else:
                print("Entered year is not leap year")
        else:
            print("Entered year is leap year")
    return

leapYearFunction(year)