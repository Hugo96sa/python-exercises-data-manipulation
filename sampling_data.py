import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

attrition_key = 'attrition'
coffee_ratings_key = 'cof_rat'
spotify_key = 'spotify'

base_file_path = 'data/sampling_data/'
attrition_file_path = f'{base_file_path}attrition.feather'
coffee_ratings_file_path = f'{base_file_path}coffee_ratings_full.feather'
spotify_file_path = f'{base_file_path}spotify_2000_2020.feather'


class Sampling:
    def set_data(self, data_selector):
        try:
            if data_selector == attrition_key:
                return pd.read_feather(attrition_file_path)
            elif data_selector == coffee_ratings_key:
                return pd.read_feather(coffee_ratings_file_path)
            elif data_selector == spotify_key:
                return pd.read_feather(spotify_file_path)
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

    def exercise_1(self):
        spotify_population = self.set_data(spotify_key)

        # Sample 1000 rows from spotify_population
        spotify_sample = spotify_population.sample(n=1000)

        # Print the sample
        print(spotify_sample)

        # Calculate the mean duration in mins from spotify_population
        mean_dur_pop = spotify_population['duration_minutes'].mean()

        # Calculate the mean duration in mins from spotify_sample
        mean_dur_samp = spotify_sample['duration_minutes'].mean()

        # Print the means
        print(mean_dur_pop)
        print(mean_dur_samp)

    def exercise_2(self):
        spotify_population = self.set_data(spotify_key)

        # Create a pandas Series from the loudness column of spotify_population
        loudness_pop = spotify_population['loudness']

        # Sample 100 values of loudness_pop
        loudness_samp = loudness_pop.sample(n=100)

        # Calculate the mean of loudness_pop
        mean_loudness_pop = loudness_pop.mean()

        # Calculate the mean of loudness_samp
        mean_loudness_samp = loudness_samp.mean()

        print(mean_loudness_pop)
        print(mean_loudness_samp)

    def exercise_3(self):
        spotify_population = self.set_data(spotify_key)

        # Update the histogram to use spotify_mysterious_sample
        spotify_population['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))
        plt.show()

        spotify_mysterious_sample = spotify_population[spotify_population['acousticness'] > 0.950]

        # Update the histogram to use spotify_mysterious_sample
        spotify_mysterious_sample['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))
        plt.show()

    def exercise_4(self):
        spotify_population = self.set_data(spotify_key)

        # Visualize the distribution of duration_minutes as a histogram
        spotify_population['duration_minutes'].hist(bins=np.arange(0, 15.5, 0.5))
        plt.show()

        spotify_mysterious_sample2 = spotify_population.sample(n=50)

        # Visualize the distribution of duration_minutes as a histogram
        spotify_mysterious_sample2['duration_minutes'].hist(bins=np.arange(0, 15.5, 0.5))
        plt.show()

    def exercise_5(self):
        # Generate random numbers from a Uniform(-3, 3)
        uniforms = np.random.uniform(low=-3, high=3, size=5000)

        # Print uniforms
        print(uniforms)

        # Plot a histogram of uniform values, binwidth 0.25
        plt.hist(uniforms, bins=np.arange(-3, 3.25, 0.25))
        plt.show()

        # Generate random numbers from a Normal(5, 2)
        normals = np.random.normal(loc=5, scale=2, size=5000)

        # Print normals
        print(normals)

        # Plot a histogram of normal values, binwidth 0.5
        plt.hist(normals, np.arange(-2, 13.5, 0.5))
        plt.show()

    def exercise_6(self):
        # The values of x are different from those of y.
        np.random.seed(123)
        x = np.random.normal(size=5)
        print(x)
        y = np.random.normal(size=5)
        print(y)

        # x and y have identical values.
        np.random.seed(123)
        x = np.random.normal(size=5)
        print(x)
        np.random.seed(123)
        y = np.random.normal(size=5)
        print(y)

        # The values of x are different from those of y.
        np.random.seed(123)
        x = np.random.normal(size=5)
        print(x)
        np.random.seed(456)
        y = np.random.normal(size=5)
        print(y)

    # Random sample
    def exercise_7(self):
        attrition_pop = self.set_data(attrition_key)

        # Sample 70 rows using simple random sampling and set the seed
        attrition_samp = attrition_pop.sample(n=70, random_state=18900217)

        # Print the sample
        print(attrition_samp)

    # Systematically sample the data, if data is not sorted
    def exercise_8(self):
        attrition_pop = self.set_data(attrition_key)

        # Set the sample size to 70
        sample_size = 70

        # Calculate the population size from attrition_pop
        pop_size = len(attrition_pop)

        # Calculate the interval
        interval = pop_size // sample_size

        # Systematically sample 70 rows
        attrition_sys_samp = attrition_pop.iloc[::interval]

        # Print the sample
        print(attrition_sys_samp)

    def exercise_9(self):
        attrition_pop = self.set_data(attrition_key)

        # Add an index column to attrition_pop
        attrition_pop_id = attrition_pop.reset_index()

        # Plot YearsAtCompany vs. index for attrition_pop_id
        attrition_pop_id.plot(x='index', y='YearsAtCompany', kind='scatter')
        plt.show()

        # Shuffle the rows of attrition_pop
        attrition_shuffled = attrition_pop.sample(frac=1)

        # Reset the row indexes and create an index column
        attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()

        # Plot YearsAtCompany vs. index for attrition_shuffled
        attrition_shuffled.plot(x='index', y='YearsAtCompany', kind='scatter')
        plt.show()

    def exercise_10(self):
        attrition_pop = self.set_data(attrition_key)

        # Proportion of employees by Education level
        education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

        # Print education_counts_pop
        print(education_counts_pop)

        # Proportional stratified sampling for 40% of each Education group
        attrition_strat = attrition_pop.groupby('Education', observed=False).sample(frac=0.4, random_state=2022)

        # Calculate the Education level proportions from attrition_strat
        education_counts_strat = attrition_strat['Education'].value_counts(normalize=True)

        # Print education_counts_strat
        print(education_counts_strat)

    def exercise_11(self):
        attrition_pop = self.set_data(attrition_key)

        # Get 30 employees from each Education group
        attrition_eq = attrition_pop.groupby('Education', observed=False).sample(n=30, random_state=2022)

        # Get the proportions from attrition_eq
        education_counts_eq = attrition_eq['Education'].value_counts(normalize=True)

        # Print the results
        print(education_counts_eq)


if __name__ == '__main__':
    try:
        s = Sampling()

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
        s.exercise_11()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
