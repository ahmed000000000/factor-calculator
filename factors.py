#factor calculator
num = int(input("Enter a number: \n"))
print(" ")


factors=[]
for i in range(1,num+1):
    if num%i == 0:
        factors.append(i)


if len(factors) ==2:
    print(num, "is a prime number. Therefore the only factors are itself and 1")
else:
    print(num, "has", len(factors), "factors")
    print("the factors of", num, "are",  factors)
    print(" ")

    a = 0
    for i in factors:
        if a < len(factors):
            print(num, "divided by", factors[a], "is equal to ", num//factors[a])
            a += 1



print(" ")
exit = input("AHMED'S FACTOR CALCULATOR")
