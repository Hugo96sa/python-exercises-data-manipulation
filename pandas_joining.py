# Hugo Solares

import pandas as pd
import matplotlib.pyplot as plt

actors_movies_key = 'act_mov'
business_owners_key = 'bus_own'
casts_key = 'casts'
census_key = 'census'
census_altered_key = 'cen_alt'
crews_key = 'crews'
cta_calendar_key = 'cta_cal'
cta_ridership_key = 'cta_rider'
financials_key = 'financials'
land_use_key = 'lan_use'
licenses_key = 'licenses'
movie_to_genres_key = 'mov_gen'
movies_key = 'movies'
ratings_key = 'ratings'
sp500_key = 'sp500'
sequels_key = 'sequels'
stations_key = 'stations'
taglines_key = 'taglines'
taxi_owners_key = 'tax_own'
taxi_vehicles_key = 'tax_veh'
ward_key = 'ward'
wards_altered_key = 'war_alt'
world_bank_gdp_key = 'wor_bnk_gdp'
world_bank_pop_key = 'wor_bnk_pop'
zip_demo_key = 'zip_demo'

actors_movies_file_path = 'data/pandas_joining/actors_movies.csv'
business_owners_file_path = 'data/pandas_joining/business_owners.p'
casts_file_path = 'data/pandas_joining/casts.p'
census_file_path = 'data/pandas_joining/census.p'
census_altered_file_path = 'data/pandas_joining/census_altered.csv'
crews_file_path = 'data/pandas_joining/crews.p'
cta_calendar_file_path = 'data/pandas_joining/cta_calendar.p'
cta_ridership_file_path = 'data/pandas_joining/cta_ridership.p'
financials_file_path = 'data/pandas_joining/financials.p'
land_use_file_path = 'data/pandas_joining/land_use.p'
licenses_file_path = 'data/pandas_joining/licenses.p'
movie_to_genres_file_path = 'data/pandas_joining/movie_to_genres.p'
movies_file_path = 'data/pandas_joining/movies.p'
ratings_file_path = 'data/pandas_joining/ratings.p'
sp500_file_path = 'data/pandas_joining/S&P500.csv'
sequels_file_path = 'data/pandas_joining/sequels.p'
stations_file_path = 'data/pandas_joining/stations.p'
taglines_file_path = 'data/pandas_joining/taglines.p'
taxi_owners_file_path = 'data/pandas_joining/taxi_owners.p'
taxi_vehicles_file_path = 'data/pandas_joining/taxi_vehicles.p'
ward_file_path = 'data/pandas_joining/ward.p'
wards_altered_file_path = 'data/pandas_joining/wards_altered.csv'
world_bank_gdp_file_path = 'data/pandas_joining/WorldBank_GDP.csv'
world_bank_pop_file_path = 'data/pandas_joining/WorldBank_POP.csv'
zip_demo_file_path = 'data/pandas_joining/zip_demo.p'


class Joining:
    def __init__(self):
        self.df = {}

    def set_data(self, data_selector):
        try:
            if data_selector == actors_movies_key:
                return pd.read_csv(actors_movies_file_path)
            elif data_selector == business_owners_key:
                return pd.read_pickle(business_owners_file_path)
            elif data_selector == casts_key:
                return pd.read_pickle(casts_file_path)
            elif data_selector == census_key:
                return pd.read_pickle(census_file_path)
            elif data_selector == census_altered_key:
                return pd.read_csv(census_altered_file_path, index_col=0)
            elif data_selector == crews_key:
                return pd.read_pickle(crews_file_path)
            elif data_selector == cta_calendar_key:
                return pd.read_pickle(cta_calendar_file_path)
            elif data_selector == cta_ridership_key:
                return pd.read_pickle(cta_ridership_file_path)
            elif data_selector == financials_key:
                return pd.read_pickle(financials_file_path)
            elif data_selector == land_use_key:
                return pd.read_pickle(land_use_file_path)
            elif data_selector == licenses_key:
                return pd.read_pickle(licenses_file_path)
            elif data_selector == movie_to_genres_key:
                return pd.read_pickle(movie_to_genres_file_path)
            elif data_selector == movies_key:
                return pd.read_pickle(movies_file_path)
            elif data_selector == ratings_key:
                return pd.read_pickle(ratings_file_path)
            elif data_selector == sp500_key:
                return pd.read_csv(sp500_file_path)
            elif data_selector == sequels_key:
                return pd.read_pickle(sequels_file_path)
            elif data_selector == stations_key:
                return pd.read_pickle(stations_file_path)
            elif data_selector == taglines_key:
                return pd.read_pickle(taglines_file_path)
            elif data_selector == taxi_owners_key:
                return pd.read_pickle(taxi_owners_file_path)
            elif data_selector == taxi_vehicles_key:
                return pd.read_pickle(taxi_vehicles_file_path)
            elif data_selector == ward_key:
                return pd.read_pickle(ward_file_path)
            elif data_selector == wards_altered_key:
                return pd.read_csv(wards_altered_file_path, index_col=0)
            elif data_selector == world_bank_gdp_key:
                return pd.read_csv(world_bank_gdp_file_path)
            elif data_selector == world_bank_pop_key:
                return pd.read_csv(world_bank_pop_file_path)
            elif data_selector == zip_demo_key:
                return pd.read_pickle(zip_demo_file_path)
            else:
                raise ValueError("Invalid data_selector provided.")

        except FileNotFoundError:
            print(f"Error: File not found for: '{data_selector}'.")
            self.df = None

        except pd.errors.ParserError:
            print(f"Error: Parsing issue for: '{data_selector}'.")
            self.df = None

    # Explore the taxi DF, in which column should both taxi DFs join?
    def exercise_1(self):
        # Load the data
        taxi_owners = self.set_data(taxi_owners_key)
        taxi_vehicles = self.set_data(taxi_vehicles_key)

        # After exploring both tables have 'vid' column, we should join here
        print(taxi_owners.head())
        print(taxi_owners.info())
        print(taxi_vehicles.head())
        print(taxi_vehicles.info())

    # Inner join
    def exercise_2(self):
        taxi_owners = self.set_data(taxi_owners_key)
        taxi_veh = self.set_data(taxi_vehicles_key)

        # Merge the taxi_owners and taxi_veh tables
        taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')

        # Print the column names of the taxi_own_veh
        print(taxi_own_veh.columns)
        print(taxi_own_veh.head())

        # Merge the taxi_owners and taxi_veh tables setting a suffix
        taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))

        # Print the column names of taxi_own_veh
        print(taxi_own_veh.columns)
        print(taxi_own_veh.head())

        # Merge the taxi_owners and taxi_veh tables setting a suffix
        taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))

        # Print the value_counts to find the most popular fuel_type
        print(taxi_own_veh['fuel_type'].value_counts())

    # Inner joins, merging data on a column
    def exercise_3(self):
        wards = self.set_data(ward_key)
        census = self.set_data(census_key)
        wards_altered = self.set_data(wards_altered_key)
        census_altered = self.set_data(census_altered_key)

        wards['ward'] = pd.to_numeric(wards['ward'])
        census['ward'] = pd.to_numeric(census['ward'])

        # Merge the wards and census tables on the ward column
        wards_census = wards.merge(census, on='ward')

        # Print the shape of wards_census
        print('wards_census table shape:', wards_census.shape)

        # Print the first few rows of the wards_altered table to view the change 
        print(wards_altered[['ward']].head())

        # Merge the wards_altered and census tables on the ward column
        wards_altered_census = wards_altered.merge(census, on='ward')

        # Print the shape of wards_altered_census
        print('wards_altered_census table shape:', wards_altered_census.shape)

        # Print the first few rows of the census_altered table to view the change 
        print(census_altered[['ward']].head())

        # Merge the wards and census_altered tables on the ward column
        wards_census_altered = wards.merge(census_altered, on='ward')

        # Print the shape of wards_census_altered
        print('wards_census_altered table shape:', wards_census_altered.shape)

    # One to many merge, use the relationship one to many to merge different DF using one column in common
    def exercise_4(self):
        licenses = self.set_data(licenses_key)
        biz_owners = self.set_data(business_owners_key)
        print(licenses.head())
        print(biz_owners.head())

        # Merge the licenses and biz_owners table on account
        licenses_owners = licenses.merge(biz_owners, on="account")

        # Group the results by title then count the number of accounts
        counted_df = licenses_owners.groupby('title').agg({'account': 'count'})

        # Sort the counted_df in descending order
        sorted_df = counted_df.sort_values('account', ascending=False)

        # Use .head() method to print the first few rows of sorted_df
        print(sorted_df.head())

    # Total riders in a month with a given filtering criteria
    def exercise_5(self):
        ridership = self.set_data(cta_ridership_key)
        cal = self.set_data(cta_calendar_key)
        stations = self.set_data(stations_key)
        print(ridership.head(), ridership.shape)
        print(cal.head(), cal.shape)
        print(stations.head(), stations.shape)

        # Merge the ridership and cal tables
        ridership_cal = ridership.merge(cal, on=['year', 'month', 'day'])
        print(ridership_cal.head())

        # Merge the ridership, cal, and stations tables
        ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
            .merge(stations, on='station_id')
        print(ridership_cal_stations.head())

        # Create a filter to filter ridership_cal_stations
        filter_criteria = ((ridership_cal_stations['month'] == 7)
                           & (ridership_cal_stations['day_type'] == 'Weekday')
                           & (ridership_cal_stations['station_name'] == 'Wilson'))

        # Use .loc and the filter to select for rides
        print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

    # Three tables merge, Find median income of alderman by merging licenses and zip demo first
    # then merging the result with wards
    def exercise_6(self):
        licenses = self.set_data(licenses_key)
        zip_demo = self.set_data(zip_demo_key)
        wards = self.set_data(ward_key)
        print(licenses.head(), licenses.shape)
        print(zip_demo.head(), zip_demo.shape)
        print(wards.head(), wards.shape)

        # Merge licenses and zip_demo, on zip; and merge the wards on ward
        licenses_zip_ward = licenses.merge(zip_demo, on='zip').merge(wards, on='ward')

        # Print the results by alderman and show median income
        print(licenses_zip_ward.groupby('alderman').agg({'income': 'median'}))

    # One to many merge in multople tables, Find the best location in the city to put your goat farm
    # with a great deal of space and relatively few businesses and people around to avoid complaints
    def exercise_7(self):
        land_use = self.set_data(land_use_key)
        census = self.set_data(census_key)
        licenses = self.set_data(licenses_key)
        print(land_use.head(), land_use.shape)
        print(census.head(), census.shape)
        print(licenses.head(), licenses.shape)

        # Merge land_use and census and merge result with licenses including suffixes 
        land_cen_lic = land_use.merge(census, on='ward') \
            .merge(licenses, on='ward', suffixes=('_cen', '_lic'))
        print(land_cen_lic.head())

        # Group by ward, pop_2010, and vacant, then count the # of accounts
        pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'],
                                           as_index=False).agg({'account': 'count'})

        # Sort pop_vac_lic and print the results
        sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'],
                                                     ascending=[False, True, True])

        # Print the top few rows of sorted_pop_vac_lic
        print(sorted_pop_vac_lic.head())


if __name__ == '__main__':
    try:
        j = Joining()

        # j.exercise_1()
        # j.exercise_2()
        # j.exercise_3()
        # j.exercise_4()
        # j.exercise_5()
        # j.exercise_6()
        j.exercise_7()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
