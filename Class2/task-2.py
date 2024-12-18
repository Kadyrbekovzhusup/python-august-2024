years = int(input("Enter your age: "))

if years > 0 and years < 13:
    print("Child")
elif years >= 13 and years < 18:
    print("Teenager")
elif years >= 18 and years < 65:
    print("Adult")
elif years >= 65:
    print("Elder")
else:
    print("Wrong age")