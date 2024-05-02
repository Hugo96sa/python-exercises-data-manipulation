# Hugo Solares

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

clean_books_key = 'cle_boo'
clean_unemployment_key = 'cle_une'
divorce_key = 'divorce'
salaries_key = 'salaries'
salaries2_key = 'salaries2'
planes_key = 'planes'

base_file_path = 'data/exploratory_data_analysis/'
clean_books_file_path = f'{base_file_path}clean_books.csv'
clean_unemployment_file_path = f'{base_file_path}clean_unemployment.csv'
divorce_file_path = f'{base_file_path}divorce.csv'
salaries_file_path = f'{base_file_path}ds_salaries_clean.csv'
salaries2_file_path = f'{base_file_path}salaries2.csv'
planes_file_path = f'{base_file_path}planes.csv'


class Exploratory:
    def set_data(self, data_selector):
        try:
            if data_selector == clean_books_key:
                return pd.read_csv(clean_books_file_path)
            elif data_selector == clean_unemployment_key:
                return pd.read_csv(clean_unemployment_file_path)
            elif data_selector == divorce_key:
                return pd.read_csv(divorce_file_path)
            elif data_selector == salaries_key:
                return pd.read_csv(salaries_file_path)
            elif data_selector == salaries2_key:
                return pd.read_csv(salaries2_file_path)
            elif data_selector == planes_key:
                return pd.read_csv(planes_file_path)
            elif data_selector is None:
                return None
            else:
                raise ValueError("Invalid data_selector provided.")

        except FileNotFoundError:
            print(f"Error: File not found for: '{data_selector}'.")
            self.df = None

        except pd.errors.ParserError:
            print(f"Error: Parsing issue for: '{data_selector}'.")
            self.df = None

    # Functions for initial exploration
    def exercise_1(self):
        unemployment = self.set_data(clean_unemployment_key)

        # Print the first five rows of unemployment
        print(unemployment.head())

        # Print a summary of non-missing values and data types in the unemployment DataFrame
        print(unemployment.info())

        # Print summary statistics for numerical columns in unemployment
        print(unemployment.describe())

    # Counting categorical values
    def exercise_2(self):
        unemployment = self.set_data(clean_unemployment_key)

        # Count the values associated with each continent in unemployment
        print(unemployment['continent'].value_counts())

    # plot the histogram graph of the year 2021
    def exercise_3(self):
        unemployment = self.set_data(clean_unemployment_key)

        # Create a histogram of 2021 unemployment; show a full percent in each bin
        sns.histplot(data=unemployment, x='2021', binwidth=1)
        plt.show()

    # checking data types
    def exercise_4(self):
        unemployment = self.set_data(clean_unemployment_key)

        # Update the data type of the 2019 column to a float
        unemployment["2019"] = unemployment['2019'].astype(float)
        # Print the dtypes to check your work
        print(unemployment.dtypes)

    # Subseting data = Validating continents
    def exercise_5(self):
        unemployment = self.set_data(clean_unemployment_key)

        # Define a Series describing whether each continent is outside of Oceania
        not_oceania = ~unemployment['continent'].isin(['Oceania'])
        print(not_oceania)

        # Print unemployment without records related to countries in Oceania
        print(unemployment[not_oceania])

    # Create a boxplot using y argument with continent for each continent
    def exercise_6(self):
        unemployment = self.set_data(clean_unemployment_key)

        # Print the minimum and maximum unemployment rates during 2021
        print(min(unemployment['2021']), max(unemployment['2021']))

        # Create a boxplot of 2021 unemployment rates, broken down by continent
        sns.boxplot(data=unemployment, x='2021', y='continent', hue='continent', legend=False)
        plt.show()

    # Practice groupby() and agg()
    def exercise_7(self):
        unemployment = self.set_data(clean_unemployment_key)

        # Print the mean and standard deviation of rates by year
        print(unemployment.agg(['mean', 'std']))

        # Print yearly mean and standard deviation grouped by continent
        print(unemployment.groupby('continent').agg(['mean', 'std']))

    # Named aggregations
    def exercise_8(self):
        unemployment = self.set_data(clean_unemployment_key)

        continent_summary = unemployment.groupby("continent").agg(
            # Create the mean_rate_2021 column
            mean_rate_2021=('2021', 'mean'),
            # Create the std_rate_2021 column
            std_rate_2021=('2021', 'std')
        )
        print(continent_summary)

    def exercise_9(self):
        unemployment = self.set_data(clean_unemployment_key)

        # Create a bar plot of continents and their average unemployment
        sns.barplot(data=unemployment, x='continent', y='2021', hue='continent', legend=False)
        plt.show()

    def exercise_10(self):
        planes = self.set_data(planes_key)

        # Count the number of missing values in each column
        print(planes.isna().sum())

        # Find the five percent threshold
        threshold = len(planes) * 0.05
        print(f'Threshold: {threshold}')

        #  Create a filter
        cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

        # Drop missing values for columns below the threshold
        planes.dropna(subset=cols_to_drop, inplace=True)

        print(planes.isna().sum())

    def exercise_11(self):
        planes = self.set_data(planes_key)
        threshold = len(planes) * 0.05
        cols_to_drop = planes.columns[planes.isna().sum() <= threshold]
        planes.dropna(subset=cols_to_drop, inplace=True)

        # Check the values of the Additional_Info column
        print(planes["Additional_Info"].value_counts())

        # Create a box plot of Price by Airline
        sns.boxplot(data=planes, x='Airline', y='Price', hue='Airline', legend=False)
        plt.show()

    def exercise_12(self):
        planes = self.set_data(planes_key)
        threshold = len(planes) * 0.05
        cols_to_drop = planes.columns[planes.isna().sum() <= threshold]
        planes.dropna(subset=cols_to_drop, inplace=True)

        # Drop the 'B' column entirely
        planes.drop('Additional_Info', axis=1, inplace=True)

        # Calculate median plane ticket prices by Airline
        airline_prices = planes.groupby("Airline")["Price"].median()
        print(airline_prices)

        # Convert to a dictionary
        prices_dict = airline_prices.to_dict()

        # Map the dictionary to missing values of Price by Airline
        planes["Price"] = planes["Price"].fillna(planes["Airline"].map(prices_dict))

        # Check for missing values
        print(planes.isna().sum())

    def exercise_13(self):
        planes = self.set_data(planes_key)
        threshold = len(planes) * 0.05
        cols_to_drop = planes.columns[planes.isna().sum() <= threshold]
        planes.dropna(subset=cols_to_drop, inplace=True)
        planes.drop('Arrival_Time', axis=1, inplace=True)

        # Filter the DataFrame for object columns
        non_numeric = planes.select_dtypes("object")

        # Loop through columns
        for col in non_numeric.columns:
            # Print the number of unique values
            print(f"Number of unique values in {col} column: ", non_numeric[col].nunique())

    # Categorize the flight durations
    def exercise_14(self):
        planes = self.set_data(planes_key)

        #  Create a list of categories
        flight_categories = ["Short-haul", "Medium", "Long-haul"]

        #  Create short-haul values
        short_flights = "^0h|^1h|^2h|^3h|^4h"

        # Create medium-haul values
        medium_flights = "^5h|^6h|^7h|^8h|^9h"

        # Create long-haul values
        long_flights = "10h|11h|12h|13h|14h|15h|16h"

        # Define conditions for each flight category as boolean arrays
        conditions = [
            planes["Duration"].str.contains(short_flights).astype(bool),
            planes["Duration"].str.contains(medium_flights).astype(bool),
            planes["Duration"].str.contains(long_flights).astype(bool)
        ]

        # Create flight categories based on conditions
        planes["Duration_Category"] = np.select(
            conditions,
            flight_categories,
            default="Extreme duration"
        )

        # Plot the counts of each category
        sns.countplot(data=planes, x="Duration_Category", hue='Duration_Category', legend=False)
        plt.show()

    # helper function for calculating the numeric values of flight durations
    def convert_duration(self, duration_str):
        try:
            parts = duration_str.split(' ')
            hours = int(parts[0].replace('h', ''))
            minutes = 0
            if len(parts) > 1:
                minutes = int(parts[1].replace('m', ''))
            decimal_hours = hours + minutes / 60
            return decimal_hours
        except (ValueError, IndexError):
            return None

    # calculate the flight durations
    def exercise_15(self):
        planes = self.set_data(planes_key)

        # Preview the column and check data types, there are nan
        print(planes["Duration"].head())
        print(planes.dtypes)
        print(planes['Duration'].isna().sum())

        # Apply the conversion function and handle potential errors
        planes["Duration"] = planes["Duration"].apply(lambda x: self.convert_duration(x) if pd.notna(x) else np.NaN)

        # Check the updated column and data types
        print(planes["Duration"].head())
        print(planes.dtypes)

        #  Plot a histogram
        sns.histplot(data=planes, x="Duration")
        plt.show()

    # Add descriptive statistics
    def exercise_16(self):
        planes = self.set_data(planes_key)

        # Price standard deviation by Airline
        planes["airline_price_st_dev"] = planes.groupby("Airline")["Price"].transform(lambda x: x.std())
        print(planes[["Airline", "airline_price_st_dev"]].value_counts())

        # Median Duration by Airline
        planes["Duration"] = planes["Duration"].apply(lambda x: self.convert_duration(x) if pd.notna(x) else np.NaN)
        planes["airline_median_duration"] = planes.groupby("Airline")["Duration"].transform(lambda x: x.median())
        print(planes[["Airline", "airline_median_duration"]].value_counts())

        # Mean Price by Destination
        planes["price_destination_mean"] = planes.groupby("Destination")["Price"].transform(lambda x: x.mean())
        print(planes[["Destination", "price_destination_mean"]].value_counts())

    def exercise_17(self):
        planes = self.set_data(planes_key)

        #  Plot a histogram of flight prices
        sns.histplot(data=planes, x="Price")
        plt.show()

        # Display descriptive statistics for flight duration, both have outliers
        print(planes["Duration"].describe())
        print(planes["Price"].describe())

    def exercise_18(self):
        planes = self.set_data(planes_key)

        # Find the 75th and 25th percentiles
        price_seventy_fifth = planes["Price"].quantile(0.75)
        price_twenty_fifth = planes["Price"].quantile(0.25)

        # Calculate iqr
        prices_iqr = price_seventy_fifth - price_twenty_fifth

        # Calculate the thresholds
        upper = price_seventy_fifth + (1.5 * prices_iqr)
        lower = price_twenty_fifth - (1.5 * prices_iqr)

        # Subset the data
        planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]

        print(planes["Price"].describe())

        # Parsing dates when reading the csv

    def exercise_19(self):
        # Import divorce.csv, parsing the appropriate columns as dates in the import
        divorce = pd.read_csv(divorce_file_path, parse_dates=['divorce_date', 'dob_man', 'dob_woman'])
        print(divorce.dtypes)

        # Convert the marriage_date column to DateTime values
        divorce["marriage_date"] = pd.to_datetime(divorce['marriage_date'])
        print(divorce.dtypes)

    # Find a way tto extract the marriage_year from marriage_date
    def exercise_20(self):
        divorce = pd.read_csv(divorce_file_path, parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

        # Define the marriage_year column
        divorce["marriage_year"] = divorce["marriage_date"].dt.year

        # Create a line plot showing the average number of kids by year
        sns.lineplot(data=divorce, x='marriage_year', y='num_kids')
        plt.show()

    # plt as a scatter plot the marriage_duration vs num_kids
    def exercise_21(self):
        divorce = self.set_data(divorce_key)
        divorce["divorce_date"] = pd.to_datetime(divorce["divorce_date"])
        divorce["dob_man"] = pd.to_datetime(divorce["dob_man"])
        divorce["dob_woman"] = pd.to_datetime(divorce["dob_woman"])
        divorce["marriage_date"] = pd.to_datetime(divorce["marriage_date"])

        # Create the scatterplot
        sns.scatterplot(data=divorce, x='marriage_duration', y='num_kids')
        plt.show()

    # is there some correlation, after using .corr() use a pairplot
    def exercise_22(self):
        divorce = self.set_data(divorce_key)
        divorce["divorce_date"] = pd.to_datetime(divorce["divorce_date"])
        divorce["dob_man"] = pd.to_datetime(divorce["dob_man"])
        divorce["dob_woman"] = pd.to_datetime(divorce["dob_woman"])
        divorce["marriage_date"] = pd.to_datetime(divorce["marriage_date"])

        # Create a pairplot for income_woman and marriage_duration
        sns.pairplot(data=divorce, vars=["income_woman", "marriage_duration"])
        plt.show()

    # is there any correlation between the age at which a woman was married and her income
    def exercise_23(self):
        divorce = self.set_data(divorce_key)
        divorce["divorce_date"] = pd.to_datetime(divorce["divorce_date"])
        divorce["dob_man"] = pd.to_datetime(divorce["dob_man"])
        divorce["dob_woman"] = pd.to_datetime(divorce["dob_woman"])
        divorce["marriage_date"] = pd.to_datetime(divorce["marriage_date"])
        divorce["marriage_year"] = divorce["marriage_date"].dt.year
        divorce["man_age_marriage"] = divorce["marriage_year"] - divorce["dob_man"].dt.year
        divorce["woman_age_marriage"] = divorce["marriage_year"] - divorce["dob_woman"].dt.year

        # Create the scatter plot
        sns.scatterplot(data=divorce, x='woman_age_marriage', y='income_woman', hue='education_woman')
        plt.show()

    # Plot a kde graph for marriage_duration and num_kids
    def exercise_24(self):
        divorce = self.set_data(divorce_key)
        divorce["divorce_date"] = pd.to_datetime(divorce["divorce_date"])
        divorce["dob_man"] = pd.to_datetime(divorce["dob_man"])
        divorce["dob_woman"] = pd.to_datetime(divorce["dob_woman"])
        divorce["marriage_date"] = pd.to_datetime(divorce["marriage_date"])
        divorce["marriage_year"] = divorce["marriage_date"].dt.year
        divorce["man_age_marriage"] = divorce["marriage_year"] - divorce["dob_man"].dt.year
        divorce["woman_age_marriage"] = divorce["marriage_year"] - divorce["dob_woman"].dt.year

        # Create the KDE plot
        sns.kdeplot(data=divorce, x='marriage_duration', hue='num_kids')
        plt.show()

        # Update the KDE plot so that marriage duration can't be smoothed too far
        sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0)
        plt.show()

        # Update the KDE plot to show a cumulative distribution function
        sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative=True)
        plt.show()

    def exercise_25(self):
        salaries = self.set_data(salaries2_key)

        # Print the count of each job type in Job_Category
        print(salaries['Job_Category'].value_counts())

        # Print the relative frequency of Job_Category, this gives the proportion
        print(salaries['Job_Category'].value_counts(normalize=True))

    def exercise_26(self):
        salaries = self.set_data(salaries2_key)

        # Cross-tabulate Company_Size and Experience
        print(pd.crosstab(salaries["Company_Size"], salaries["Experience"]))

        # Cross-tabulate Job_Category and Company_Size
        print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"]))

        # Cross-tabulate Job_Category and Company_Size
        print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"],
                          values=salaries["Salary_USD"], aggfunc="mean"))

    def exercise_27(self):
        salaries = self.set_data(salaries2_key)
        salaries['date_of_response'] = pd.to_datetime(salaries['date_of_response'])
        print(salaries.info())

        #  Get the month of the response
        salaries["month"] = salaries["date_of_response"].dt.month

        #  Extract the weekday of the response
        salaries["weekday"] = salaries["date_of_response"].dt.weekday

        # Identify columns with string values
        string_columns = salaries.select_dtypes(include=['object']).columns
        columns_to_exclude = list(string_columns) + ['Working_Year']

        # Exclude columns with string values
        numeric_salaries = salaries.drop(columns=columns_to_exclude)

        # Create a heatmap
        sns.heatmap(numeric_salaries.corr(), annot=True)
        plt.show()

    def exercise_28(self):
        salaries = self.set_data(salaries2_key)

        # Find the 25th percentile
        twenty_fifth = salaries["Salary_USD"].quantile(0.25)

        # Save the median
        salaries_median = salaries["Salary_USD"].median()

        # Gather the 75th percentile
        seventy_fifth = salaries["Salary_USD"].quantile(0.75)
        print(twenty_fifth, salaries_median, seventy_fifth)

        # Create salary labels
        salary_labels = ["entry", "mid", "senior", "exec"]

        # Create the salary ranges list
        salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]

        # Create salary_level
        salaries["salary_level"] = pd.cut(salaries["Salary_USD"],
                                          bins=salary_ranges,
                                          labels=salary_labels)

        # Plot the count of salary levels at companies of different sizes
        sns.countplot(data=salaries, x="Company_Size", hue='salary_level')
        plt.show()

    def exercise_29(self):
        salaries = self.set_data(salaries2_key)

        # Filter for employees in the US or GB
        usa_and_gb = salaries[salaries["Employee_Location"].isin(["US", "GB"])]

        # Create a barplot of salaries by location
        sns.barplot(data=salaries, x="Salary_USD", y="Employee_Location", hue='Employee_Location', legend=False)
        plt.show()

        # Create a barplot of salaries by location
        sns.barplot(data=usa_and_gb, x="Employee_Location", y="Salary_USD", hue='Employee_Location', legend=False)
        plt.show()

    def exercise_30(self):
        salaries = self.set_data(salaries2_key)

        # Create a bar plot of salary versus company size, factoring in employment status
        sns.barplot(data=salaries, x="Company_Size", y="Salary_USD", hue="Employment_Status")
        plt.show()


if __name__ == '__main__':
    try:
        e = Exploratory()

        # e.exercise_1()
        # e.exercise_2()
        # e.exercise_3()
        # e.exercise_4()
        # e.exercise_5()
        # e.exercise_6()
        # e.exercise_7() # unable to run
        # e.exercise_8()
        # e.exercise_8()
        # e.exercise_9()
        # e.exercise_10()
        # e.exercise_11()
        # e.exercise_12()
        # e.exercise_13()
        # e.exercise_14()
        # e.exercise_15()
        # e.exercise_16()
        # e.exercise_17()
        # e.exercise_18()
        # e.exercise_19()
        # e.exercise_20()
        # e.exercise_21()
        # e.exercise_22()
        # e.exercise_23()
        # e.exercise_24()
        # e.exercise_25()
        # e.exercise_26()
        # e.exercise_27()
        # e.exercise_28()
        # e.exercise_29()
        e.exercise_30()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
