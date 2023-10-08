import time
import calendar
import pandas as pd
# edit
# edit
# refactor
# refactor
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
monthsOfYear = {'January', 'February', 'March', 'April', 'May', 'June'}
daysOfWeek = {
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            'Please enter the name of the city you want to see data for (Chicago, New York, or Washington):\n') \
            .strip().lower()
        if city in CITY_DATA:
            print(f'You have selected: {city.capitalize()}. Processing...')
            break
        else:
            print('Invalid input.')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            'Please enter the month you want to see data for (all, january, february, ... , june):\n') \
            .strip().capitalize()
        if month in monthsOfYear or month == 'All':
            print(f'You have selected: {month}. Processing...')
            break
        else:
            print('Invalid input.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            'Please enter the day of week you want to see data for (all, monday, tuesday, ... sunday):\n') \
            .strip().capitalize()
        if day in daysOfWeek or day == 'All':
            print(f'You have selected: {day}. Processing...')
            break
        else:
            print('Invalid input.')

    print('-' * 40)
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
    print(f"Loading DataFrame for city: {city}, month: {month}, day of the week: {day}")
    filename = CITY_DATA.get(city)
    data = pd.read_csv(filename)
    data["Start Time"] = pd.to_datetime(data["Start Time"])

    """Filter data by month and day."""
    if month != "All":
        data = data[data["Start Time"].dt.strftime('%B') == month]
        print(f"Data loaded and filtered for the month: {month}.")

    if day != "All":
        data = data[data["Start Time"].dt.strftime('%A') == day]
        print(f"Data loaded and filtered for the day of week: {day}.")
    df = pd.DataFrame(data)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df["Month"] = df["Start Time"].dt.month
    month_counts = df["Month"].value_counts()
    most_common_month = month_counts.idxmax()
    print(f"The most common month is: {calendar.month_name[most_common_month]}")

    # display the most common day of week
    df["Day"] = df["Start Time"].dt.dayofweek
    day_counts = df["Day"].value_counts()
    most_common_day = day_counts.idxmax()
    print(f"The most common day of week is: {calendar.day_name[most_common_day]}")
    # display the most common start hour
    df["Hour"] = df["Start Time"].dt.hour
    hour_counts = df["Hour"].value_counts()
    most_common_hour = hour_counts.idxmax()
    print("The most common hour is:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_counts = df["Start Station"].value_counts()
    common_start_station = start_station_counts.idxmax()
    print("The most commonly used start station is:", common_start_station)
    # display most commonly used end station
    end_station_counts = df["End Station"].value_counts()
    common_end_station = end_station_counts.idxmax()
    print("The most commonly used end station is:", common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
    most_frequent = frequent_combination.loc[frequent_combination['count'].idxmax()]
    print(
        f"The most frequent combination start station is "
        f"start: {most_frequent['Start Station']} end: {most_frequent['End Station']}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_time} seconds")

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df["User Type"].value_counts()
    print(f"Counts of : {count_user_types}")

    # Display counts of gender
    if "Gender" in df.columns:
        count_user_gender = df["Gender"].value_counts()
        print(f"Counts of : {count_user_gender}")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_birth = int(df["Birth Year"].min())
        recent_birth = int(df["Birth Year"].max())
        common_birth_count = df["Birth Year"].value_counts()
        common_birth = int(common_birth_count.idxmax())

        print(f"Earliest year of birth: {earliest_birth}")
        print(f"Recent year of birth: {recent_birth}")
        print(f"Common year of birth: {common_birth}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    index = 0
    user_input = input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes', 'y', 'yep', 'yea'] and index + 5 < df.shape[0]:
        print(df.iloc[index:index + 5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
