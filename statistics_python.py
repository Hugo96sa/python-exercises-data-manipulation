# Hugo Solares

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

amir_deals_key = 'ami_dea'
food_consumption_key = 'foo_con'
restaurant_groups_key = 'res_gro'
world_happiness_key = 'wor_hap'

amir_deals_file_path = 'data/statistics_python/amir_deals.csv'
food_consumption_file_path = 'data/statistics_python/food_consumption.csv'
restaurant_groups_file_path = 'data/statistics_python/restaurant_groups.csv'
world_happiness_file_path = 'data/statistics_python/world_happiness.csv'


class Statistics:
    def __init__(self):
        self.df = {}

    def set_data(self, data_selector):
        try:
            if data_selector == amir_deals_key:
                return pd.read_csv(amir_deals_file_path)
            elif data_selector == food_consumption_key:
                return pd.read_csv(food_consumption_file_path)
            elif data_selector == restaurant_groups_key:
                return pd.read_csv(restaurant_groups_file_path, index_col=0)
            elif data_selector == world_happiness_key:
                return pd.read_csv(world_happiness_file_path, index_col=0)

            else:
                raise ValueError("Invalid data_selector provided.")

        except FileNotFoundError:
            print(f"Error: File not found for: '{data_selector}'.")
            self.df = None

        except pd.errors.ParserError:
            print(f"Error: Parsing issue for: '{data_selector}'.")
            self.df = None

    # Mean and median
    def exercise_1(self):
        food_consumption = self.set_data(food_consumption_key)

        # Filter for Belgium
        be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

        # Filter for USA
        usa_consumption = food_consumption[food_consumption['country'] == 'USA']

        # Calculate mean and median consumption in Belgium
        print(np.mean(be_consumption['consumption']))
        print(np.median(be_consumption['consumption']))

        # Calculate m)an and median consumption in USA
        print(np.mean(usa_consumption['consumption']))
        print(np.median(usa_consumption['consumption']))

        # Subset for Belgium and USA only
        be_and_usa = food_consumption[
            (food_consumption['country'] == 'Belgium') | (food_consumption['country'] == 'USA')]

        # Group by country, select consumption column, and compute mean and median
        print(be_and_usa.groupby('country')['consumption'].agg(['mean', 'median']))

    # Mean vs. Median
    def exercise_2(self):
        food_consumption = self.set_data(food_consumption_key)

        # Subset for food_category equals rice
        rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

        # Histogram of co2_emission for rice and show plot, it shows a right skewed graph
        rice_consumption.co2_emission.hist()
        plt.show()

        # Subset for food_category equals rice
        rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

        # Calculate mean and median of co2_emission with .agg(), in this case given the right-skewed data,
        # the measure of central tendency that best summarizes the data is median
        print(rice_consumption[['consumption', 'co2_emission']].agg(['mean', 'median']))

    # Quartiles, quintiles, deciles are all quantiles
    def exercise_3(self):
        food_consumption = self.set_data(food_consumption_key)

        # Calculate the quartiles of co2_emission
        print(np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1]))

        # Calculate the quintiles of co2_emission
        print(np.quantile(food_consumption['co2_emission'], [0, 0.2, 0.4, 0.6, 0.8, 1]))

        # Calculate the deciles of co2_emission
        print(np.quantile(food_consumption['co2_emission'], [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))

    # Variance and standard deviation
    def exercise_4(self):
        food_consumption = self.set_data(food_consumption_key)

        # Print variance and sd of co2_emission for each food_category
        print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

        # Create histogram of co2_emission for food_category 'beef'
        food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
        # Show plot
        plt.show()

        # Create histogram of co2_emission for food_category 'eggs'
        food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
        # Show plot
        plt.show()

    # Finding outliers using IQR
    def exercise_5(self):
        food_consumption = self.set_data(food_consumption_key)

        # Calculate total co2_emission per country: emissions_by_country
        emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
        print(emissions_by_country)

        # Compute the first and third quartiles and IQR of emissions_by_country
        q1 = np.quantile(emissions_by_country, 0.25)
        q3 = np.quantile(emissions_by_country, 0.75)
        iqr = q3 - q1

        # Calculate the lower and upper cutoffs for outliers
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        # Subset emissions_by_country to find outliers
        outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
        print(outliers)

    # plot co2 emissions vs food category and vs country
    def exercise_6(self):
        food_consumption = self.set_data(food_consumption_key)

        # Sort the DataFrame by 'food_category'
        food_consumption = food_consumption.sort_values(by='food_category')

        # Calculate and print the sum of 'co2_emission' for each category
        sum_co2_by_category = food_consumption.groupby('food_category')['co2_emission'].sum().reset_index()
        sum_co2_by_category = sum_co2_by_category.sort_values(by='co2_emission', ascending=False)
        print(sum_co2_by_category)

        # Calculate and print the sum of 'co2_emission' for each country
        food_consumption = food_consumption.sort_values(by='country')
        sum_co2_by_country = food_consumption.groupby('country')['co2_emission'].sum().reset_index()
        sum_co2_by_country = sum_co2_by_country.sort_values(by='co2_emission', ascending=False)
        print(sum_co2_by_country)

        # Plotting the bar chart
        plt.figure(figsize=(10, 6))  # Set the figure size
        plt.bar(sum_co2_by_category['food_category'], sum_co2_by_category['co2_emission'], color='skyblue')

        # Adding labels and title
        plt.xlabel('Food Category')
        plt.ylabel('Sum of CO2 Emission')
        plt.title('Sum of CO2 Emission by Food Category')

        # Rotating x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')

        # Display the plot
        plt.tight_layout()  # Adjust layout to prevent overlap of labels
        plt.show()

        plt.bar(sum_co2_by_country['country'], sum_co2_by_country['co2_emission'], color='blue')

        # Adding labels and title
        plt.xlabel('Country')
        plt.ylabel('Sum of CO2 Emission')
        plt.title('Sum of CO2 Emission by Country')

        # Rotating x-axis labels for better readability
        plt.xticks(rotation=90, ha='right')
        plt.show()

    # Calculate the probabilities
    def exercise_7(self):
        amir_deals = self.set_data(amir_deals_key)

        # Count the deals for each product
        counts = amir_deals['product'].value_counts()
        print(counts)

        # Calculate probability of picking a deal with each product
        probs = counts / amir_deals.shape[0]
        print(probs)

        # If you randomly select one of Amir's deals, what's the probability
        # that the deal will involve Product C?: 8.427%

    def exercise_8(self):
        amir_deals = self.set_data(amir_deals_key)

        # Set random seed
        np.random.seed(24)

        # Sample 5 deals without replacement
        sample_without_replacement = amir_deals.sample(5)
        print(sample_without_replacement)

        # Sample 5 deals with replacement
        sample_with_replacement = amir_deals.sample(5, replace=True)
        print(sample_with_replacement)

        # What type of sampling is better to use for this situation?
        # -> Without replacement

    def exercise_9(self):
        restaurant_groups = self.set_data(restaurant_groups_key)

        # Create a histogram of restaurant_groups and show plot
        restaurant_groups['group_size'].hist(bins=np.linspace(2,6,5))
        plt.show()

        # Create probability distribution
        size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]

        # Reset index and rename columns
        size_dist = size_dist.reset_index()
        size_dist.columns = ['group_size', 'prob']
        print(size_dist)

        # Calculate expected value
        expected_value = (size_dist['group_size'] * size_dist['prob']).sum()
        print(expected_value)

        # Subset groups of size 4 or more
        groups_4_or_more = size_dist[size_dist['group_size'] >= 4]

        # Sum the probabilities of groups_4_or_more
        prob_4_or_more = np.sum(groups_4_or_more['prob'])
        print(prob_4_or_more)


if __name__ == '__main__':
    try:
        s = Statistics()

        # s.exercise_1()
        # s.exercise_2()
        # s.exercise_3()
        # s.exercise_4()
        # s.exercise_5()
        # s.exercise_6()
        # s.exercise_7()
        # s.exercise_8()
        s.exercise_9()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
