weather = input("Enter the weather (sunny or rainy):\n")
temperature = int(input("Enter the temperature:\n"))
if weather != "sunny" and weather != "rainy":
    print("Invalid weather")
    exit(0)
if weather == "sunny" and temperature >= 90:
    print("Stay Home")
elif weather == "rainy":
    print("Stay Home")
else:
    print("Go Hiking")
