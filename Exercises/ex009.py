# Your Student ID: 220543603
# Your Name and Surname: Muhammed Elubeyid

conversion_type = input("Enter 1 to convert from Celsius to Fahrenheit (C to F) or 2 to convert Fahrenheit to Celsius (F to C)")

if conversion_type == '1':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f}C is equal to {fahrenheit:.2f}F")
elif conversion_type == '2':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}F is equal to {celsius:.2f}C")
else:
    print("Invalid input.")
