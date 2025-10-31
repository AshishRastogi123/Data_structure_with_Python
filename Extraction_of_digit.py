n=int(input("Enter a number: "))
print("The digits Extracted From last to start are:")
while n>0:
    digit=n%10
    print(digit)
    n=n//10