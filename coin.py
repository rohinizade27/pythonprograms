import random

headcount=0;
tailcount=0;
num_of_trails=int(input("Enter the number of trails you want to filp the coin:"))
for i in range(num_of_trails):
    random_number=random.random()
    print(random_number)
    if random_number>0.5:
        headcount=headcount+1
    else:
        tailcount=tailcount+1

headpercent=(headcount*100)/num_of_trails
print("Head percentage:")
print(headpercent)
tailpercent=(tailcount*100)/num_of_trails
print("Tail percentage:")
print(tailpercent)

if headpercent>tailpercent:
    print("Head percentage is greater")
else:
    print("tail percentage is greater")