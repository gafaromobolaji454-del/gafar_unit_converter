# Engineering Unit Converter
# This program shows a menu of unit conversions (mm <-> inches, °C <-> °F,
# kg <-> lb and km/h <-> m/s). The user can keep converting until they quit.
# My own twist: when the user quits, the program shows a history of all the
# conversions they did.

QUIT_OPTION = 9  # the menu number for "show history and quit"


def show_menu():
    """Print the list of conversions the user can choose from."""
    print("\n=== Engineering Unit Converter ===")
    print("1. Millimetres to inches")
    print("2. Inches to millimetres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to pounds")
    print("6. Pounds to kilograms")
    print("7. km/h to m/s")
    print("8. m/s to km/h")
    print("9. Show history and quit")


def get_menu_choice():
    """Keep asking until the user types a whole number from 1 to 9."""
    while True:  # repeats until we get a good answer
        text = input("Choose an option (1-9): ")
        try:
            choice = int(text)  # convert the typed text to a whole number
        except ValueError:
            # This runs if the user typed letters or symbols
            print("That is not a number. Please type a whole number from 1 to 9.")
            continue
        if 1 <= choice <= 9:
            return choice
        print("Please choose a number between 1 and 9.")


def get_number(prompt):
    """Keep asking until the user types a valid number, then return it as a float."""
    while True:
        text = input(prompt)
        try:
            return float(text)  # convert the typed text to a decimal number
        except ValueError:
            print("That is not a number. Please type digits only, for example 36.6")


def convert(choice, value):
    """Do the chosen conversion and return a sentence describing the result."""
    if choice == 1:
        result = value / 25.4
        return f"{value} mm = {result:.2f} inches"
    elif choice == 2:
        result = value * 25.4
        return f"{value} inches = {result:.2f} mm"
    elif choice == 3:
        result = value * 9 / 5 + 32
        return f"{value} °C = {result:.2f} °F"
    elif choice == 4:
        result = (value - 32) * 5 / 9
        return f"{value} °F = {result:.2f} °C"
    elif choice == 5:
        result = value * 2.20462
        return f"{value} kg = {result:.2f} lb"
    elif choice == 6:
        result = value / 2.20462
        return f"{value} lb = {result:.2f} kg"
    elif choice == 7:
        result = value / 3.6
        return f"{value} km/h = {result:.2f} m/s"
    else:
        # The only choice left is 8
        result = value * 3.6
        return f"{value} m/s = {result:.2f} km/h"


def main():
    history = []  # a list that stores every conversion the user does

    while True:  # keep converting until the user chooses to quit
        show_menu()
        choice = get_menu_choice()

        if choice == QUIT_OPTION:
            break  # leave the loop and go to the history

        value = get_number("Enter the value to convert: ")
        result_text = convert(choice, value)
        print(result_text)
        history.append(result_text)  # save it for the history

    # Twist: show everything the user converted
    print("\n--- Conversion history ---")
    if len(history) == 0:
        print("You did not do any conversions.")
    else:
        for number, item in enumerate(history, start=1):
            print(f"{number}. {item}")
    print("\nGoodbye!")


# Run the program
main()
