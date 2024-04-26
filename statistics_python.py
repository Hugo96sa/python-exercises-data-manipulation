# Hugo Solares

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import expon

amir_deals_key = 'ami_dea'
all_deals_key = 'all_dea'
food_consumption_key = 'foo_con'
restaurant_groups_key = 'res_gro'
world_happiness_key = 'wor_hap'

base_file_path = 'data/statistics_python/'
amir_deals_file_path = f'{base_file_path}amir_deals.csv'
all_deals_file_path = f'{base_file_path}all_deals.csv'
food_consumption_file_path = f'{base_file_path}food_consumption.csv'
restaurant_groups_file_path = f'{base_file_path}restaurant_groups.csv'
world_happiness_file_path = f'{base_file_path}world_happiness.csv'
world_happiness_2_file_path = f'{base_file_path}world_happiness2.csv'

class Statistics:
    def __init__(self):
        self.df = {}

    def set_data(self, data_selector):
        try:
            if data_selector == amir_deals_key:
                return pd.read_csv(amir_deals_file_path)
            elif data_selector == all_deals_key:
                return pd.read_csv(all_deals_file_path, index_col=0)
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
        restaurant_groups['group_size'].hist(bins=np.linspace(2, 6, 5))
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

    def exercise_10(self):
        # Min and max wait times for back-up that happens every 30 min
        min_time = 0
        max_time = 30

        # Calculate probability of waiting less than 5 mins
        prob_less_than_5 = uniform.cdf(5, min_time, max_time)
        print(prob_less_than_5)

        # Calculate probability of waiting more than 5 mins
        prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time)
        print(prob_greater_than_5)

        # Calculate probability of waiting 10-20 mins
        prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)
        print(prob_between_10_and_20)

    def exercise_11(self):
        # Set random seed to 334
        np.random.seed(334)

        # Generate 1000 wait times between 0 and 30 mins
        wait_times = uniform.rvs(0, 30, size=1000)

        print(wait_times)

        # Create a histogram of simulated times and show plot
        plt.hist(wait_times)
        plt.show()

    def exercise_12(self):
        # Set random seed to 10
        np.random.seed(10)

        # Simulate a single deal
        print(binom.rvs(1, 0.3, size=1))

        # Simulate 1 week of 3 deals
        print(binom.rvs(3, 0.3, size=1))

        # Simulate 52 weeks of 3 deals
        deals = binom.rvs(3, 0.3, size=52)

        # Print mean deals won per week
        print(np.mean(deals))

    def exercise_13(self):
        # Probability of closing 3 out of 3 deals
        prob_3 = binom.pmf(3, 3, 0.3)
        print(prob_3)

        # Probability of closing <= 1 deal out of 3 deals
        prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)
        print(prob_less_than_or_equal_1)

        # Probability of closing > 1 deal out of 3 deals
        prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)
        print(prob_greater_than_1)

    def exercise_14(self):
        # Expected number won with 30% win rate
        won_30pct = 3 * 0.3
        print(won_30pct)

        # Expected number won with 25% win rate
        won_25pct = 3 * 0.25
        print(won_25pct)

        # Expected number won with 35% win rate
        won_35pct = 3 * 0.35
        print(won_35pct)

    def exercise_15(self):
        amir_deals = self.set_data(amir_deals_key)

        # Histogram of amount with 10 bins and show plot
        amir_deals['amount'].hist(bins=10)
        plt.show()

    def exercise_16(self):
        # Probability of deal < 7500
        prob_less_7500 = norm.cdf(7500, 5000, 2000)
        print(prob_less_7500)

        # Probability of deal > 1000
        prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)
        print(prob_over_1000)

        # Probability of deal between 3000 and 7000
        prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)
        print(prob_3000_to_7000)

        # Calculate amount that 25% of deals will be less than
        pct_25 = norm.ppf(0.25, 5000, 2000)
        print(pct_25)

    def exercise_17(self):
        # Calculate new average amount
        new_mean = 5000 * 1.2

        # Calculate new standard deviation
        new_sd = 2000 * 1.3

        # Simulate 36 new sales
        new_sales = norm.rvs(new_mean, new_sd, size=36)

        # Create histogram and show
        plt.hist(new_sales)
        plt.show()

    # Which market is better?
    def exercise_18(self):
        # Based only on the metric of percent of sales over $1000, does Amir perform better
        # in the current market or the predicted market?
        print(1 - norm.cdf(1000, 5000, 2000))
        print(1 - norm.cdf(1000, 6000, 2600))
        # Amir performs about equally in both markets.

    # Central limit theorem in action
    def exercise_19(self):
        amir_deals = self.set_data(amir_deals_key)

        # Create a histogram of num_users and show
        amir_deals['num_users'].hist()
        plt.show()

        # Set seed to 104
        np.random.seed(104)

        # Sample 20 num_users with replacement
        samp_20 = amir_deals['num_users'].sample(20, replace=True)

        # Take mean of samp_20
        print(np.mean(samp_20))

        sample_means = []

        # Loop 100 times
        for i in range(100):
            # Take samples of 20 num_users with replacement
            samp_20 = amir_deals['num_users'].sample(20, replace=True)
            # Calculate mean of samp_20
            samp_20_mean = np.mean(samp_20)
            # Append samp_20_mean to sample_means
            sample_means.append(samp_20_mean)

        print(sample_means)

        # Convert to Series and plot histogram
        sample_means_series = pd.Series(sample_means)
        sample_means_series.hist()
        # Show plot
        plt.show()

    # Mean of means
    def exercise_20(self):
        all_deals = self.set_data(all_deals_key)
        amir_deals = self.set_data(amir_deals_key)

        # Set seed to 321
        np.random.seed(321)

        sample_means = []
        # Loop 30 times to take 30 means
        for i in range(30):
            # Take sample of size 20 from num_users col of all_deals with replacement
            cur_sample = all_deals['num_users'].sample(20, replace=True)
            # Take mean of cur_sample
            cur_mean = np.mean(cur_sample)
            # Append cur_mean to sample_means
            sample_means.append(cur_mean)

        # Print mean of sample_means
        print(np.mean(sample_means))

        # Print mean of num_users in amir_deals
        print(np.mean(amir_deals['num_users']))

    # Poisson distribution
    def exercise_21(self):
        # Probability of 5 responses
        prob_5 = poisson.pmf(5, 4)

        print(prob_5)

        # Probability of 5 responses
        prob_coworker = poisson.pmf(5, 5.5)

        print(prob_coworker)

        # Probability of 2 or fewer responses
        prob_2_or_less = poisson.cdf(2, 4)

        print(prob_2_or_less)

        # Probability of > 10 responses
        prob_over_10 = 1 - poisson.cdf(10, 4)

        print(prob_over_10)

    # Exponencial distribution
    def exercise_22(self):
        # Print probability response takes < 1 hour
        print(expon.cdf(1, scale=2.5))

        # Print probability response takes > 4 hours
        print(1 - expon.cdf(4, scale=2.5))

        # Print probability response takes 3-4 hours
        print(expon.cdf(3, scale=2.5) - expon.cdf(4, scale=2.5))

    # Linear correlation and plots
    def exercise_23(self):
        world_happiness = self.set_data(world_happiness_key)

        # Create a scatterplot of happiness_score vs. life_exp and show
        sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)
        plt.show()

        # Create a hexbin plot
        sns.jointplot(x='life_exp', y='happiness_score', data=world_happiness, kind='hex', color='orange')
        plt.show()

        # Create scatterplot of happiness_score vs life_exp with trendline
        sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)
        plt.show()

        # Based on the scatterplot, which is most likely the correlation between life_exp and happiness_score? = 0.8

        # Correlation between life_exp and happiness_score
        cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])
        print(cor)

    # Fix the correlation with the use of np.log
    def exercise_24(self):
        world_happiness = self.set_data(world_happiness_key)

        # Scatterplot of gdp_per_cap and life_exp
        sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)
        plt.show()

        # Correlation between gdp_per_cap and life_exp
        cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])
        print(cor)

        # Create log_gdp_per_cap column
        world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

        # Fixxing the Scatterplot of gdp_per_cap and life_exp
        sns.scatterplot(x='log_gdp_per_cap', y='life_exp', data=world_happiness)
        plt.show()

        # Fixxing the Correlation between gdp_per_cap and life_exp with log_gdp_per_cap
        cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['life_exp'])
        print(cor)

    # Transforming variables
    def exercise_25(self):
        world_happiness = self.set_data(world_happiness_key)

        # Scatterplot of happiness_score vs. gdp_per_cap
        sns.scatterplot(x='gdp_per_cap', y='happiness_score', data=world_happiness)
        plt.show()

        # Calculate correlation
        cor = world_happiness['gdp_per_cap'].corr(world_happiness['happiness_score'])
        print(cor)

        # Create log_gdp_per_cap column
        world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

        # Scatterplot of happiness_score vs. log_gdp_per_cap
        sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
        plt.show()

        # Calculate correlation
        cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
        print(cor)
    
    # Does sugar improve happiness?, an effort was made to merge 2 different csv files so we are
    # working with the most data possible
    def exercise_26(self):
        world_happiness = self.set_data(world_happiness_key)

        # Scatterplot of grams_sugar_per_day and happiness_score
        sns.scatterplot(x='grams_sugar_per_day', y='happiness_score', data=world_happiness)
        plt.show()

        # Correlation between grams_sugar_per_day and happiness_score
        cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
        print(cor)

        # Which statement about sugar consumption and happiness scores is true?
        # Increased sugar consumption is associated with a higher happiness score.


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
        # s.exercise_9()
        # s.exercise_10()
        # s.exercise_11()
        # s.exercise_12()
        # s.exercise_13()
        # s.exercise_14()
        # s.exercise_15()
        # s.exercise_16()
        # s.exercise_17()
        # s.exercise_18()
        # s.exercise_19()
        # s.exercise_20()
        # s.exercise_21()
        # s.exercise_22()
        # s.exercise_23()
        # s.exercise_24()
        # s.exercise_25()
        s.exercise_26()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
