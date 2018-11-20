import sys
number=int(sys.argv[1])
if 0 <= number <= 31:
    for i in range(number+1):
        result= 2**i
        print(result)
else:
     print("Entered number is not valid")
