age = int(input("Enter your age:\n"))
if age < 0:
    print("You are not born yet.")
    exit(0)
decade = age // 10
years = age % 10
print("You are " + str(decade) + " decades and " + str(years) + " years old.")
