year = int(input("Enter Year"))

if year % 4 == 0 and year % 100 !=0:
    print(year,"is a Leap Year")
elif year % 100 == 0:
    print(year,"is not a Leap year")
elif year % 400 == 0:
    print(year,"is a Leap year")
else:
    print(year,"is not a leap year")