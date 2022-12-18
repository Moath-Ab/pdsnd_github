import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    CITIES = ['chicago', 'new york city', 'washington']
    print('Hello! Let\'s explore some US bikeshare data!')
    city=''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Enter city  you want to explore \n> ')
       city= city.lower()
       if city in CITIES:
           break
            
       city= city.lower()       
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month :")
        month= month.lower()
        if month in ['january', 'february', 'march', 'april', 'march', 'may', 'june', 'all']:
            break
        else:
            month = input("Please months is :january, february, march, april, march, may, june, all. choose one of them")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day you want to explore :")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            day = input("Please enter correct day . ")
            
    print('-'*40)
    return city, month, day





def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
        # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
        # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = month.index(month)
    
        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df.loc[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
        # TO DO: display the most common month
    mostCommonMonth= df['month'].mode()[0]
    print("Most commomn month is : ",mostCommonMonth)


    # TO DO: display the most common day of week
    mostCommonDay= df['day_of_week'].mode()[0]
    print("Most commomn day is : ", mostCommonDay)
    
    
        # TO DO: display the most common start hour
    mostCommonHour=df['hour'].mode()[0]
    print("Most commomn hour is : ", mostCommonHour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
        # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)


        # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)
    
    
        # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}" \
    .format(most_common_start_end_station[0], most_common_start_end_station[1]))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
        # TO DO: display total travel time
    totalTtravel = df['Trip Duration'].sum()
    print("Total travel time :", totalTtravel)
    
    
        # TO DO: display mean travel time
    meanTravel = df['Trip Duration'].mean()
    print("Mean travel time :", meanTravel)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
        # TO DO: Display counts of user types
    print("Counts of user types:\n")
    userCounts = df['User Type'].value_counts()
    
    if city == 'chicago' or city == 'new york city':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))

            
  

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth from the given fitered data is: {}\n'.format(earliest_birth))
        print('Most recent birth from the given fitered data is: {}\n'.format(most_recent_birth))
        print('Most common birth from the given fitered data is: {}\n'.format(most_common_birth) )
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
