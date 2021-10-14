# put your python code here
year = int(input().strip())

if year % 4 != 0:
    print("Ordinary")
elif year % 100 == 0 and year % 400 != 0:
    print("Ordinary")
else:
    print("Leap")
