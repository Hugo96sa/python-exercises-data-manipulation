# Hugo Solares

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

actors_movies_key = 'act_mov'
albums_key = 'albums'
artists_key = 'artists'
bac_key = 'bac'
business_owners_key = 'bus_own'
casts_key = 'casts'
census_altered_key = 'cen_alt'
census_key = 'census'
classic_18_key = 'cla_18'
classic_19_key = 'cla_19'
crews_key = 'crews'
cta_calendar_key = 'cta_cal'
cta_ridership_key = 'cta_rid'
dji_key = 'dji'
employees_key = 'employees'
financials_key = 'financials'
gdp_2_key = 'gdp_2'
gdp_key = 'gdp'
genres_key = 'genres'
inflation_2_key = 'inflation_2'
inflation_key = 'inflation'
inv_aug_key = 'inv_aug'
inv_jul_key = 'inv_jul'
inv_sep_key = 'inv_sep'
jpm_key = 'jpm_sep'
land_use_key = 'lan_use'
licenses_key = 'licenses'
movie_to_genres_key = 'mov_gen'
movies_key = 'movies'
non_mus_key = 'non_mus'
pop_18_key = 'pop_18'
pop_19_key = 'pop_19'
pop_key = 'pop'
ratings_key = 'ratings'
recession_key = 'recession'
sp500_key = 'sp500'
sequels_key = 'sequels'
social_fin_key = 'soc_fin'
stations_key = 'stations'
taglines_key = 'taglines'
taxi_owners_key = 'tax_own'
taxi_vehicles_key = 'tax_veh'
ten_yr_key = 'ten_yr'
top_cust_key = 'top_cst'
top_invoices_key = 'top_inv'
tracks_master_key = 'trk_mas'
tracks_ride_key = 'trk_rid'
tracks_st_key = 'trk_st'
unemployment_key = 'unemployment'
ur_wide_key = 'ur_wide'
ward_key = 'ward'
wards_altered_key = 'war_alt'
wells_key = 'wells'
world_bank_gdp_key = 'wor_bnk_gdp'
world_bank_pop_key = 'wor_bnk_pop'
zip_demo_key = 'zip_demo'

base_file_path = 'data/pandas_joining/'
actors_movies_file_path = f'{base_file_path}actors_movies.csv'
albums_file_path = f'{base_file_path}albums.csv'
artists_file_path = f'{base_file_path}artists.csv'
bac_file_path = f'{base_file_path}bac.csv'
business_owners_file_path = f'{base_file_path}business_owners.p'
casts_file_path = f'{base_file_path}casts.p'
census_altered_file_path = f'{base_file_path}census_altered.csv'
census_file_path = f'{base_file_path}census.p'
classic_18_file_path = f'{base_file_path}classic_18.csv'
classic_19_file_path = f'{base_file_path}classic_19.csv'
crews_file_path = f'{base_file_path}crews.p'
cta_calendar_file_path = f'{base_file_path}cta_calendar.p'
cta_ridership_file_path = f'{base_file_path}cta_ridership.p'
dji_file_path = f'{base_file_path}dji.csv'
employees_file_path = f'{base_file_path}employees.csv'
financials_file_path = f'{base_file_path}financials.p'
genres_file_path = f'{base_file_path}genres.csv'
gdp_2_file_path = f'{base_file_path}gdp_2.csv'
gdp_file_path = f'{base_file_path}gdp.csv'
inflation_2_file_path = f'{base_file_path}inflation_2.csv'
inflation_file_path = f'{base_file_path}inflation.csv'
inv_aug_file_path = f'{base_file_path}inv_aug.csv'
inv_jul_file_path = f'{base_file_path}inv_jul.csv'
inv_sep_file_path = f'{base_file_path}inv_sep.csv'
jpm_file_path = f'{base_file_path}jpm.csv'
land_use_file_path = f'{base_file_path}land_use.p'
licenses_file_path = f'{base_file_path}licenses.p'
movie_to_genres_file_path = f'{base_file_path}movie_to_genres.p'
movies_file_path = f'{base_file_path}movies.p'
non_mus_file_path = f'{base_file_path}non_mus_tcks.csv'
pop_18_file_path = f'{base_file_path}pop_18.csv'
pop_19_file_path = f'{base_file_path}pop_19.csv'
pop_file_path = f'{base_file_path}pop.csv'
ratings_file_path = f'{base_file_path}ratings.p'
recession_file_path = f'{base_file_path}recession.csv'
sp500_file_path = f'{base_file_path}S&P500.csv'
sequels_file_path = f'{base_file_path}sequels.p'
social_fin_file_path = f'{base_file_path}social_fin.csv'
stations_file_path = f'{base_file_path}stations.p'
taglines_file_path = f'{base_file_path}taglines.p'
taxi_owners_file_path = f'{base_file_path}taxi_owners.p'
taxi_vehicles_file_path = f'{base_file_path}taxi_vehicles.p'
ten_yr_file_path = f'{base_file_path}ten_yr.csv'
top_cust_file_path = f'{base_file_path}top_cust.csv'
top_invoices_file_path = f'{base_file_path}top_invoices.csv'
tracks_master_file_path = f'{base_file_path}tracks_master.csv'
tracks_ride_file_path = f'{base_file_path}tracks_ride.csv'
tracks_st_file_path = f'{base_file_path}tracks_st.csv'
unemployment_file_path = f'{base_file_path}unemployment.csv'
ur_wide_file_path = f'{base_file_path}ur_wide.csv'
ward_file_path = f'{base_file_path}ward.p'
wards_altered_file_path = f'{base_file_path}wards_altered.csv'
wells_file_path = f'{base_file_path}wells.csv'
world_bank_gdp_file_path = f'{base_file_path}WorldBank_GDP.csv'
world_bank_pop_file_path = f'{base_file_path}WorldBank_POP.csv'
zip_demo_file_path = f'{base_file_path}zip_demo.p'


class Joining:
    def __init__(self):
        self.df = {}

    def set_data(self, data_selector):
        try:
            if data_selector == actors_movies_key:
                return pd.read_csv(actors_movies_file_path)
            elif data_selector == albums_key:
                return pd.read_csv(albums_file_path, index_col=0)
            elif data_selector == artists_key:
                return pd.read_csv(artists_file_path, index_col=0)
            elif data_selector == bac_key:
                return pd.read_csv(bac_file_path, index_col=0)
            elif data_selector == business_owners_key:
                return pd.read_pickle(business_owners_file_path)
            elif data_selector == casts_key:
                return pd.read_pickle(casts_file_path)
            elif data_selector == census_altered_key:
                return pd.read_csv(census_altered_file_path, index_col=0)
            elif data_selector == census_key:
                return pd.read_pickle(census_file_path)
            elif data_selector == classic_18_key:
                return pd.read_csv(classic_18_file_path, index_col=0)
            elif data_selector == classic_19_key:
                return pd.read_csv(classic_19_file_path, index_col=0)
            elif data_selector == crews_key:
                return pd.read_pickle(crews_file_path)
            elif data_selector == cta_calendar_key:
                return pd.read_pickle(cta_calendar_file_path)
            elif data_selector == cta_ridership_key:
                return pd.read_pickle(cta_ridership_file_path)
            elif data_selector == dji_key:
                return pd.read_csv(dji_file_path, index_col=0)
            elif data_selector == employees_key:
                return pd.read_csv(employees_file_path, index_col=0)
            elif data_selector == financials_key:
                return pd.read_pickle(financials_file_path)
            elif data_selector == genres_key:
                return pd.read_csv(genres_file_path, index_col=0)
            elif data_selector == gdp_2_key:
                return pd.read_csv(gdp_2_file_path, index_col=0)
            elif data_selector == gdp_key:
                return pd.read_csv(gdp_file_path, index_col=0)
            elif data_selector == inflation_2_key:
                return pd.read_csv(inflation_2_file_path, index_col=0)
            elif data_selector == inflation_key:
                return pd.read_csv(inflation_file_path, index_col=0)
            elif data_selector == inv_aug_key:
                return pd.read_csv(inv_aug_file_path, index_col=0)
            elif data_selector == inv_jul_key:
                return pd.read_csv(inv_jul_file_path, index_col=0)
            elif data_selector == inv_sep_key:
                return pd.read_csv(inv_sep_file_path, index_col=0)
            elif data_selector == jpm_key:
                return pd.read_csv(jpm_file_path, index_col=0)
            elif data_selector == land_use_key:
                return pd.read_pickle(land_use_file_path)
            elif data_selector == licenses_key:
                return pd.read_pickle(licenses_file_path)
            elif data_selector == movie_to_genres_key:
                return pd.read_pickle(movie_to_genres_file_path)
            elif data_selector == movies_key:
                return pd.read_pickle(movies_file_path)
            elif data_selector == non_mus_key:
                return pd.read_csv(non_mus_file_path, index_col=0)
            elif data_selector == pop_18_key:
                return pd.read_csv(pop_18_file_path, index_col=0)
            elif data_selector == pop_19_key:
                return pd.read_csv(pop_19_file_path, index_col=0)
            elif data_selector == pop_key:
                return pd.read_csv(pop_file_path, index_col=0)
            elif data_selector == ratings_key:
                return pd.read_pickle(ratings_file_path)
            elif data_selector == recession_key:
                return pd.read_csv(recession_file_path, index_col=0)
            elif data_selector == sp500_key:
                return pd.read_csv(sp500_file_path)
            elif data_selector == sequels_key:
                return pd.read_pickle(sequels_file_path)
            elif data_selector == social_fin_key:
                return pd.read_csv(social_fin_file_path, index_col=0)
            elif data_selector == stations_key:
                return pd.read_pickle(stations_file_path)
            elif data_selector == taglines_key:
                return pd.read_pickle(taglines_file_path)
            elif data_selector == taxi_owners_key:
                return pd.read_pickle(taxi_owners_file_path)
            elif data_selector == taxi_vehicles_key:
                return pd.read_pickle(taxi_vehicles_file_path)
            elif data_selector == ten_yr_key:
                return pd.read_csv(ten_yr_file_path, index_col=0)
            elif data_selector == top_cust_key:
                return pd.read_csv(top_cust_file_path, index_col=0)
            elif data_selector == top_invoices_key:
                return pd.read_csv(top_invoices_file_path, index_col=0)
            elif data_selector == tracks_master_key:
                return pd.read_csv(tracks_master_file_path, index_col=0)
            elif data_selector == tracks_ride_key:
                return pd.read_csv(tracks_ride_file_path, index_col=0)
            elif data_selector == tracks_st_key:
                return pd.read_csv(tracks_st_file_path, index_col=0)
            elif data_selector == unemployment_key:
                return pd.read_csv(unemployment_file_path, index_col=0)
            elif data_selector == ur_wide_key:
                return pd.read_csv(ur_wide_file_path, index_col=0)
            elif data_selector == ward_key:
                return pd.read_pickle(ward_file_path)
            elif data_selector == wards_altered_key:
                return pd.read_csv(wards_altered_file_path, index_col=0)
            elif data_selector == wells_key:
                return pd.read_csv(wells_file_path, index_col=0)
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

    # One to many merge in multiple tables, Find the best location in the city to put your goat farm
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

    # Left joins
    def exercise_8(self):
        movies = self.set_data(movies_key)
        financials = self.set_data(financials_key)
        print(movies.head(), movies.shape)
        print(financials.head(), financials.shape)

        # Merge movies and financials with a left join
        movies_financials = movies.merge(financials, on='id', how='left')
        print(movies_financials.head())

        # Count the number of rows in the budget column that are missing
        number_of_missing_fin = movies_financials['budget'].isnull().sum()

        # Print the number of movies missing financials
        print(number_of_missing_fin)

    # Enriching the dataset
    def exercise_9(self):
        movies = self.set_data(movies_key)
        taglines = self.set_data(taglines_key)
        toy_story = movies[movies['title'].isin(['Toy Story', 'Toy Story 2', 'Toy Story 3'])]

        if toy_story.empty:
            print("No Toy Story movies found.")
            return  # Exit the method if no Toy Story movies are found

        # Merge the toy_story DF and taglines tables with a left join
        toystory_tag = toy_story.merge(taglines, on='id', how='left')

        # Print the rows and shape of toystory_tag
        print(toystory_tag)
        print(toystory_tag.shape)

        # Merge the toy_story DF and taglines tables with inner join, notice that nulls are lost
        toystory_tag = toy_story.merge(taglines, on='id')

        # Print the rows and shape of toystory_tag
        print(toystory_tag)
        print(toystory_tag.shape)

    # Left join, one to one and one to many
    def exercise_10(self):
        movies = self.set_data(movies_key)
        left_table = movies[movies['title'].isin(
            ['Jurassic Park', 'The Lost World: Jurassic Park', 'Jurassic World', 'Jurassic Park III'])]
        one_to_one = self.set_data(taglines_key)
        one_to_many = self.set_data(crews_key)
        print(left_table.head(), left_table.shape)
        print(one_to_one.head(), one_to_one.shape)
        print(one_to_many.head(), one_to_many.shape)

        # The output of a one-to-many merge with a left join will have greater than or equal rows than the left table.
        print(left_table.merge(one_to_one, on='id', how='left').shape)
        print(left_table.merge(one_to_many, on='id', how='left').shape)

    # Right joins
    def exercise_11(self):
        movies_genres = self.set_data(movie_to_genres_key)
        movies = self.set_data(movies_key)
        action_movies = movies_genres[movies_genres['genre'].isin(['Action'])]
        scifi_movies = movies_genres[movies_genres['genre'].isin(['Science Fiction'])]

        # Some movies have more than 1 genre
        print(movies_genres[movies_genres['movie_id'] == 18])

        # Merge action_movies to scifi_movies with right join, add suffixes
        action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                           suffixes=('_act', '_sci'))

        # Print the first few rows of action_scifi to see the structure
        print(action_scifi.head())

        # From action_scifi, select only the rows where the genre_act column is null
        scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

        # Merge the movies and scifi_only tables with an inner join
        movies_and_scifi_only = movies.merge(scifi_only, left_on='id', right_on='movie_id')

        # Print the first few rows and shape of movies_and_scifi_only
        print(movies_and_scifi_only.head())
        print(movies_and_scifi_only.shape)

    # Popular genres with right join, first find the top 10 most popular genres in movies, then join by id and count
    # plot the result with matplotlib
    def exercise_12(self):
        movie_to_genres = self.set_data(movie_to_genres_key)
        movies = self.set_data(movies_key)
        pop_movies = movies.sort_values('popularity', ascending=False).head(10)  # select the top 10

        # Use right join to merge the movie_to_genres and pop_movies tables
        genres_movies = movie_to_genres.merge(pop_movies, how='right', left_on='movie_id', right_on='id')

        # Count the number of genres
        genre_count = genres_movies.groupby('genre').agg({'id': 'count'})

        # Sort genre_count in descending order based on the count of movies
        genre_count = genre_count.sort_values(by='id', ascending=False)
        print(genre_count)

        # Plot with matplotlib a bar chart of the genre_count
        genre_count.plot(kind='bar', rot=45)
        plt.xlabel('Genre')
        plt.ylabel('Number of Movies')
        plt.title('Number of Movies per Genre for Top 10 Popular Movies')
        plt.show()

    # Popular genres with right join, first find the top 10 most popular genres in movies, then join by id and count
    # plot the result with seaborn
    def exercise_13(self):
        movie_to_genres = self.set_data(movie_to_genres_key)
        movies = self.set_data(movies_key)
        pop_movies = movies.sort_values('popularity', ascending=False).head(10)  # select the top 10

        # Use right join to merge the movie_to_genres and pop_movies tables
        genres_movies = movie_to_genres.merge(pop_movies, how='right', left_on='movie_id', right_on='id')

        # Count the number of genres
        genre_count = genres_movies.groupby('genre').agg({'id': 'count'})

        # Sort genre_count in descending order based on the count of movies
        genre_count = genre_count.sort_values(by='id', ascending=False).reset_index()
        print(genre_count)

        # Plot using Seaborn
        plt.figure(figsize=(10, 6))
        sns.barplot(x='genre', y='id', data=genre_count, palette='viridis')
        plt.xlabel('Genre')
        plt.ylabel('Number of Movies')
        plt.title('Number of Movies per Genre for Top 10 Popular Movies')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()  # Adjust layout to prevent overlapping labels
        plt.show()

    # Popular genres with right join, first find the top 10 most popular genres in movies, then join by id and count
    # plot the result with plotly
    def exercise_14(self):
        movie_to_genres = self.set_data(movie_to_genres_key)
        movies = self.set_data(movies_key)
        pop_movies = movies.sort_values('popularity', ascending=False).head(10)  # select the top 10

        # Use right join to merge the movie_to_genres and pop_movies tables
        genres_movies = movie_to_genres.merge(pop_movies, how='right', left_on='movie_id', right_on='id')

        # Count the number of genres
        genre_count = genres_movies.groupby('genre').agg({'id': 'count'})

        # Sort genre_count in descending order based on the count of movies
        genre_count = genre_count.sort_values(by='id', ascending=False).reset_index()
        print(genre_count)

        # Plot using Plotly
        fig = px.bar(genre_count, x='genre', y='id', labels={'genre': 'Genre', 'id': 'Number of Movies'},
                     title='Number of Movies per Genre for Top 10 Popular Movies',
                     color='genre', color_discrete_sequence=px.colors.qualitative.Plotly)

        fig.update_layout(xaxis_title='Genre', yaxis_title='Number of Movies',
                          title='Number of Movies per Genre for Top 10 Popular Movies')
        fig.show()

    # Perform an outer join
    def exercise_15(self):
        movies = self.set_data(movies_key)
        casts = self.set_data(casts_key)
        iron_man_id = movies['id'][movies['title'].isin(['Iron Man'])].values[0]
        iron_man_2_id = movies['id'][movies['title'].isin(['Iron Man 2'])].values[0]

        iron_1_actors = casts[casts['movie_id'] == iron_man_id][['character', 'id', 'name']]
        iron_2_actors = casts[casts['movie_id'] == iron_man_2_id][['character', 'id', 'name']]
        print(casts)
        # Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
        iron_1_and_2 = iron_1_actors.merge(iron_2_actors, on='id', how='outer', suffixes=('_1', '_2'))

        # Create an index that returns true if name_1 or name_2 are null
        m = iron_1_and_2['name_1'].isnull() | iron_1_and_2['name_2'].isnull()

        # Print the first few rows of iron_1_and_2
        print(iron_1_and_2[m].head())

    # Make a self in crews
    def exercise_16(self):
        crews = self.set_data(crews_key)

        # Merge the crews table to itself
        crews_self_merged = crews.merge(crews, on='id', how='inner', suffixes=('_dir', '_crew'))

        # Create a Boolean index to select the appropriate
        boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & (crews_self_merged['job_crew'] != 'Director'))
        direct_crews = crews_self_merged[boolean_filter]

        # Print the first few rows of direct_crews
        print(direct_crews.head())

    # Merge movies and ratings on the index
    def exercise_17(self):
        movies = self.set_data(movies_key)
        ratings = self.set_data(ratings_key)

        # Merge to the movies table the ratings table on the index
        movies_ratings = movies.merge(ratings, on='id', how='left')

        # Print the first few rows of movies_ratings
        print(movies_ratings.head())

    # Find if sequels make more money than originals
    def exercise_18(self):
        sequels = self.set_data(sequels_key).set_index('id')
        financials = self.set_data(financials_key).set_index('id')

        # Merge sequels and financials on index id
        sequels_fin = sequels.merge(financials, on='id', how='left')

        # Self merge with suffixes as inner join with left on sequel and right on id
        orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                                     right_on='id', right_index=True, suffixes=('_org', '_seq'))

        # Add calculation to subtract revenue_org from revenue_seq 
        orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

        # Select the title_org, title_seq, and diff 
        titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

        # Print the first rows of the sorted titles_diff
        print(titles_diff.sort_values('diff', ascending=False).head())

    # Perform an anti-join following the 3 main steps
    def exercise_19(self):
        employees = self.set_data(employees_key)
        top_cust = self.set_data(top_cust_key)

        # Merge employees and top_cust
        empl_cust = employees.merge(top_cust, on='srid', how='left', indicator=True)

        # Select the srid column where _merge is left_only
        srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

        # Get employees not working with top customers
        print(employees[employees['srid'].isin(srid_list)])

    # Perform a semi-join
    def exercise_20(self):
        non_mus_tcks = self.set_data(non_mus_key)
        top_invoices = self.set_data(top_invoices_key)
        genres = self.set_data(genres_key)

        # Merge the non_mus_tck and top_invoices tables on tid
        tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

        # Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
        top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

        # Group the top_tracks by gid and count the tid rows
        cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid': 'count'})

        # Merge the genres table to cnt_by_gid on gid and print
        print(cnt_by_gid.merge(genres, on='gid'))

    # Concatenate multiple DF
    def exercise_21(self):
        tracks_master = self.set_data(tracks_master_key)
        tracks_ride = self.set_data(tracks_ride_key)
        tracks_st = self.set_data(tracks_st_key)

        # Concatenate the tracks
        tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], sort=True)
        print(tracks_from_albums)

        # Concatenate the tracks so the index goes from 0 to n-1
        tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], ignore_index=True, sort=True)
        print(tracks_from_albums)

        # Concatenate the tracks, show only columns names that are in all tables
        tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], join='inner', ignore_index=True,
                                       sort=True)
        print(tracks_from_albums)

    # Concatenate using keys
    def exercise_22(self):
        inv_jul = self.set_data(inv_jul_key)
        inv_aug = self.set_data(inv_aug_key)
        inv_sep = self.set_data(inv_sep_key)

        # Concatenate the tables and add keys
        inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep],
                                    keys=['7Jul', '8Aug', '9Sep'])

        # Group the invoices by the index keys and find avg of the total column
        avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total': 'mean'})

        # Bar plot of avg_inv_by_month
        avg_inv_by_month.plot(kind='bar')
        plt.show()

    # Validate the merge before, spot the error
    def exercise_23(self):
        artists = self.set_data(artists_key)
        albums = self.set_data(albums_key)

        print(artists.merge(albums, on='artid', validate='many_to_one'))

    # Concatenate and merge to fing common songs
    def exercise_24(self):
        classic_18 = self.set_data(classic_18_key)
        classic_19 = self.set_data(classic_19_key)
        pop_18 = self.set_data(pop_18_key)
        pop_19 = self.set_data(pop_19_key)

        # Concatenate the classic tables vertically
        classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

        # Concatenate the pop tables vertically
        pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

        # Merge classic_18_19 with pop_18_19
        classic_pop = classic_18_19.merge(pop_18_19, on='tid')

        # Using .isin(), filter classic_18_19 rows where tid is in classic_pop
        popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

        # Print popular chart
        print(popular_classic)

    # Practice renaming, what is the correlation between gdp and sp500?
    def exercise_25(self):
        gdp = self.set_data(world_bank_gdp_key)
        sp500 = self.set_data(sp500_key)

        gdp = gdp[gdp['Country Code'].isin(['USA'])]
        gdp = gdp[['Country Code', 'Year', 'GDP']]
        gdp = gdp.rename(columns={'Country Code': 'country code', 'Year': 'year', 'GDP': 'gdp'})
        sp500 = sp500.rename(columns={'Date': 'date', 'Returns': 'returns'})

        # Use merge_ordered() to merge gdp and sp500 on year and date
        gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', how='left')

        # Print gdp_sp500
        print(gdp_sp500)

        # Use merge_ordered() to merge gdp and sp500, interpolate missing value
        gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', how='left', fill_method='ffill')

        # Print gdp_sp500
        print(gdp_sp500)

        # Subset the gdp and returns columns
        gdp_returns = gdp_sp500[['gdp', 'returns']]

        # Print gdp_returns correlation
        print(gdp_returns.corr())

    # Perform a Phillips curve with merge_ordered()
    def exercise_26(self):
        inflation = self.set_data(inflation_key)
        unemployment = self.set_data(unemployment_key)

        # Use merge_ordered() to merge inflation, unemployment with inner join
        inflation_unemploy = pd.merge_ordered(inflation, unemployment,
                                              on='date', how='inner')

        # Print inflation_unemploy 
        print(inflation_unemploy)

        # Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
        inflation_unemploy.plot(kind='scatter', x='unemployment_rate', y='cpi')
        plt.show()

    def exercise_27(self):
        gdp = self.set_data(gdp_key)
        pop = self.set_data(pop_key)

        # Merge gdp and pop on date and country with fill and notice rows 2 and 3
        ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'], fill_method='ffill')

        # Print ctry_date
        print(ctry_date)

        # Merge gdp and pop on country and date with fill
        date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'], fill_method='ffill')

        # Print date_ctry
        print(date_ctry)

    def exercise_28(self):
        jpm = self.set_data(jpm_key)
        wells = self.set_data(wells_key)
        bac = self.set_data(bac_key)
        jpm['date_time'] = pd.to_datetime(jpm['date_time'])
        wells['date_time'] = pd.to_datetime(wells['date_time'])
        bac['date_time'] = pd.to_datetime(bac['date_time'])

        # Use merge_asof() to merge jpm and wells
        jpm_wells = pd.merge_asof(jpm, wells, on='date_time',
                                  suffixes=('', '_wells'), direction='nearest')

        # Use merge_asof() to merge jpm_wells and bac
        jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time',
                                      suffixes=('_jpm', '_bac'), direction='nearest')

        # Compute price diff
        price_diffs = jpm_wells_bac.diff()

        # Plot the price diff of the close of jpm, wells and bac only
        price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
        plt.show()

    def exercise_29(self):
        gdp = self.set_data(gdp_2_key)
        recession = self.set_data(recession_key)
        gdp['date'] = pd.to_datetime(gdp['date'])
        recession['date'] = pd.to_datetime(recession['date'])

        # Merge gdp and recession on date using merge_asof()
        gdp_recession = pd.merge_asof(gdp, recession, on='date')

        # Create a list based on the row value of gdp_recession['econ_status']
        is_recession = ['r' if s == 'recession' else 'g' for s in gdp_recession['econ_status']]

        # Plot a bar chart of gdp_recession
        gdp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90)
        plt.show()

    def exercise_30(self):
        social_fin = self.set_data(social_fin_key)

        # False, There 2 rows where the value is greater than $50,000,000K.
        print(social_fin.query('value > 50000000'))

        # False, There are 3 rows for total revenue for Facebook.
        print(social_fin.query('financial == "total_revenue" and company == "facebook"'))

        # True, There are 6 rows where the net income has a negative value.
        print(social_fin.query('financial == "net_income" and value < 0'))

        # False, social_fin.query('financial == "gross_profit" and value > 100')
        print(social_fin.query('financial == "gross_profit" and value > 100'))

    def exercise_31(self):
        gdp = self.set_data(gdp_key)
        pop = self.set_data(pop_key)

        # Merge gdp and pop on date and country with fill
        gdp_pop = pd.merge_ordered(gdp, pop, on=['country', 'date'], fill_method='ffill')

        # Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
        gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

        # Pivot table of gdp_per_capita, where index is date and columns is country
        gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

        # Select dates equal to or greater than 1991-01-01
        recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

        # Plot recent_gdp_pop
        recent_gdp_pop.plot(rot=90)
        plt.show()

    def exercise_32(self):
        inflation = self.set_data(inflation_2_key)

        print(inflation.melt(id_vars=['country', 'indicator'], var_name='year', value_name='annual'))

    def exercise_33(self):
        ur_wide = self.set_data(ur_wide_key)

        # unpivot everything besides the year column
        ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')

        # Create a date column using the month and year columns of ur_tall
        ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'].astype(str), format='%b-%Y')

        # Sort ur_tall by date in ascending order
        ur_sorted = ur_tall.sort_values('date')

        # Plot the unempl_rate by date
        ur_sorted.plot(x='date', y='unempl_rate')
        plt.show()

    def exercise_34(self):
        ten_yr = self.set_data(ten_yr_key)
        dji = self.set_data(dji_key)

        # Use melt on ten_yr, unpivot everything besides the metric column
        bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

        # Use query on bond_perc to select only the rows where metric=close
        bond_perc_close = bond_perc.query('metric == "close"')

        # Merge (ordered) dji and bond_perc_close on date with an inner join
        dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date',
                                    suffixes=('_dow', '_bond'), how='inner')

        # Plot only the close_dow and close_bond columns
        dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
        plt.show()


if __name__ == '__main__':
    try:
        j = Joining()

        # j.exercise_1()
        # j.exercise_2()
        # j.exercise_3()
        # j.exercise_4()
        # j.exercise_5()
        # j.exercise_6()
        # j.exercise_7()
        # j.exercise_8()
        # j.exercise_9()
        # j.exercise_10()
        # j.exercise_11()
        # j.exercise_12()
        # j.exercise_13()
        # j.exercise_14()
        # j.exercise_15()
        # j.exercise_16()
        # j.exercise_17()
        # j.exercise_18()
        # j.exercise_19()
        # j.exercise_20()
        # j.exercise_21()
        # j.exercise_22()
        # j.exercise_23() # Stops execution
        # j.exercise_24()
        # j.exercise_25()
        # j.exercise_26()
        # j.exercise_27()
        # j.exercise_28()
        # j.exercise_29()
        # j.exercise_30()
        # j.exercise_31()
        # j.exercise_32()
        # j.exercise_33()
        j.exercise_34()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
