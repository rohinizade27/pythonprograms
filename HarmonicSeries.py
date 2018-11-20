number = float(input("Enter the number:"))
result=0.0
while number>0:
    result = float(result+1/number)
    number=number-1

print("Harmonic value:" ,str(result))