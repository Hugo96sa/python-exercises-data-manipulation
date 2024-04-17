# Hugo Solares

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

baseball_key = 'baseball'
brics_key = 'brics'
cars_key = 'cars'
gapminder_key = 'gapminder'

baseball_file_path = 'data/introduction_to_python/baseball.csv'
brics_file_path = 'data/intermediate_python/brics.csv'
cars_file_path = 'data/intermediate_python/cars.csv'
gapminder_file_path = 'data/intermediate_python/gapminder.csv'


class Intermediate:
    def __init__(self, data_selector):
        try:
            self.df = self.set_data(data_selector)
            np.random.seed(123)

        except FileNotFoundError:
            print(f"Error: File not found for: '{data_selector}'.")
            self.df = None

        except pd.errors.ParserError:
            print(f"Error: Parsing issue for: '{data_selector}'.")
            self.df = None

    def set_data(self, data_selector):
        if data_selector == baseball_key:
            return pd.read_csv(baseball_file_path)
        elif data_selector == brics_key:
            return pd.read_csv(brics_file_path, index_col=0)
        elif data_selector == cars_key:
            return pd.read_csv(cars_file_path, index_col=0)
        elif data_selector == gapminder_key:
            return pd.read_csv(gapminder_file_path, index_col=0)
        elif data_selector is None:
            return None
        else:
            raise ValueError("Invalid data_selector provided.")

    def exercise_1(self):
        # Pre-defined lists
        names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
        dr = [True, False, False, False, True, True, True]
        cpc = [809, 731, 588, 18, 200, 70, 45]

        # Create dictionary my_dict with three key:value pairs: my_dict
        my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

        # Build a DataFrame cars from my_dict: cars
        cars = pd.DataFrame(my_dict)

        # Definition of row_labels
        row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

        # Specify row labels of cars
        cars.index = row_labels
        print(cars)

        cars = cars.sort_values(by='cars_per_cap', ascending=False)
        print(cars)

    def exercise_2(self):
        cars_df = self.df
        print(cars_df)
        cars_df = cars_df.sort_values(by='cars_per_cap', ascending=False)
        print(cars_df)

    def exercise_3(self):
        brics_df = self.df
        print(brics_df)

        # column access, accepts lists
        print(brics_df[['country', 'capital']])
        # row access by slicing
        print(brics_df[2:4])
        # loc column access, accepts lists
        print(brics_df.loc[:, 'capital'])
        # loc row access
        print(brics_df.loc[['RU', 'IN']])

        # intersection
        print(brics_df.loc[['RU', 'CH'], ['country', 'capital', 'population']])

        # iloc intersection
        print(brics_df.iloc[[1, 3], [0, 1, 3]])

    def exercise_4(self):
        my_house = np.array([18.0, 20.0, 10.75, 9.50])
        your_house = np.array([14.0, 24.0, 14.25, 9.0])

        # my_house greater than 18.5 or smaller than 10
        print(np.logical_or(my_house > 18.5, my_house < 10))

        # Both my_house and your_house smaller than 11
        print(np.logical_and(my_house < 11, your_house < 11))

    def exercise_5(self):
        # Import cars data
        cars = self.df

        # Extract drives_right column as Series: dr
        dr = cars["drives_right"]

        # Use dr to subset cars: sel
        sel = cars[dr]

        # Print sel
        print(sel)

    def exercise_6(self):
        # Convert code to a one-liner
        print(self.df[self.df['drives_right']])

    def exercise_7(self):
        cars = self.df

        # Create car_maniac: observations that have a cars_per_cap over 500
        cpc = cars["cars_per_cap"]
        many_cars = cpc > 500
        car_maniac = cars[many_cars]

        # Print car_maniac
        print(car_maniac)

    def exercise_8(self):
        cars = self.df

        # Create medium: observations with cars_per_cap between 100 and 500
        cpc = cars['cars_per_cap']
        between = np.logical_and(cpc > 100, cpc < 500)
        medium = cars[between]

        # Print medium
        print(medium)

    def exercise_9(self):
        # areas list
        areas = [11.25, 18.0, 20.0, 10.75, 9.50]

        # Code the for loop
        for area in areas:
            print(area)

        # list comprehension
        print(list(area for area in areas))

    def exercise_10(self):
        # areas list
        areas = [11.25, 18.0, 20.0, 10.75, 9.50]

        # Change for loop to use enumerate() and update print()
        for index, a in enumerate(areas):
            print("room " + str(index) + ": " + str(a))

    def exercise_11(self):
        # areas list
        areas = [11.25, 18.0, 20.0, 10.75, 9.50]

        # Code the for loop
        for index, area in enumerate(areas):
            print("room " + str(index + 1) + ": " + str(area))

    def exercise_12(self):
        # house list of lists
        house = [["hallway", 11.25],
                 ["kitchen", 18.0],
                 ["living room", 20.0],
                 ["bedroom", 10.75],
                 ["bathroom", 9.50]]

        # Build a for loop from scratch
        for room in house:
            print("the " + str(room[0]) + " is " + str(room[1]) + " sqm")

    def exercise_13(self):
        # Definition of dictionary
        europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
                  'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

        # Iterate over europe
        for key, value in europe.items():
            print("the capital of " + key + " is " + str(value))

    def exercise_14(self):
        baseball_df = self.df
        height = baseball_df['Height'].to_numpy()  # Convert to NumPy array
        weight = baseball_df['Weight'].to_numpy()  # Convert to NumPy array
        np_height = np.array(height)
        np_weight = np.array(weight)

        # Combine height and weight into a list of lists
        np_baseball = np.array([[w, h] for w, h in zip(height, weight)])

        # For loop over np_height
        for element in np_height:
            print(str(element) + " inches")

        # For loop over np_baseball
        for x in np.nditer(np_baseball):
            print(str(x))

    def exercise_15(self):
        cars = self.df

        # Iterate over rows of cars
        for label, row in cars.iterrows():
            print(str(label))
            print(str(row))

    def exercise_16(self):
        cars = self.df

        # Adapt for loop
        for lab, row in cars.iterrows():
            print(str(lab) + ": " + str(row["cars_per_cap"]))

    def exercise_17(self):
        cars = self.df

        # Code for loop that adds COUNTRY column
        for label, row in cars.iterrows():
            cars.loc[label, "COUNTRY"] = row["country"].upper()

        # Print cars
        print(cars)

    def exercise_18(self):
        cars = self.df

        # Use .apply(str.upper)
        cars["COUNTRY"] = cars["country"].apply(str.upper)
        print(cars)

    def exercise_19(self):
        # Generate and print random float with the given seed
        print(np.random.rand())

    def exercise_20(self):
        # Use randint() to simulate a dice
        print(np.random.randint(1, 7))
        # Use randint() again
        print(np.random.randint(1, 7))

    def exercise_21(self):
        # Starting step
        step = 50

        # Roll the dice
        dice = np.random.randint(1, 7)

        # Finish the control construct
        if dice <= 2:
            step = step - 1
        elif dice <= 5:
            step += 1
        else:
            step = step + np.random.randint(1, 7)

        # Print out dice and step
        print(dice)
        print(step)

    def exercise_22(self):
        # Initialize random_walk
        random_walk = [0]

        # Complete the ___
        for x in range(100):
            # Set step: last element in random_walk
            step = random_walk[-1]

            # Roll the dice
            dice = np.random.randint(1, 7)

            # Determine next step
            if dice <= 2:
                step = step - 1
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1, 7)

            # append next_step to random_walk
            random_walk.append(step)

        # Print random_walk
        print(random_walk)

    def exercise_23(self):
        # Initialize random_walk
        random_walk = [0]

        for x in range(100):
            step = random_walk[-1]
            dice = np.random.randint(1, 7)

            if dice <= 2:
                # Replace below: use max to make sure step can't go below 0
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1, 7)

            random_walk.append(step)

        print(random_walk)

    def exercise_24(self):
        random_walk = [0]

        for x in range(100):
            step = random_walk[-1]
            dice = np.random.randint(1, 7)

            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1, 7)

            random_walk.append(step)

        # Import matplotlib.pyplot as plt
        import matplotlib.pyplot as plt

        # Plot random_walk
        plt.plot(random_walk)

        # Show the plot
        plt.show()

    def exercise_25(self):
        # Initialize all_walks (don't change this line)
        all_walks = []

        # Simulate random walk five times
        for i in range(5):

            # Code from before
            random_walk = [0]
            for x in range(100):
                step = random_walk[-1]
                dice = np.random.randint(1, 7)

                if dice <= 2:
                    step = max(0, step - 1)
                elif dice <= 5:
                    step = step + 1
                else:
                    step = step + np.random.randint(1, 7)
                random_walk.append(step)

            # Append random_walk to all_walks
            all_walks.append(random_walk)

        # Print all_walks
        print(all_walks)

    def exercise_26(self):
        # initialize and populate all_walks
        all_walks = []
        for i in range(5):
            random_walk = [0]
            for x in range(100):
                step = random_walk[-1]
                dice = np.random.randint(1, 7)
                if dice <= 2:
                    step = max(0, step - 1)
                elif dice <= 5:
                    step = step + 1
                else:
                    step = step + np.random.randint(1, 7)
                random_walk.append(step)
            all_walks.append(random_walk)

        # Convert all_walks to NumPy array: np_aw
        np_aw = np.array(all_walks)
        # Plot np_aw and show
        plt.plot(np_aw)
        plt.show()

        # Clear the figure
        plt.clf()

        # Transpose np_aw: np_aw_t
        np_aw_t = np.transpose(np_aw)
        # Plot np_aw_t and show
        plt.plot(np_aw_t)
        plt.show()

    def exercise_27(self):
        # clear the plot so it doesn't get cluttered if you run this many times
        plt.clf()

        # Simulate random walk 20 times
        all_walks = []
        for i in range(20):
            random_walk = [0]
            for x in range(100):
                step = random_walk[-1]
                dice = np.random.randint(1, 7)
                if dice <= 2:
                    step = max(0, step - 1)
                elif dice <= 5:
                    step = step + 1
                else:
                    step = step + np.random.randint(1, 7)

                # Implement clumsiness
                if np.random.rand() <= 0.005:
                    step = 0

                random_walk.append(step)
            all_walks.append(random_walk)

        # Create and plot np_aw_t
        np_aw_t = np.transpose(np.array(all_walks))
        plt.plot(np_aw_t)
        plt.show()

    def exercise_28(self):
        # Simulate random walk 500 times
        all_walks = []
        for i in range(500):
            random_walk = [0]
            for x in range(100):
                step = random_walk[-1]
                dice = np.random.randint(1, 7)
                if dice <= 2:
                    step = max(0, step - 1)
                elif dice <= 5:
                    step += 1
                else:
                    step = step + np.random.randint(1, 7)
                if np.random.rand() <= 0.001:
                    step = 0
                random_walk.append(step)
            all_walks.append(random_walk)

        # Create and plot np_aw_t
        np_aw_t = np.transpose(np.array(all_walks))

        # Select last row from np_aw_t: ends
        ends = np_aw_t[-1, :]

        # Plot histogram of ends, display plot
        plt.hist(ends)
        plt.show()


if __name__ == '__main__':
    try:
        # Here all the instances are being executed only when called and with the given key, hope you find it useful
        # Intermediate(None).exercise_1()
        # Intermediate(cars_key).exercise_2()
        # Intermediate(brics_key).exercise_3()
        # Intermediate(brics_key).exercise_3()
        # Intermediate(None).exercise_4()
        # Intermediate(cars_key).exercise_5()
        # Intermediate(cars_key).exercise_6()
        # Intermediate(cars_key).exercise_7()
        # Intermediate(cars_key).exercise_8()
        # Intermediate(None).exercise_9()
        # Intermediate(None).exercise_10()
        # Intermediate(None).exercise_11()
        # Intermediate(None).exercise_12()
        # Intermediate(None).exercise_13()
        # Intermediate(baseball_key).exercise_14() # very large
        # Intermediate(cars_key).exercise_15()
        # Intermediate(cars_key).exercise_16()
        # Intermediate(cars_key).exercise_17()
        # Intermediate(cars_key).exercise_18()
        # Intermediate(None).exercise_19()
        # Intermediate(None).exercise_20()
        # Intermediate(None).exercise_21()
        # Intermediate(None).exercise_22()
        # Intermediate(None).exercise_23()
        # Intermediate(None).exercise_24()
        # Intermediate(None).exercise_25()
        # Intermediate(None).exercise_26()
        # Intermediate(None).exercise_27()
        Intermediate(None).exercise_28()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError:
        print("There was a problem retrieving the pandas attribute or the key_selector is None.")
