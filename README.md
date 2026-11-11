# Engineering Unit Converter

## What it does
This Python program shows a menu of common engineering unit conversions: millimetres and inches, Celsius and Fahrenheit, kilograms and pounds, and km/h and m/s (both directions for each). The user can keep converting until they choose to quit.

## How to run it
Install Python 3, then run: python unit_converter.py

## Sample output
```
=== Engineering Unit Converter ===
1. Millimetres to inches
2. Inches to millimetres
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius
5. Kilograms to pounds
6. Pounds to kilograms
7. km/h to m/s
8. m/s to km/h
9. Show history and quit
Choose an option (1-9): 1
Enter the value to convert: 25.4
25.4 mm = 1.00 inches

=== Engineering Unit Converter ===
1. Millimetres to inches
2. Inches to millimetres
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius
5. Kilograms to pounds
6. Pounds to kilograms
7. km/h to m/s
8. m/s to km/h
9. Show history and quit
Choose an option (1-9): 3
Enter the value to convert: 100
100.0 °C = 212.00 °F

=== Engineering Unit Converter ===
1. Millimetres to inches
2. Inches to millimetres
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius
5. Kilograms to pounds
6. Pounds to kilograms
7. km/h to m/s
8. m/s to km/h
9. Show history and quit
Choose an option (1-9): 9

--- Conversion history ---
1. 25.4 mm = 1.00 inches
2. 100.0 °C = 212.00 °F

Goodbye!
```

## My own twist
When the user quits, the program shows a numbered history of every conversion they did during that session.

## What I learned
I learned how to use a menu inside a loop that repeats until the user chooses to quit, and how to store results in a list so I can show a history at the end. I also learned to check menu choices and numbers so the program asks again instead of crashing when someone types something wrong.

## Author
Gafar Omobolaji Haleem, ND1 Mechatronics Engineering, YabaTech.
