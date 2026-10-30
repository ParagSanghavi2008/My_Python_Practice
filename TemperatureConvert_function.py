def celsius_to_fahrenheit(celsius):
    Fahrenheit = (celsius * 9 / 5) + 32 
    return float(Fahrenheit)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")