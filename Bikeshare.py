import pandas as pd
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        city = input('Please enter the name of the city you\'d like to analyze\n').lower()
        if city.lower() == 'chicago' or city == 'new york' or city == 'washington':
            print('Carrying on ..\n')
            break
        else:
            print('You\'ve entered an invalid value. Please type either chicago, new york or washington\n')
    # TO DO: get user input for month (all, january, february, ... , june)
    while 1:
        months_names = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input('Please enter the name of the month you\'d like to go through\nIf you\'d like to go through all the of the months please type "all"\n').lower()
        if month.lower() in months_names:
            print('Carrying on ..\n')
            break
        else:
            print('You\'ve entered an invalid value. Please type the name of the month correctly')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
            weekday_names = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'all']
            day = input('Please enter the name of the weekday you\'d like to go through. If you\'d like to go through all the of the weekdays please type "all"\n').lower()
            if day in weekday_names:
                print('Carrying on ..\n')
                break
            else:
                print('You\'ve entered an invalid value. Please type the name of the weekday correctly')


    print('-'*40)
    x = city
    return city, month, day

x = get_filters()

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

myframe = load_data(x[0], x[1], x[2])

#The next section will be dedicated to prompting the user to show parts of the dataframe

while 1:
    prompt = input('would you like to see some data? Type "yes" to display and "no" to keep going\nAnswer: ').lower()
    if prompt != 'yes' and prompt != 'no':
        while prompt != 'yes' and prompt != 'no':
            prompt = input('Please enter a valid answer. Would you like to see some data? Type "yes" to display data and "no" to keep going: ')
    if prompt == 'yes':
        finish = 5
        answer = 'yes'
        while answer == 'yes':
            if finish > len(myframe):
                start = finish - 5
                print(myframe.iloc[start:len(myframe),:])
                print('\n Sorry, you\'ve reached the end of the data')
                prompt = input('would you like to restart? Type yes to restart and no to continue\nAnswer: ')
                while prompt != 'yes' and prompt != 'no':
                    prompt = input('Please enter a valid answer. Would you like to see some data? Type "yes" to display data and "no" to keep going: ')
                break

            if finish == len(myframe):
                start = finish - 5
                print(myframe.iloc[start:finish,:])
                print('\n Sorry , this was all the data!')
                prompt = input('would you like to restart? Type yes to restart and no to continue\nAnswer: ')
                while prompt != 'yes' and prompt != 'no':
                    prompt = input('Please enter a valid answer. Would you like to see some data? Type "yes" to display data and "no" to keep going: ')
                break

            if finish < len(myframe):
                start = finish - 5
                print(myframe.iloc[start:finish,:])
                answer = input('would you like to see some more date? Type "yes" to continue and "no" to stop: ').lower()
                if answer == 'yes':
                    finish += 5
                    continue
                if answer == 'no':
                    prompt = 'no'
                    break

    if prompt == 'no':
        break



def time_stats(city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    df = pd.read_csv(CITY_DATA[city])

    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month\

    common_month = df['Start Time'].dt.month_name().mode()[0]
    print('The most common month for travelling in {} is {}\n'.format(x[0], common_month))
    # TO DO: display the most common day of week
    common_weekday = df['Start Time'].dt.day_name().mode()[0]
    print('The most common weekday for travelling in {} is {}\n'.format(x[0], common_weekday))


    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour for travelling in {} is {}\n'.format(x[0], common_hour))


    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    df = pd.read_csv(CITY_DATA[city])

    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common starting station is {}\n'.format(common_start_station))
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common ending station is {}\n'.format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['Combination'].mode()[0]
    print('The most common combination of a starting station and an ending one is {}\n'.format(common_combination))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # TO DO: display total travel time

    duration = df['End Time'] - df['Start Time']
    print('The total time travelled by all bikers is {}\n'.format(duration.sum()))
    # TO DO: display mean travel time
    print('The average amount of time each biker travels  is {}\n'.format(duration.mean()))


    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def user_stats(city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    df = pd.read_csv(CITY_DATA[city])
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('The number of subscribers is {} and the number of customers is {}\n'.format(user_count['Subscriber'], user_count['Customer']))

    # TO DO: Display counts of gender
    if city == 'chicago' or city == 'new york city':
        gender_count = df['Gender'].value_counts()
        print('The number of males is {} and the number of females is {}\n'.format(user_count['Male'], user_count['Female']))
        # TO DO: Display earliest, most recent, and most common year of birth
        min_birth_year = df['Birth Year'].min()
        max_birth_year = df['Birth Year'].max()
        mode_birth_year = df['Birth Year'].mode()
        print('The earlist birth year is {}\n'.format(min_birth_year))
        print('The most recent birth year is {}\n'.format(max_birth_year))
        print('The most common birth year is {}\n'.format(mode_birth_year))

    if city == 'washington':
        print('Gender and birth year are not available in washington')


    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)










time_stats(x[0])
station_stats(x[0])
trip_duration_stats(x[0])
