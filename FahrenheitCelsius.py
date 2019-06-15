# fahrenheit / celsius converter (zero decimal places, rounds up)
import math

def convert_to_Celsius(temp):
    return (temp - 32) * 5/9

def convert_to_Fahrenheit(temp):
    return (temp * 9/5) + 32

print("Welcome to the temperature converter tool.")

while True:

    keyboardinput = raw_input("\nIf you have \
a Fahrenheit temperature to convert to Celsius, please press 1. \nIf you have \
a Celsius temperature to convert to Fahrenheit, please press 2. \nPress x to quit.")

    if keyboardinput == "1":
        tempFahrenheit = math.ceil(float(input("Please enter a temperature in Fahrenheit: ")))
        tempCelsius = math.ceil(convert_to_Celsius(tempFahrenheit))
        print("%d degrees Fahrenheit is equal to %d degrees Celsius.") % (tempFahrenheit, tempCelsius)

    if keyboardinput == "2":
        tempCelsius = math.ceil(float(input("Please enter a temperature in Celsius: ")))
        tempFahrenheit = math.ceil(convert_to_Fahrenheit(tempCelsius))
        print("%d degrees Celsius is equal to %d degrees Fahrenheit.") % (tempCelsius, tempFahrenheit)

    if keyboardinput == "x":
        quit()

    else:
        continue

