number=int(input("Enter the number:"))
factors=[]
primefactors=[]
isprime=0
for i in range(2,int(number+1)):
    while number%i==0:
        factors.append(i)
        print(" ",i)
        number=number/i

for i in range(0,len(factors)):
    if factors[i] == 2:
        primefactors.append(factors[i])
    else:
        for j in range(2,factors[i]):

            if factors[i]%j==0:
                isprime=0
                break
            else:
                isprime=1
        if isprime==1:
            primefactors.append(factors[i])

#print(factors)
print(primefactors)