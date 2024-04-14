import math

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
            print("Please enter a valid numbers.")


if __name__ == '__main__':
    exer = Exercises()

    exer.exercise_1()
    exer.exercise_2()
    exer.exercise_3()
    exer.exercise_4()
    exer.exercise_5()
    exer.exercise_6()
    exer.exercise_7()
    exer.exercise_8()
    exer.exercise_9()
    exer.exercise_10()
    exer.exercise_11()
    exer.exercise_12()

