# MechaConvert - Smart Engineering Unit Converter
# Author: Friday Isaac Edet
# Department: Mechatronics Engineering
# Institution: YabaTech

# Conversion history
history = []


# Function to display the main menu
def show_menu():
    print("\n===== MECHACONVERT =====")
    print("1. Millimeters to Inches")
    print("2. Inches to Millimeters")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. km/h to m/s")
    print("8. m/s to km/h")
    print("9. View Conversion History")
    print("10. Engineering Reference")
    print("0. Exit")


# Function to perform conversions
def convert(choice, value):

    if choice == 1:
        result = value / 25.4
        unit = "inches"

    elif choice == 2:
        result = value * 25.4
        unit = "mm"

    elif choice == 3:
        result = (value * 9/5) + 32
        unit = "°F"

    elif choice == 4:
        result = (value - 32) * 5/9
        unit = "°C"

    elif choice == 5:
        result = value * 2.20462
        unit = "lb"

    elif choice == 6:
        result = value / 2.20462
        unit = "kg"

    elif choice == 7:
        result = value / 3.6
        unit = "m/s"

    elif choice == 8:
        result = value * 3.6
        unit = "km/h"

    else:
        return None, None

    return result, unit


# Function to display engineering constants
def engineering_reference():

    print("\n===== ENGINEERING REFERENCE =====")
    print("1 inch = 25.4 mm")
    print("1 kg = 2.20462 pounds")
    print("1 km/h = 0.277778 m/s")
    print("0°C = 32°F")
    print("1 meter = 1000 millimeters")


# Main program
while True:

    show_menu()

    try:
        choice = int(input("\nChoose an option: "))

        if choice == 0:
            print("Thank you for using MechaConvert!")
            break

        elif choice == 9:

            print("\n===== CONVERSION HISTORY =====")

            if len(history) == 0:
                print("No conversions performed yet.")

            else:
                for item in history:
                    print(item)

        elif choice == 10:
            engineering_reference()

        elif 1 <= choice <= 8:

            value = float(input("Enter the value to convert: "))

            result, unit = convert(choice, value)

            if result is not None:

                output = f"{value} converted = {result:.4f} {unit}"

                print("\nConversion Result:")
                print(output)

                history.append(output)

        else:
            print("Invalid menu option. Choose between 0 and 10.")

    except ValueError:
        print("Invalid input! Please enter a number.")