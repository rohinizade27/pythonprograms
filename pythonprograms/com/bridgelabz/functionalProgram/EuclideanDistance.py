from com.bridgelabz.utility.Utility  import Utility
import sys

utility_obj=Utility()
x=int(sys.argv[1])
y=input(sys.argv[2])
distance=utility_obj.FindEuclideanDistance(x,y)
print("Euclidean Distance is:",distance)