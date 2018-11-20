import sys
import math

x=int(sys.argv[1])
y=int(sys.argv[2])
Result1 = math.pow(x, x)
Result2 = math.pow(y, y)
distance = math.sqrt(Result1 + Result2)
print("Euclidean Distance is:")
print(distance)

