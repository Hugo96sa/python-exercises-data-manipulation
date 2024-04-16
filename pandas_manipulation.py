import pandas as pd
import numpy as np

homeless_key = 'homeless'
sales_key = 'sales'
temp_key = 'temp'

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

    # Read and explore the homelessness data
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

    # perform numpy observations and general extractions
    def exercise_2(self):
        homelessness = self.df

        # Print the values of homelessness
        print(homelessness.values)

        # Print the column index of homelessness
        print(homelessness.columns)

        # Print the row index of homelessness
        print(homelessness.index)

    # Perform sorting operations in DF
    def exercise_3(self):
        homelessness = self.df

        # Sort homelessness by individuals
        homelessness_ind = homelessness.sort_values("individuals")

        # Print the top few rows
        print(homelessness_ind.head())

        # Sort homelessness by descending family members
        homelessness_fam = homelessness.sort_values("family_members", ascending = False)

        # Print the top few rows
        print(homelessness_fam.head())

        # Sort homelessness by region, then descending family members
        homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending = [True, False])

        # Print the top few rows
        print(homelessness_reg_fam.head())

    # Perform sorting by value with two columns
    def exercise_4(self):
        homelessness = self.df

        # Sort homelessness by region, then descending family members
        homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending = [True, False])

        # Print the top few rows
        print(homelessness_reg_fam.head())

        # Select the state and family_members columns
        state_fam = homelessness[['state', 'family_members']]

        # Print the head of the result
        print(state_fam.head())

        # Select only the individuals and state columns, in that order
        ind_state = homelessness[['individuals', 'state']]

        # Print the head of the result
        print(ind_state.head())

    def exercise_5(self):
        homelessness = self.df

        # Filter for rows where individuals is greater than 10000
        ind_gt_10k = homelessness[homelessness['individuals'] > 10000]

        # See the result
        print(ind_gt_10k)

        # Filter for rows where region is Mountain
        mountain_reg = homelessness[homelessness['region'] == "Mountain"]

        # See the result
        print(mountain_reg)

        # Filter for rows where family_members is less than 1000 and region is Pacific
        fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & (homelessness['region'] == 'Pacific')]

        # See the result
        print(fam_lt_1k_pac)
    
    def exercise_6(self):
        homelessness = self.df

        # Subset for rows in South Atlantic or Mid-Atlantic regions
        regions = ['South Atlantic', 'Mid-Atlantic']
        south_mid_atlantic = homelessness[homelessness['region'].isin(regions)]

        # See the result
        print(south_mid_atlantic)

        # The Mojave Desert states
        canu = ["California", "Arizona", "Nevada", "Utah"]

        # Filter for rows in the Mojave Desert states
        mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

        # See the result
        print(mojave_homelessness)
    
    def exercise_7(self):
        homelessness = self.df

        # Add total col as sum of individuals and family_members
        total = homelessness['individuals'] + homelessness['family_members']
        homelessness['total'] = total

        # Add p_individuals col as proportion of total that are individuals
        homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']

        # See the result
        print(homelessness)
    
    def exercise_8(self):
        homelessness = self.df

        # Create indiv_per_10k col as homeless individuals per 10k state pop
        homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop'] 

        # Subset rows for indiv_per_10k greater than 20
        high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

        # Sort high_homelessness by descending indiv_per_10k
        high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending = False)

        # From high_homelessness_srt, select the state and indiv_per_10k cols
        result = high_homelessness_srt[['state', 'indiv_per_10k']]

        # See the result
        print(result)

    def exercise_9(self):
        sales = self.df

        # Print the head of the sales DataFrame
        print(sales.head())

        # Print the info about the sales DataFrame
        print(sales.info())

        # Print the mean of weekly_sales
        print(sales['weekly_sales'].mean())

        # Print the median of weekly_sales
        print(sales['weekly_sales'].median())

    def exercise_10(self):
        sales = self.df

        # Print the maximum of the date column
        print(sales['date'].max())

        # Print the minimum of the date column
        print(sales['date'].min())

    def exercise_11(self):
        sales = self.df

        # A custom IQR (inter-quartile range) function
        def iqr(column):
            return column.quantile(0.75) - column.quantile(0.25)
            
        # Print IQR of the temperature_c column
        print(sales['temperature_c'].agg(iqr))

        # Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
        print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))

        # Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment, passing median as a string instead of np.median
        print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, 'median']))

    def exercise_12(self):
        sales_1_1 = self.df[(self.df['store'] == 1) & (self.df['department'] == 1)]

        # Sort sales_1_1 by date
        sales_1_1 = sales_1_1.sort_values('date', ascending = True)

        # Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
        sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

        # Get the cumulative max of weekly_sales, add as cum_max_sales col
        sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

        # See the columns you calculated
        print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
    
    def exercise_13(self):
        sales = self.df

        # Drop duplicate store/type combinations
        store_types = sales.drop_duplicates(subset=['store', 'type'])
        print(store_types.head())

        # Drop duplicate store/department combinations
        store_depts = sales.drop_duplicates(subset=['store', 'department'])
        print(store_depts.head())

        # Subset the rows where is_holiday is True and drop duplicate dates
        holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset='date')

        # Print date col of holiday_dates
        print(holiday_dates['date'])

    def exercise_14(self):
        sales = self.df

        # Drop duplicate store/type combinations
        store_types = sales.drop_duplicates(subset=["store", "type"])

        # Drop duplicate store/department combinations
        store_depts = sales.drop_duplicates(subset=["store", "department"])

        # Count the number of stores of each type
        store_counts = store_types['type'].value_counts()
        print(store_counts)

        # Get the proportion of stores of each type
        store_props = store_types['type'].value_counts(normalize = True)
        print(store_props)

        # Count the number of each department number and sort
        dept_counts_sorted = store_depts['department'].value_counts(sort = True)
        print(dept_counts_sorted)

        # Get the proportion of departments of each number and sort
        dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
        print(dept_props_sorted)
    
    def exercise_15(self):
        sales = self.df

        # Calc total weekly sales
        sales_all = sales["weekly_sales"].sum()

        # Subset for type A stores, calc total weekly sales
        sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

        # Subset for type B stores, calc total weekly sales
        sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

        # Subset for type C stores, calc total weekly sales
        sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

        # Get proportion for each type
        sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
        print(sales_propn_by_type)
    
    def exercise_16(self):
        sales = self.df

        # Group by type; calc total weekly sales
        sales_by_type = sales.groupby("type")["weekly_sales"].sum()

        # Get proportion for each type
        sales_propn_by_type = sales_by_type / sum(sales['weekly_sales'])
        print(sales_propn_by_type)

        # Group by type and is_holiday; calc total weekly sales
        sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
        print(sales_by_type_is_holiday)

    def exercise_17(self):
        sales = self.df

        # For each store type, aggregate weekly_sales: get min, max, mean, and median, passing aggregates as a strings
        sales_stats = sales.groupby('type')['weekly_sales'].agg(['min', 'max', 'mean', 'median'])

        # Print sales_stats
        print(sales_stats)

        # For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median, passing aggregates as a strings
        unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg(['min', 'max', 'mean', 'median'])

        # Print unemp_fuel_stats
        print(unemp_fuel_stats)

    def exercise_18(self):
        sales = self.df

        # Pivot for mean weekly_sales for each store type
        mean_sales_by_type = sales.pivot_table(values = 'weekly_sales', index = 'type')

        # Print mean_sales_by_type
        print(mean_sales_by_type)

        # Pivot for mean and median weekly_sales for each store type
        mean_med_sales_by_type = sales.pivot_table(values = 'weekly_sales', index = 'type', aggfunc = ['mean', 'median'])

        # Print mean_med_sales_by_type
        print(mean_med_sales_by_type)

        mean_sales_by_type_holiday = sales.pivot_table(values = 'weekly_sales', index = 'type', columns = 'is_holiday', aggfunc = 'mean')

        # Print mean_sales_by_type_holiday
        print(mean_sales_by_type_holiday)

    def exercise_19(self):
        sales = self.df

        print(sales.pivot_table(values = 'weekly_sales', index = 'department', columns = 'type', aggfunc = 'mean', fill_value = 0))

        print(sales.pivot_table(values="weekly_sales", index="department", columns="type", aggfunc = 'mean', fill_value = 0, margins = True))

    def exercise_20(self):
        temp = self.df

        # Filter the DataFrame to include only rows with null values in 'avg_temp_c'
        null_temp_df = temp[temp['avg_temp_c'].isnull()]

        # Group by 'country' and count the null values in each group
        null_temp_counts = null_temp_df.groupby('country').size()

        # Sort the counts in descending order to find the country with the most null values
        null_temp_counts_sorted = null_temp_counts.sort_values(ascending=False)

        # Print the sorted counts
        print(null_temp_counts_sorted)

    def exercise_21(self):
        temperatures = self.df

        # Look at temperatures
        print(temperatures.head())

        # Set the index of temperatures to city
        temperatures_ind = temperatures.set_index("city")

        # Look at temperatures_ind
        print(temperatures_ind.head())

        # Reset the temperatures_ind index, keeping its contents
        print(temperatures_ind.reset_index())

        # Reset the temperatures_ind index, dropping its contents
        print(temperatures_ind.reset_index(drop=True))

if __name__ == '__main__':
    try: 
        # Manipulation(homeless_key).exercise_1()
        # Manipulation(homeless_key).exercise_2()
        Manipulation(homeless_key).exercise_3()
        # Manipulation(homeless_key).exercise_4()
        # Manipulation(homeless_key).exercise_5()
        # Manipulation(homeless_key).exercise_6()
        # Manipulation(homeless_key).exercise_7()
        # Manipulation(homeless_key).exercise_8()
        # Manipulation(sales_key).exercise_9()
        # Manipulation(sales_key).exercise_10()
        # Manipulation(sales_key).exercise_11()
        # Manipulation(sales_key).exercise_12()
        # Manipulation(sales_key).exercise_13()
        # Manipulation(sales_key).exercise_14()
        # Manipulation(sales_key).exercise_15()
        # Manipulation(sales_key).exercise_16()
        # Manipulation(sales_key).exercise_17()
        # Manipulation(sales_key).exercise_18()
        # Manipulation(sales_key).exercise_19()
        # Manipulation(temp_key).exercise_20()
        # Manipulation(temp_key).exercise_21()
    
    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)  

    except AttributeError:
        print("There was a problem retriving the pandas attribute or the key_selector is None.")
