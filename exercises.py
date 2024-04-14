import math
import numpy as np

class Exercises:

    # Sum 2 numbers and show its result
    def exercise_1(self):
        try:
            number_1 = int(input('Enter first number: '))
            number_2 = int(input('Enter second number: '))
            result = number_1 + number_2
            print('the sum is', result)
        
        except ValueError:
            print("Please enter valid integers.")
    
    # Calculate the circle area with a given radius
    def exercise_2(self):
        try:
            radius = float(input('Enter radius: '))
            area = math.pi * (radius ** 2)
            print('The area of the circle is:', round(area, 4))
        
        except ValueError:
            print("Please enter valid number.")
    
    # Concatenate a string with fstrings
    def exercise_3(self):
        try: 
            string_1 = input('Enter first string: ')
            string_2 = input('Enter second string: ')
            concat_string = f'{string_1} {string_2}'
            print(concat_string)

        except ValueError:
            print("Please enter valid Strings.")

    # Create a list and print it
    def exercise_4(self):
        list_1 = [1, 'two', 3.0, True]
        print(list_1)

    # Multiplicate 2 numbers and show its result
    def exercise_5(self):
        try:
            num_1 = int(input('Enter first number: '))
            num_2 = int(input('Enter second number: '))
            result = num_1 * num_2
            print(result)

        except ValueError:
            print("Please enter valid integers.")
    
    # Multiplicate 2 numbers without using * operator and show its result
    def exercise_6(self):
        def multiply_by_sum(num_1, num_2):
            result = 0
            for _ in range(abs(num_2)):
                result += num_1 if num_2 > 0 else -num_1
            return result
        
        try: 
            num_1 = int(input('Enter first number: '))
            num_2 = int(input('Enter second number: '))
            result = multiply_by_sum(num_1, num_2)
            print(f"The product of {num_1} and {num_2} is: {result}")

        except ValueError:
            print("Please enter valid integers.")

    # Create a text string and show its lenght
    def exercise_7(self):
        try:
            string = input('Enter a text string: ')
            length = len(string)
            print(f'length = {length}')

        except ValueError:
            print("Please enter a valid string.")
    
    # Calculate the mean of a list of numbers
    def exercise_8(self):
        try:
            string = input('Enter a list of numbers separated by spaces: ')
            # Split the string into a list of strings
            numbers_str = string.split(' ')
            # Convert each string in the list to an integer
            numbers = [int(num) for num in numbers_str]
            # Calculate the mean of the numbers
            mean = sum(numbers) / len(numbers)
            print(f'The mean of the list is: {mean}')

        except ValueError:
            print("Please enter a valid list.")
    
    # Create a tuple of elements and print it
    def exercise_9(self):
        my_tuple = (3, False, 'one', 5.5)
        print(f'Tuple = {my_tuple}')

    # Power of a number
    def exercise_10(self):
        try:
            base = int(input('Enter base number: '))
            exponent = int(input('Enter exponent number: '))
            result = base ** exponent
            print(f'result = {result}')
        
        except ValueError:
            print("Please enter a valid integers.")

    # Return the Inverse of a String
    def exercise_11(self):
        try:
            string = input('Enter a String to find out its inverse: ')
            inverse = string[::-1]
            print(f'Inverse string = {inverse}')

        except ValueError:
            print("Please enter a valid string.")

    # Calculate the rectangle area with given base and height
    def exercise_12(self):
        try:
            base = float(input('Enter base: '))
            height = float(input('Enter height: '))
            area = base * height
            print(f'The area is = {area}')
        
        except ValueError:
            print("Please enter valid numbers.")

    # Convert a whole number in string
    def exercise_13(self):
        try:
            integer = int(input('Enter a number: '))
            print(f'the integer was: {str(integer)}, input function reads a string, so it need to be converted to int.')

        except ValueError:
            print("Please enter a valid number.")

    # Replace a character in a string
    def exercise_14(self):
        try:
            string = input('Enter a string: ')
            old_char = input('Enter character to replace: ')
            new_char = input('Enter character to replace with: ')

            if len(old_char) != 1 or len(new_char) != 1:
                raise ValueError('Please enter single characters.')

            if old_char not in string:
                raise LookupError('Character not found in string.')

            string = string.replace(old_char, new_char)
            print(f'The new string is: {string}')

        except ValueError as e:
            print(e)
        except LookupError as e:
            print(e)

    # Turn a string to lowercase
    def exercise_15(self):
        try:
            lower_string = input('Enter a string: ')
            upper_string = lower_string.upper()
            print(f'The uppercase string is {upper_string}')

        except ValueError:
            print('Please enter a valid number.')

    # Sort a list in ascending order
    def exercise_16(self):
        try:
            string = input('Enter a list of numbers separated by spaces: ')
            # Split the string into a list of strings
            numbers_str = string.split(' ')
            # Convert each string in the list to an integer
            numbers = [int(num) for num in numbers_str]
            # sort the list
            numbers.sort()
            print(f'The sorted list is: {numbers}')

        except ValueError:
            print("Please enter a valid list.")
    
    # Calculate the power of a number without using the ** operator
    def exercise_17(self):
        try:
            base = int(input('Enter base number: '))
            power = int(input('Enter power number: '))
            result = 1
            for _ in range(power):
                result = result * base
            print(result)
        
        except ValueError:
            print("Please enter valid numbers.")

    # Extract a substring from a given string
    def exercise_18(self):
        try:
            string = input('Enter the string: ')
            pos_string_1 = int(input('Enter the start position: '))
            pos_string_2 = int(input('Enter the end position: '))

            if pos_string_1 < 0 or pos_string_2 > len(string):
                raise ValueError('Positions are not valid.')

            if pos_string_1 > pos_string_2:
                raise ValueError('End position should be greater than start position.')

            substring = string[pos_string_1:pos_string_2]
            print(f'The substring is {substring}')

        except ValueError as e:
            print(e)
    
    # convert a float into a string
    def exercise_19(self):
        try:
            number = int(input('Enter a decimal number: '))
            print(f'The integer number is: {number}')
        
        except ValueError:
            print("Please enter a valid numbers.")

    # Count the ocurrence of a character in a given string
    def exercise_20(self):
        try:
            string = input('Enter a string: ')
            char = input('Enter a char: ')
            if len(char) != 1:
                raise ValueError('Please enter single characters.')

            if char not in string:
                raise LookupError('Character not found in string.')
            
            count = string.count(char)
            print(f'The number of ocurrence is: {count}')

        except ValueError as e:
            print(e)
        
        except LookupError as e:
            print(e)

    # Find and show the last character of a string
    def exercise_21(self):
        try:
            string = input('Enter a string: ')
            last_char = string[-1]
            print(f'The last character is: {last_char}')

        except ValueError:
            print('Please enter a valid string.')
    
    # Multiply a string by a given number
    def exercise_22(self):
        try:
            string = input('Enter a string: ')
            number = int(input('Enter a number: '))
            result = string * number
            print(f'The result is: {result}')

        except ValueError:
            print('Please enter a valid string.')
    
    def exercise_23(self):
        try:
            string = input('Enter a string with spaces like the one you are reading: ')
            string_list = string.split()
            print(f'The string separated into simple words is {string_list}')

        except ValueError:
            print("Please enter a valid string.")


if __name__ == '__main__':
    exer = Exercises()

    # exer.exercise_1()
    # exer.exercise_2()
    # exer.exercise_3()
    # exer.exercise_4()
    # exer.exercise_5()
    # exer.exercise_6()
    # exer.exercise_7()
    # exer.exercise_8()
    # exer.exercise_9()
    # exer.exercise_10()
    # exer.exercise_11()
    # exer.exercise_12()
    # exer.exercise_13()
    # exer.exercise_14()
    # exer.exercise_15()
    # exer.exercise_16()
    # exer.exercise_17()
    # exer.exercise_18()
    # exer.exercise_19()
    # exer.exercise_20()
    # exer.exercise_21()
    # exer.exercise_22()
    exer.exercise_23()
