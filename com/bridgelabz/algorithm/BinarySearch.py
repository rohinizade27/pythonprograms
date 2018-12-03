
"""
purpose   : To find the possible Binary Search Trees from given number of node

@Author   : Rohini Zade
@version  : 1.0
@since    : 1-12-2018

"""
from com.bridgelabz.utility.Utility  import Utility

if __name__ == "__main__":
    utility_obj = Utility()

    starttime = utility_obj.getstartandstoptime()
    utility_obj.binarySearch()
    stoptime = utility_obj.getstartandstoptime()
    elapsetime = utility_obj.elapsedTime(starttime, stoptime)
    print("Elapsed time is:", elapsetime)




