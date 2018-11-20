import sys
import math

t=int(sys.argv[1])
v=int(sys.argv[2])

def computeWindChill(t,v):
    wc = 0.0
    if(math.fabs(t) <= 50 and (math.fabs(v) <= 120 and math.fabs(v) >= 3)):
        wc = (85.74 + 0.6215 + (0.4275 * t - 35.75) * math.pow(v, 0.16))
        print("Result:",wc)
    else:
        print("Entered value for t and v are invalid..!!!")

        t=int(input("Entered value for t :"))
        v=int(input("Entered value for v :"))
        computeWindChill(t, v)
    return

computeWindChill(t,v)