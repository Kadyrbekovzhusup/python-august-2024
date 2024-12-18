years = int(input("Enter number of years: "))
unit = input("""select your choice: 
1 - Days
2 - Weeks
3 - Hours
""")

if unit == "1":
    print(years*365)
elif unit == "2":
    print(years*52)
elif unit == "3":
    print(years*365*24)
else:
    print("Pick the right choice")



