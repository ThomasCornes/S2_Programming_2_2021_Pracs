"""
CP1404/CP5632 - Practical - Suggested Solution
Temperature conversions
"""

MENU = """C - Convert Celsius to Fahrenheit
         F - Convert Fahrenheit to Celsius
            Q - Quit"""

def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":




def covert_Celsius_to_fahrenhiet(Celsius):
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)
