# Hugo Solares

import pandas as pd
import matplotlib.pyplot as plt

airline_key = 'airline'
avocados_key = 'avocados'
avocados_2016_key = 'avocados_2016'
homeless_key = 'homeless'
sales_key = 'sales'
temp_key = 'temp'

base_file_path = 'data/pandas_manipulation/'
airline_file_path = f'{base_file_path}airline_bumping.csv'
avocados_file_path = f'{base_file_path}avoplotto.pkl'
avocados_2016_file_path = f'{base_file_path}avocados_2016.csv'
homeless_file_path = f'{base_file_path}homelessness.csv'
sales_file_path = f'{base_file_path}sales_subset.csv'
temp_file_path = f'{base_file_path}temperatures.csv'


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
        if data_selector == airline_key:
            return pd.read_csv(airline_file_path, index_col=0)
        elif data_selector == avocados_key:
            return pd.read_pickle(avocados_file_path)
        elif data_selector == avocados_2016_key:
            return pd.read_csv(avocados_2016_file_path, index_col=0)
        elif data_selector == homeless_key:
            return pd.read_csv(homeless_file_path, index_col=0)
        elif data_selector == sales_key:
            return pd.read_csv(sales_file_path, index_col=0)
        elif data_selector == temp_key:
            return pd.read_csv(temp_file_path, index_col=0)
        elif data_selector is None:
            return None
        else:
            raise ValueError("Invalid data_selector provided.")

    # Read and explore the homelessness DF
    def exercise_1(self):
        homelessness = self.df

        # Print the head of the homelessness data
        print(homelessness.head())

        # Print the tail of the homelessness data
        print(homelessness.tail())

        # Print a random sample of the homelessness data
        print(homelessness.sample())

        # Print information about homelessness, including data types and null values.
        print(homelessness.info())

        # Print the shape of homelessness, shape attribute is a tuple containing the number of rows and columns
        print(homelessness.shape)

        # Print a description of homelessness, with descriptive statistics about the DataFrame
        # such as mean, median, min, max, etc.
        print(homelessness.describe())

    # Explore the DF parts and print them, it consists of only 3 parts: values, column names and indexes,
    # those are stored as attributes
    def exercise_2(self):
        homelessness = self.df

        # Print the values of homelessness
        print(homelessness.values)

        # Print the column index of homelessness
        print(homelessness.columns)

        # Print the row index of homelessness
        print(homelessness.index)

    # Indexing and Selection
    def exercise_2_1(self):
        homelessness = self.df

        # Select a single column from a DataFrame with df[column_name].
        print(homelessness['state'].head())

        # Select a single column from a DataFrame with df.column_name.
        print(homelessness.region.head())

        # Select multiple columns from a DataFrame with df[[col1, col2]].
        print(homelessness[['region', 'state']].head())

        # Loc, Select specific rows and columns by labels with df.loc[row_label, col_label]
        print(homelessness.loc[3, 'state'])

        # Iloc, Select specific rows and columns by integer indices with df.iloc[row_index, col_index]
        print(homelessness.iloc[3, 1])

    # Filtering simple and multiple columns
    def exercise_2_2(self):
        homelessness = self.df

        # Filter rows based on a condition df[df['column'] > value]
        print(homelessness[homelessness['individuals'] > 10000])

        # Filter rows based on multiple conditions, use & operator
        print(homelessness[(homelessness['individuals'] > 10000) & (homelessness['state_pop'] > 15000000)])

    # Perform Sorting operations in DF, note that a list can be passed as an argument
    def exercise_3(self):
        homelessness = self.df

        # Sort homelessness by individuals
        homelessness_ind = homelessness.sort_values("individuals")

        # Print the top few rows
        print(homelessness_ind.head())

        # Sort homelessness by descending family members
        homelessness_fam = homelessness.sort_values("family_members", ascending=False)

        # Print the top few rows
        print(homelessness_fam.head())

        # Sort homelessness by region, then descending family members
        homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

        # Print the top few rows
        print(homelessness_reg_fam.head())

    # Perform sub setting by columns
    def exercise_4(self):
        homelessness = self.df

        # Select the individuals column
        individuals = homelessness['individuals']

        # Print the head of the result
        print(individuals.head())

        # Select the state and family_members columns
        state_fam = homelessness[['state', 'family_members']]

        # Print the head of the result
        print(state_fam.head())

        # Select only the individuals and state columns, in that order
        ind_state = homelessness[['individuals', 'state']]

        # Print the head of the result
        print(ind_state.head())

    # Perform sub setting by rows, note that you can subset rows with multiple conditions using () and &
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

    # Perform sub setting by rows with categorical values, note that isin() can accept a list
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

    # Broadcasting, Add a column in the DF called 'total' with the sum of 'individuals' and 'family_members'
    def exercise_7(self):
        homelessness = self.df

        # Add total col as sum of individuals and family_members
        total = homelessness['individuals'] + homelessness['family_members']
        homelessness['total'] = total

        # Add p_individuals col as proportion of total that are individuals
        homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']

        # See the result
        print(homelessness)

    # We have seen the four most common types of data manipulation: sorting rows, subsetting columns, 
    # subsetting rows, and adding new columns.
    # Perform broadcasting calculations and subsetting operations in the DF to find the places with high homelessness
    def exercise_8(self):
        homelessness = self.df

        # Create indiv_per_10k col as homeless individuals per 10k state pop
        homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']

        # Subset rows for indiv_per_10k greater than 20
        high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

        # Sort high_homelessness by descending indiv_per_10k
        high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)

        # From high_homelessness_srt, select the state and indiv_per_10k cols
        result = high_homelessness_srt[['state', 'indiv_per_10k']]

        # See the result
        print(result)

    # Find unique values in a given column
    def exercise_8_1(self):
        homelessness = self.df

        print(homelessness['state'].unique())

    # Summary statistics
    # Explore the sales dataset, calculate and print the mean and the median of 'weekly_sales'
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

    # Calculate the maximum and minimum of 'date' in sales DF
    def exercise_10(self):
        sales = self.df

        # Print the maximum of the date column
        print(sales['date'].max())

        # Print the minimum of the date column
        print(sales['date'].min())

    # Define a custom IQR function and print aggregate operations using this function
    # The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to
    # more than one column of a DataFrame at once, making your aggregations super-efficient.
    def exercise_11(self):
        sales = self.df

        # A custom IQR (inter-quartile range) function
        def iqr(column):
            return column.quantile(0.75) - column.quantile(0.25)

        # Print IQR of the temperature_c column
        print(sales['temperature_c'].agg(iqr))

        # Print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
        print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))

        # Print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment,
        # passing median as a string argument instead of np.median object
        print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, 'median']))

    # Find the cumulative sum and maximum values in 'weekly_sales' from 'store' = 1 and 'department' == 1 data
    def exercise_12(self):
        # Subset the DF to find the data in which 'store' == 1 and 'department' == 1, note that we use & operator
        sales_1_1 = self.df[(self.df['store'] == 1) & (self.df['department'] == 1)]

        # Sort sales_1_1 by date
        sales_1_1 = sales_1_1.sort_values('date', ascending=True)

        # Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
        sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

        # Get the cumulative max of weekly_sales, add as cum_max_sales col
        sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

        # See the columns you calculated
        print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

    # Find unique combinations of 'store' and 'type' / 'store' and 'department' by dropping duplicates
    # subset the rows where 'is_holiday' == True, dropping duplicates with the same 'date'
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

    # From last exercise, count and get the proportion of the store/types and store/departments, sort them
    def exercise_14(self):
        sales = self.df
        store_types = sales.drop_duplicates(subset=["store", "type"])
        store_depts = sales.drop_duplicates(subset=["store", "department"])

        # Count the number of stores of each type
        store_counts = store_types['type'].value_counts()
        print(store_counts)

        # Get the proportion of stores of each type
        store_props = store_types['type'].value_counts(normalize=True)
        print(store_props)

        # Count the number of each department number and sort
        dept_counts_sorted = store_depts['department'].value_counts(sort=True)
        print(dept_counts_sorted)

        # Get the proportion of departments of each number and sort
        dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
        print(dept_props_sorted)

        # Another way to just print count uniques
        sales['count'] = sales.groupby(['store', 'department']).transform('size')
        sales = sales.drop_duplicates(subset=['store', 'department'])
        print(sales[['store', 'department', 'count']])

        counts = sales.groupby(['store', 'department']).size().reset_index(name='count')
        unique_counts = counts.drop_duplicates(subset=['store', 'department'])
        print(unique_counts)

    # Grouped summary statistics, without using groupby()
    # Calculate the percentage of sales occurred in each store type
    def exercise_15(self):
        sales = self.df

        # Calc total weekly sales
        sales_all = sales["weekly_sales"].sum()

        # Subset for type A stores, calc total weekly sales
        sales_a = sales[sales["type"] == "A"]["weekly_sales"].sum()

        # Subset for type B stores, calc total weekly sales
        sales_b = sales[sales["type"] == "B"]["weekly_sales"].sum()

        # Subset for type C stores, calc total weekly sales
        sales_c = sales[sales["type"] == "C"]["weekly_sales"].sum()

        # Get proportion for each type
        sales_prop_by_type = [sales_a, sales_b, sales_c] / sales_all
        print(sales_prop_by_type)

    # Calculations with groupby()
    def exercise_16(self):
        sales = self.df

        # Group by type; calc total weekly sales
        sales_by_type = sales.groupby("type")["weekly_sales"].sum()

        # Get proportion for each type
        sales_prop_by_type = sales_by_type / sum(sales['weekly_sales'])
        print(sales_prop_by_type)

        # Group by type and is_holiday; calc total weekly sales
        sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
        print(sales_by_type_is_holiday)

    # Multiple grouped summaries
    def exercise_17(self):
        sales = self.df

        # For each store type, aggregate weekly_sales: get min, max, mean, and median, passing aggregates as a strings
        sales_stats = sales.groupby('type')['weekly_sales'].agg(['min', 'max', 'mean', 'median'])

        # Print sales_stats
        print(sales_stats)

        # For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
        # passing aggregates as a strings
        unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg(
            ['min', 'max', 'mean', 'median'])

        # Print unemp_fuel_stats
        print(unemp_fuel_stats)

    # Pivoting on one variable
    def exercise_18(self):
        sales = self.df

        # Calculate the mean using groupby()
        mean_sales_by_type = sales.groupby("type")["weekly_sales"].mean()
        print(mean_sales_by_type)

        # Calculate the mean using pivot_table(), Pivot for mean weekly_sales for each store type, not specifying
        # aggfunc argument returns mean by default
        mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')

        # Print mean_sales_by_type
        print(mean_sales_by_type)

        # Pivot for mean and median weekly_sales for each store type
        mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=['mean', 'median'])

        # Print mean_med_sales_by_type
        print(mean_med_sales_by_type)

        mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales', index='type', columns='is_holiday',
                                                       aggfunc='mean')

        # Print mean_sales_by_type_holiday
        print(mean_sales_by_type_holiday)

    # Pivoting on 2 variables, filling the NaN with 0
    def exercise_19(self):
        sales = self.df

        # Print mean weekly_sales by department and type; fill missing values with 0
        print(
            sales.pivot_table(values='weekly_sales', index='department', columns='type', aggfunc='mean', fill_value=0))

        # Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
        print(sales.pivot_table(values="weekly_sales", index="department", columns="type", aggfunc='mean', fill_value=0,
                                margins=True))

    # Find the countries with the most null values registered and sort them in descending order
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

    # Setting and removing indexes
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

        # Reset the temperatures_ind index, dropping its contents it will completely eliminate the index column
        print(temperatures_ind.reset_index(drop=True))

    # Subsetting in DF using .loc[] and indexes
    def exercise_22(self):
        temperatures = self.df
        temperatures_ind = temperatures.set_index("city")

        # Make a list of cities to subset on
        cities = ["Moscow", "Saint Petersburg"]

        # Subset temperatures using square brackets
        print(temperatures[temperatures["city"].isin(cities)])

        # Subset temperatures_ind using .loc[]
        print(temperatures_ind.loc[cities])

    # Setting multi-level indexing of hierarchical indexing
    def exercise_23(self):
        temperatures = self.df

        # Index temperatures by country & city
        temperatures_ind = temperatures.set_index(["country", "city"])

        # List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
        rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

        # Subset for rows to keep
        print(temperatures_ind.loc[rows_to_keep])

    # Sorting by index values with multi_level index
    def exercise_24(self):
        temperatures = self.df
        temperatures_ind = temperatures.set_index(["country", "city"])

        # Sort temperatures_ind by index values
        print(temperatures_ind.sort_index())

        # Sort temperatures_ind by index values at the city level
        print(temperatures_ind.sort_index(level=["city", "country"]))

        # Sort temperatures_ind by country then descending city
        print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))

    # Slicing using .loc[] with multi-level index
    def exercise_25(self):
        temperatures = self.df
        temperatures_ind = temperatures.set_index(["country", "city"])

        # Sort the index of temperatures_ind
        temperatures_srt = temperatures_ind.sort_index()

        # Subset rows from Pakistan to Russia
        print(temperatures_srt.loc["Pakistan":"Russia"])

        # Try to subset rows from Lahore to Moscow
        print(temperatures_srt.loc["Lahore":"Moscow"])

        # Subset rows from Pakistan, Lahore to Russia, Moscow
        print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])

    # Slicing in both directions
    def exercise_26(self):
        temperatures = self.df
        temperatures_ind = temperatures.set_index(["country", "city"])
        temperatures_srt = temperatures_ind.sort_index()

        # Subset rows from India, Hyderabad to Iraq, Baghdad
        print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

        # Subset columns from date to avg_temp_c
        print(temperatures_srt.loc[:, "date":"avg_temp_c"])

        # Subset in both directions at once
        print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), "date":"avg_temp_c"])

    # Slicing with time series
    def exercise_27(self):
        temperatures = self.df

        # Use Boolean conditions to subset temperatures for rows in 2010 and 2011
        temperatures_bool = temperatures[
            (temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
        print(temperatures_bool)

        # Set date as the index and sort the index
        temperatures_ind = temperatures.set_index("date").sort_index()

        # Use .loc[] to subset temperatures_ind for rows in 2010 and 2011, mind the inclusive range
        print(temperatures_ind.loc["2010":"2012"])

        # Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011, mind the inclusive range
        print(temperatures_ind.loc["2010-08":"2011-03"])

    # Subsetting by row and column number with .iloc[]
    def exercise_28(self):
        temperatures = self.df

        # Get 23rd row, 2nd column (index 22, 1)
        print(temperatures.iloc[22, 1])

        # Use slicing to get the first 5 rows
        print(temperatures.iloc[:5])

        # Use slicing to get columns 3 to 4
        print(temperatures.iloc[:, 2:4])

        # Use slicing in both directions at once
        print(temperatures.iloc[:5, 2:4])

    # Pivot temperature table by city and year
    def exercise_29(self):
        temperatures = self.df
        # Convert "date" column to datetime format
        temperatures["date"] = pd.to_datetime(temperatures["date"])

        # Add a year column to temperatures
        temperatures["year"] = temperatures["date"].dt.year
        print(temperatures.head())

        # Pivot avg_temp_c by country and city vs year
        temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country", "city"],
                                                                columns="year")

        # See the result
        print(temp_by_country_city_vs_year)

    # Subsetting pivot tables, first make the pivot table, then subset it with .loc[]
    def exercise_30(self):
        temperatures = self.df
        temperatures["date"] = pd.to_datetime(temperatures["date"])
        temperatures["year"] = temperatures["date"].dt.year
        temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country", "city"],
                                                                columns="year")

        # Subset for Egypt to India
        print(temp_by_country_city_vs_year.loc["Egypt":"India"])

        # Subset for Egypt, Cairo to India, Delhi
        print(temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")])

        # Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
        print(temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"])

    # Calculating on a pivot table
    def exercise_31(self):
        temperatures = self.df
        temperatures["date"] = pd.to_datetime(temperatures["date"])
        temperatures["year"] = temperatures["date"].dt.year
        temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country", "city"],
                                                                columns="year")

        # Get the worldwide mean temp by year
        mean_temp_by_year = temp_by_country_city_vs_year.mean(axis="index")

        # Filter for the year that had the highest mean temp
        print(mean_temp_by_year[mean_temp_by_year == max(mean_temp_by_year)])

        # Get the mean temp by city
        mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

        # Filter for the city that had the lowest mean temp
        print(mean_temp_by_city[mean_temp_by_city == min(mean_temp_by_city)])

    # Find the most popular avocado
    def exercise_32(self):
        avocados = self.df

        # Look at the first few rows of data
        print(avocados.head())

        # Get the total number of avocados sold of each size
        nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

        # Create a bar plot of the number of avocados sold by size, you can set up colors
        nb_sold_by_size.plot(kind="bar", color=['blue', 'green', 'red'])

        # Show the plot
        plt.show()

    # Find the changes in sales over time
    def exercise_33(self):
        avocados = self.df

        # Get the total number of avocados sold on each date
        nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
        print(nb_sold_by_date.head())

        # Create a line plot of the number of avocados sold by date
        nb_sold_by_date.plot(kind="line", color='green', rot=45)

        # Show the plot
        plt.show()

    # Avocado supply and demand, Plot the relationship between number sold vs average price
    def exercise_34(self):
        avocados = self.df

        # Scatter plot of nb_sold vs avg_price with title
        avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

        # Show the plot
        plt.show()

    # Create histograms showing the average price with conventional and organic avocados
    def exercise_35(self):
        avocados = self.df

        # Histogram of conventional avg_price 
        avocados[avocados["type"] == "conventional"]["avg_price"].hist()

        # Histogram of organic avg_price
        avocados[avocados["type"] == "organic"]["avg_price"].hist()

        # Add a legend
        plt.legend(["conventional", "organic"])

        # Show the plot
        plt.show()

        # Modify histogram transparency to 0.5 
        avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

        # Modify histogram transparency to 0.5
        avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

        # Add a legend
        plt.legend(["conventional", "organic"])

        # Show the plot
        plt.show()

        # Modify bins to 20
        avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

        # Modify bins to 20
        avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

        # Add a legend
        plt.legend(["conventional", "organic"])

        # Show the plot
        plt.show()

    # Find missing values, plot the histogram of occurrence
    def exercise_36(self):
        avocados_2016 = self.df

        # Check individual values for missing values
        print(avocados_2016.isna())

        # Check each column for missing values
        print(avocados_2016.isna().any())

        # Bar plot of missing values by variable
        avocados_2016.isna().sum().plot(kind="bar", rot=45)

        # Show plot
        plt.show()

    # Missing Data Handling, remove missing values and check info()
    def exercise_37(self):
        avocados_2016 = self.df

        # Remove rows with missing values
        avocados_complete = avocados_2016.dropna()

        # Check if any columns contain missing values
        print(avocados_complete.isna().any())

    # Replace missing values, Plot the occurrence of missing data in the DF before and after replacing
    def exercise_38(self):
        avocados_2016 = self.df

        # List the columns with missing values
        cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

        # Create histograms showing the distributions cols_with_missing
        avocados_2016[cols_with_missing].plot(kind="hist")
        # avocados_2016[cols_with_missing].hist()

        # Show the plot
        plt.show()

        # Fill in missing values with 0
        avocados_filled = avocados_2016.fillna(0)

        # Create histograms of the filled columns
        avocados_filled[cols_with_missing].hist()

        # Show the plot
        plt.show()

    # Create a DF using dictionaries, list of dictionaries
    def exercise_39(self):
        # Create a list of dictionaries with new data
        avocados_list = [
            {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
            {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
        ]

        # Convert list into DataFrame
        avocados_2019 = pd.DataFrame(avocados_list)

        # Print the new DataFrame
        print(avocados_2019)

    # Create a DF using dictionaries, dictionary of lists
    def exercise_40(self):
        # Create a dictionary of lists with new data
        avocados_dict = {
            "date": ["2019-11-17", "2019-12-01"],
            "small_sold": [10859987, 9291631],
            "large_sold": [7674135, 6238096]
        }

        # Convert dictionary into DataFrame
        avocados_2019 = pd.DataFrame(avocados_dict)

        # Print the new DataFrame
        print(avocados_2019)

    # Read a CSV, work in the DF to find the number of bumps for every 10000 passengers
    def exercise_41(self):
        # Read CSV as DataFrame called airline_bumping, already done in the set_data() method above
        airline_bumping = self.df

        # Take a look at the DataFrame
        print(airline_bumping.head())

        # For each airline, select nb_bumped and total_passengers and sum
        airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

        # Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
        airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

        # Print airline_totals
        print(airline_totals)

    # Writing DF to CSV
    def exercise_42(self):
        airline_bumping = self.df
        airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
        airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

        # Create airline_totals_sorted
        airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

        # Print airline_totals_sorted
        print(airline_totals_sorted)

        # Save as airline_totals_sorted.csv
        airline_totals_sorted.to_csv("data/pandas_manipulation/airline_totals_sorted.csv")


if __name__ == '__main__':
    try:
        # Here all the instances are being executed only when called and with the given key, hope you find it useful
        # Manipulation(homeless_key).exercise_1()
        # Manipulation(homeless_key).exercise_2()
        # Manipulation(homeless_key).exercise_2_1()
        # Manipulation(homeless_key).exercise_2_2()
        # Manipulation(homeless_key).exercise_3()
        # Manipulation(homeless_key).exercise_4()
        # Manipulation(homeless_key).exercise_5()
        # Manipulation(homeless_key).exercise_6()
        # Manipulation(homeless_key).exercise_7()
        # Manipulation(homeless_key).exercise_8()
        # Manipulation(homeless_key).exercise_8_1()
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
        # Manipulation(temp_key).exercise_22()
        # Manipulation(temp_key).exercise_23()
        # Manipulation(temp_key).exercise_24()
        # Manipulation(temp_key).exercise_25()
        # Manipulation(temp_key).exercise_26()
        # Manipulation(temp_key).exercise_27()
        # Manipulation(temp_key).exercise_28()
        # Manipulation(temp_key).exercise_29()
        # Manipulation(temp_key).exercise_30()
        # Manipulation(temp_key).exercise_31()
        # Manipulation(avocados_key).exercise_32()
        # Manipulation(avocados_key).exercise_33()
        # Manipulation(avocados_key).exercise_34()
        # Manipulation(avocados_key).exercise_35()
        # Manipulation(avocados_2016_key).exercise_36()
        # Manipulation(avocados_2016_key).exercise_37()
        # Manipulation(avocados_2016_key).exercise_38()
        # Manipulation(None).exercise_39()
        # Manipulation(None).exercise_40()
        # Manipulation(airline_key).exercise_41()
        Manipulation(airline_key).exercise_42()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
