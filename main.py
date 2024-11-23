def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
"""Converts Celsius to Fahrenheit.
Args:
    celsius: the first sumand.
    9/5: fraction
    32: number.
Returns:
    The result of the conversion from celsius to fahrenheit.
"""

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
"""Converts Fahrenheit to Celsius.
Args:
    fahrenheit: the first sumand.
    32: number 
    5/9: fraction
Returns:
    The result of the conversion from fahrenheit to celsius.
"""

def is_even(num):
    return num % 2 == 0
"""Finds out if the number is even or odd
Args:
    Even or Odd
Returns:
    The result of the number is even or odd.
"""


if __name__ == "__main__":
        scale = input("Would you like to enter the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        """Ask the user what temperature they want
            Args:
                Celsius or Fahrenheit
            Returns:
                C/F
        """
    
if scale == 'C':
        celsius_input = float(input("Enter the temperature in Celsius: "))
        fahrenheit_result = celsius_to_fahrenheit(celsius_input)
        print(f"{celsius_input:.2f}°C is {fahrenheit_result:.2f}°F")
        """Ask the user for Celsius temperature
            Args:
        User inputs number for celsius
            Returns:
        The temperature in celsius and converts it fahrenheit
        """
        
        if is_even(int(celsius_input)):
            print(f"The temperature {celsius_input}°C is even.")
        else:
            print(f"The temperature {celsius_input}°C is odd.")
            
        """Determines if the temperature is even or odd
            Args:
                Pulls the celsius input
            Returns:
                If the input is even or odd
        """
        
elif scale == 'F':
        fahrenheit_input = float(input("Enter the temperature in Fahrenheit: "))
        celsius_result = fahrenheit_to_celsius(fahrenheit_input)
        print(f"{fahrenheit_input:.2f}°F is {celsius_result:.2f}°C")
        """Ask the user for Fahrenheit temperature
            Args:
                User inputs number for Fahrenheit 
            Returns:
                The temperature in fahrenheit and converts it celsius
        """
        
        if is_even(int(fahrenheit_input)):
            print(f"The temperature {fahrenheit_input}°F is even.")
        else:
            print(f"The temperature {fahrenheit_input}°F is odd.")
else:
    print("Invalid scale entered. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    
    """Determines if the temperature is even or odd
            Args:
                Pulls the fahrenheit input
            Returns:
                If the input is even or odd
        """