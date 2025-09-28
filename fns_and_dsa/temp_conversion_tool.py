FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp = input("Enter the temperature value: ").strip()
    scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
    try:
        temp_value = float(temp)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    if scale == "C":
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result:.2f}°F")
    elif scale == "F":
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {result:.2f}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()