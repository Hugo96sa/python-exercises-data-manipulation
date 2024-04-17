# Hugo Solares

import pandas as pd
import numpy as np

baseball_key = 'baseball'
fifa_key = 'fifa'

baseball_file_path = 'data/introduction_to_python/baseball.csv'
fifa_file_path = 'data/introduction_to_python/fifa.csv'


class Introduction:
    def __init__(self, data_selector):
        try:
            self.df = self.set_data(data_selector)

        except FileNotFoundError:
            print(f"Error: File not found for: '{data_selector}'.")
            self.df = None

        except pd.errors.ParserError:
            print(f"Error: Parsing issue for: '{data_selector}'.")
            self.df = None

    def set_data(self, data_selector):
        if data_selector == baseball_key:
            return pd.read_csv(baseball_file_path)
        elif data_selector == fifa_key:
            return pd.read_csv(fifa_file_path, sep=', ')
        elif data_selector is None:
            return None
        else:
            raise ValueError("Invalid data_selector provided.")

    # Print the sum of 7 + 10
    def exercise_1(self):
        # Example, do not modify!
        print(5 / 8)
        # Print the sum of 7 and 10
        print(7 + 10)

    # Write the comment for the print for 7 + 10
    def exercise_2(self):
        # Division
        print(5 / 8)
        # Addition, practice with comments
        print(7 + 10)

    # Use Python to calculate arithmetic operations
    def exercise_3(self):
        # Addition
        print(4 + 5)
        # Subtraction
        print(5 - 5)
        # Multiplication
        print(3 * 5)
        # Division
        print(10 / 2)

    # Create and print a variable
    def exercise_4(self):
        # Create a variable savings
        savings = 100

        # Print out savings
        print(savings)

    # Create and perform calculations with variables
    def exercise_5(self):
        savings = 100

        # Create the variables monthly_savings and num_months
        monthly_savings = 10
        num_months = 4

        # Multiply monthly_savings and num_months
        new_savings = monthly_savings * num_months

        # Add new_savings to your savings
        total_savings = new_savings + savings

        # Print total_savings
        print(total_savings)

    # Create variables other than numbers
    def exercise_6(self):
        # Create a variable half
        half = 0.5

        # Create a variable intro
        intro = "Hello! How are you?"

        # Create a variable is_good
        is_good = True

    # Perform operations with other types
    def exercise_7(self):
        monthly_savings = 10
        num_months = 12
        intro = "Hello! How are you?"

        # Calculate year_savings using monthly_savings and num_months
        year_savings = monthly_savings * num_months

        # Print the type of year_savings
        print(type(year_savings))

        # Assign sum of intro and intro to doubleintro
        doubleintro = intro + intro

        # Print out doubleintro
        print(doubleintro)

    # Practice type conversion
    def exercise_8(self):
        # Definition of savings and total_savings
        savings = 100
        total_savings = 150

        # Fix the printout
        print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

        # Definition of pi_string
        pi_string = "3.1415926"

        # Convert pi_string into float: pi_float
        pi_float = float(pi_string)

    # Create a list
    def exercise_9(self):
        # area variables (in square meters)
        hall = 11.25
        kit = 18.0
        liv = 20.0
        bed = 10.75
        bath = 9.50

        # Create list areas
        areas = [hall, kit, liv, bed, bath]

        # Print areas
        print(areas)

    # Create a list with different types
    def exercise_10(self):
        # area variables (in square meters)
        hall = 11.25
        kit = 18.0
        liv = 20.0
        bed = 10.75
        bath = 9.50

        # Adapt list areas
        areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

        # Print areas
        print(areas)

    # Create a list of lists
    def exercise_11(self):
        # area variables (in square meters)
        hall = 11.25
        kit = 18.0
        liv = 20.0
        bed = 10.75
        bath = 9.50

        # house information as list of lists
        house = [["hallway", hall],
                 ["kitchen", kit],
                 ["living room", liv],
                 ["bedroom", bed],
                 ["bathroom", bath]]

        # Print out house
        print(house)

        # Print out the type of house
        print(type(house))

    # Subset elements inside the list
    def exercise_12(self):
        # Create the areas list
        areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

        # Print out second element from areas
        print(areas[1])

        # Print out last element from areas
        print(areas[-1])

        # Print out the area of the living room
        print(areas[5])

    # Create a dictionary-like list
    def exercise_13(self):
        # Create the areas list
        areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

        # Sum of kitchen and bedroom area: eat_sleep_area
        eat_sleep_area = areas[3] + areas[7]

        # Print the variable eat_sleep_area
        print(eat_sleep_area)

    # Create and subset a dictionary-like list
    def exercise_14(self):
        # Create the areas list
        areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

        # Use slicing to create downstairs
        downstairs = areas[0:6]

        # Use slicing to create upstairs
        upstairs = areas[6:10]

        # Print out downstairs and upstairs
        print(downstairs)
        print(upstairs)

    # Slice and subset a dictionary-like list
    def exercise_15(self):
        # Create the areas list
        areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

        # Alternative slicing to create downstairs
        downstairs = areas[:6]

        # Alternative slicing to create upstairs
        upstairs = areas[6:]

    # Replace elements inside of a list
    def exercise_16(self):
        # Create the areas list
        areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

        # Correct the bathroom area
        areas[-1] = 10.50

        # Change "living room" to "chill zone"
        areas[4] = "chill zone"

    # Extend a list, to delete elements of a list you may use del()
    def exercise_17(self):
        # Create the areas list and make some changes
        areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
                 "bedroom", 10.75, "bathroom", 10.50]

        # Add poolhouse data to areas, new list is areas_1
        areas_1 = areas + ["poolhouse", 24.5]

        # Add garage data to areas_1, new list is areas_2
        areas_2 = areas_1 + ["garage", 15.45]

    # Verify that original areas list is not afectes by changes in other copies
    def exercise_18(self):
        # Create list areas
        areas = [11.25, 18.0, 20.0, 10.75, 9.50]

        # Create areas_copy
        areas_copy = list(areas)

        # Change areas_copy
        areas_copy[0] = 5.0

        # Print areas
        print(areas)
    
    # Use some functions like type(), len(), int()
    def exercise_19(self):
        # Create variables var1 and var2
        var1 = [1, 2, 3, 4]
        var2 = True

        # Print out type of var1
        print(type(var1))

        # Print out length of var1
        print(len(var1))

        # Convert var2 to an integer: out2
        out2 = int(var2)

    # Review arguments usage in a function like sorted()
    def exercise_20(self):
        # Create lists first and second
        first = [11.25, 18.0, 20.0]
        second = [10.75, 9.50]

        # Paste together first and second: full
        print(first + second)

        # Sort full in descending order: full_sorted
        full_sorted = sorted(first + second, reverse=True)

        # Print out full_sorted
        print(full_sorted)

    # Exercise some string methods
    def exercise_21(self):
        # string to experiment with: place
        place = "poolhouse"

        # Use upper() on place: place_up
        place_up = place.upper()

        # Print out place and place_up
        print(place)
        print(place_up)

        # Print out the number of o's in place
        print(place.count("o"))

    # Now with list methods
    def exercise_22(self):
        # Create list areas
        areas = [11.25, 18.0, 20.0, 10.75, 9.50]

        # Print out the index of the element 20.0
        print(areas.index(20.0))

        # Print out how often 9.50 appears in areas
        print(areas.count(9.50))

    # More list methods
    def exercise_23(self):
        # Create list areas
        areas = [11.25, 18.0, 20.0, 10.75, 9.50]

        # Use append twice to add poolhouse and garage size
        areas.append(24.5)
        areas.append(15.45)

        # Print out areas
        print(areas)

        # Reverse the orders of the elements in areas
        areas.reverse()

        # Print out areas
        print(areas)

    # Calculate the area and the circumference of a circle
    def exercise_24(self):
        # Import the math package
        import math as mt

        # Definition of radius
        r = 0.43

        # Calculate C
        c = 2 * mt.pi * r

        # Calculate A
        a = mt.pi * (r ** 2)

        # Build printout
        print("Circumference: " + str(c))
        print("Area: " + str(a))

    # Calculate the distance travelled by the Moon over 12 degrees of its orbit
    def exercise_25(self):
        # Import radians function of math package
        from math import radians

        # Definition of radius
        r = 192500

        # Travel distance of Moon over 12 degrees. Store in dist.
        phi = radians(12)
        dist = r * phi

        # Print out dist
        print(dist)

    # turn a list into a numpy array
    def exercise_26(self):
        # Create list baseball
        baseball = [180, 215, 210, 210, 188, 176, 209, 200]

        # Create a numpy array from baseball: np_baseball
        np_baseball = np.array(baseball)

        # Print out type of np_baseball
        print(type(np_baseball))

    # Convert height in inches to meters using numpy arrays
    def exercise_27(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()

        # Create a numpy array from height_in: np_height_in
        np_height_in = np.array(height_in)

        # Print out np_height_in
        print(np_height_in)

        # Convert np_height_in to m: np_height_m
        np_height_m = np_height_in * 0.0254

        # Print np_height_m
        print(np_height_m)

    # Now find the weight in kg and calculate the bmi of each playes using numpy arrays
    def exercise_28(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()

        # Create array from height_in with metric units: np_height_m
        np_height_m = np.array(height_in) * 0.0254

        # Create array from weight_lb with metric units: np_weight_kg
        np_weight_kg = np.array(weight_lb) * 0.453592

        # Calculate the BMI: bmi
        bmi = np_weight_kg / (np_height_m ** 2)

        # Print out bmi
        print(bmi)
    
    # Find out which players are considered light using bmi with m and kg
    def exercise_29(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()

        # Calculate the BMI: bmi
        np_height_m = np.array(height_in) * 0.0254
        np_weight_kg = np.array(weight_lb) * 0.453592
        bmi = np_weight_kg / np_height_m ** 2

        # Create the light array
        light = bmi < 21

        # Print out light
        print(light)

        # Print out BMIs of all baseball players whose BMI is below 21
        print(bmi[light])

    # Subset numpy arrays
    def exercise_30(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()

        # Store weight and height lists as numpy arrays
        np_weight_lb = np.array(weight_lb)
        np_height_in = np.array(height_in)

        # Print out the weight at index 50
        print(np_weight_lb[50])

        # Print out sub-array of np_height_in: index 100 up to and including index 110
        print(np_height_in[100:111])

    # Practice 2d numpy arrays, first create one in pairs from the DF
    def exercise_31(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()

        # Combine height and weight into a list of lists
        baseball = [[h, w] for h, w in zip(height_in, weight_lb)]

        # Create a 2D numpy array from baseball: np_baseball
        np_baseball = np.array(baseball)

        # Print out the type of np_baseball
        print(type(np_baseball))

        # Print out the shape of np_baseball
        print(np_baseball.shape)

    # Checkout the data type in a numpy arrays
    def exercise_32(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()
        baseball = [[h, w] for h, w in zip(height_in, weight_lb)]

        # Create a 2D numpy array from baseball: np_baseball
        np_baseball = np.array(baseball)

        # Print out the shape of np_baseball
        print(np_baseball.shape)

    # Subset in a 2d numpy array
    def exercise_33(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()
        baseball = [[h, w] for h, w in zip(height_in, weight_lb)]

        # Create np_baseball (2 cols)
        np_baseball = np.array(baseball)

        # Print out the 50th row of np_baseball
        print(np_baseball[49, :])

        # Select and print the entire second column of np_baseball: np_weight_lb
        np_weight_lb = np_baseball[:, 1]
        print(np_weight_lb)

        # Print out height of 124th player
        print(np_baseball[123, 0])

    # Perform calculations inside the 3D np array, wheight, height and age
    def exercise_34(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()
        age_years = mlb_df['Age'].to_list()
        baseball = [[h, w, a] for h, w, a in zip(height_in, weight_lb, age_years)]

        # Create np_baseball (3 cols)
        np_baseball = np.array(baseball)

        # # Print out addition of np_baseball and updated, updated is a 2D np array of 1015 x 3, sadly not found in resources 
        # print(np_baseball + updated)
        
        # Create numpy array: conversion
        conversion = [0.0254, 0.453592, 1]
        np_conversion = np.array(conversion)
        
        # Print out product of np_baseball and conversion
        print(np_baseball * np_conversion)

    # Calculate the nean and median of the np_basebal np array
    def exercise_35(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()
        baseball = [[h, w] for h, w in zip(height_in, weight_lb)]
        np_baseball = np.array(baseball)

        # Create np_height_in from np_baseball
        np_height_in = np_baseball[:, 0]

        # Print out the mean of np_height_in
        print(np.mean(np_height_in))

        # Print out the median of np_height_in
        print(np.median(np_height_in))

    # Explore np_baseball data
    def exercise_36(self):
        mlb_df = self.df
        height_in = mlb_df['Height'].to_list()
        weight_lb = mlb_df['Weight'].to_list()
        baseball = [[h, w] for h, w in zip(height_in, weight_lb)]
        np_baseball = np.array(baseball)

        # Print mean height (first column)
        avg = np.mean(np_baseball[:, 0])
        print("Average: " + str(avg))

        # Print median height. Replace 'None'
        med = np.median(np_baseball[:, 0])
        print("Median: " + str(med))

        # Print out the standard deviation on height. Replace 'None'
        stddev = np.std(np_baseball[:, 0])
        print("Standard Deviation: " + str(stddev))

        # Print out correlation between first and second column. Replace 'None'
        corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
        print("Correlation: \n" + str(corr))

    # Now use fifa data, practice np operations and retrieve summary statistics
    def exercise_37(self):
        fifa_df = self.df
        positions = fifa_df['position'].to_list()
        heights = fifa_df['height'].to_list()

        # Convert positions and heights to numpy arrays: np_positions, np_heights
        np_positions = np.array(positions)
        np_heights = np.array(heights)

        # Heights of the goalkeepers: gk_heights
        gk_heights = np_heights[np_positions == 'GK']

        # Heights of the other players: other_heights
        other_heights = np_heights[np_positions != 'GK']

        # Print out the median height of goalkeepers. Replace 'None'
        print("Median height of goalkeepers: " + str(np.median(gk_heights)))

        # Print out the median height of other players. Replace 'None'
        print("Median height of other players: " + str(np.median(other_heights)))


if __name__ == '__main__':
    try:
        # Here all the instances are being executed only when called and with the given key, hope you find it useful
        # Introduction(None).exercise_1()
        # Introduction(None).exercise_2()
        # Introduction(None).exercise_3()
        # Introduction(None).exercise_4()
        # Introduction(None).exercise_5()
        # Introduction(None).exercise_6()
        # Introduction(None).exercise_7()
        # Introduction(None).exercise_8()
        # Introduction(None).exercise_9()
        # Introduction(None).exercise_10()
        # Introduction(None).exercise_11()
        # Introduction(None).exercise_12()
        # Introduction(None).exercise_13()
        # Introduction(None).exercise_14()
        # Introduction(None).exercise_15()
        # Introduction(None).exercise_16()
        # Introduction(None).exercise_17()
        # Introduction(None).exercise_18()
        # Introduction(None).exercise_19()
        # Introduction(None).exercise_20()
        # Introduction(None).exercise_21()
        # Introduction(None).exercise_22()
        # Introduction(None).exercise_23()
        # Introduction(None).exercise_24()
        # Introduction(None).exercise_25()
        # Introduction(None).exercise_26()
        # Introduction(baseball_key).exercise_27()
        # Introduction(baseball_key).exercise_28()
        # Introduction(baseball_key).exercise_29()
        # Introduction(baseball_key).exercise_30()
        # Introduction(baseball_key).exercise_31()
        # Introduction(baseball_key).exercise_32()
        # Introduction(baseball_key).exercise_33()
        # Introduction(baseball_key).exercise_34()
        # Introduction(baseball_key).exercise_35()
        # Introduction(baseball_key).exercise_36()
        Introduction(fifa_key).exercise_37()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError:
        print("There was a problem retrieving the pandas attribute or the key_selector is None.")
