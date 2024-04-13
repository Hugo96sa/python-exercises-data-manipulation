import pandas as pd
import numpy as np

brics_key = 'brics'
cars_key = 'cars'
baseball_key = 'baseball'

brics_file_path = 'data/intermediate_python/brics.csv'
cars_file_path = 'data/intermediate_python/cars.csv'
baseball_file_path = 'data/introduction_to_python/baseball.csv'


class Intermediate:
    def __init__(self, data_selector, data_file_path):
        if data_selector == brics_key:
            self.df = pd.read_csv(data_file_path, index_col=0)
        elif data_selector == cars_key:
            self.df = pd.read_csv(data_file_path, index_col=0)
        elif data_selector == baseball_key:
            self.df = pd.read_csv(data_file_path)

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


if __name__ == '__main__':
    brics = Intermediate(brics_key, brics_file_path)
    cars = Intermediate(cars_key, cars_file_path)
    inter = Intermediate(None, None)
    baseb = Intermediate(baseball_key, baseball_file_path)

    # inter.exercise_1()
    # cars.exercise_2()
    # brics.exercise_3()
    # inter.exercise_4()
    # cars.exercise_5()
    # cars.exercise_6()
    # cars.exercise_7()
    # cars.exercise_8()
    # inter.exercise_9()
    # inter.exercise_10()
    # inter.exercise_11()
    # inter.exercise_12()
    # inter.exercise_13()
    # baseb.exercise_14() # very large
    # cars.exercise_15()
    # cars.exercise_16()
    cars.exercise_17()
