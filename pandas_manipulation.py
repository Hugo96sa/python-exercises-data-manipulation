import pandas as pd
import numpy as np

homeless_key = 'homeless'
sales_key = 'sales'
temp_key = 'sales'

homeless_file_path = 'data/pandas_manipulation/homelessness.csv'
sales_file_path = 'data/pandas_manipulation/sales_subset.csv'
temp_file_path = 'data/pandas_manipulation/temperatures.csv'


class Manipulation:
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
        if data_selector == homeless_key:
            return pd.read_csv(homeless_file_path, index_col=0)
        elif data_selector == sales_key:
            return pd.read_csv(sales_file_path, index_col=0)
        elif data_selector == temp_key:
            return pd.read_csv(temp_file_path, index_col=0)
        elif data_selector is None:
            return None
        else:
            raise ValueError("Invalid data_selector provided.")

    def exercise_1(self):
        homelessness = self.df

        # Print the head of the homelessness data
        print(homelessness.head())

        # Print information about homelessness
        print(homelessness.info())

        # Print the shape of homelessness
        print(homelessness.shape)

        # Print a description of homelessness
        print(homelessness.describe())

    def exercise_2(self):
        homelessness = self.df

        # Print the values of homelessness
        print(homelessness.values)

        # Print the column index of homelessness
        print(homelessness.columns)

        # Print the row index of homelessness
        print(homelessness.index)

if __name__ == '__main__':
    try: 
        # Manipulation(homeless_key).exercise_1()
        Manipulation(None).exercise_2()
    
    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)  

    except AttributeError:
        print('There was a problem retriving the pandas attribute or the key_selector is None')
