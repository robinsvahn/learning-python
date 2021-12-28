import datetime
import calendar

chosen_year = -1
chosen_number = -1
close_program = False


def welcomeUserToProgram():
    print("""Welcome to my awesome program, using this program you can 
figure out how many dates, in a defined year, using the format
yy.mm.dd add up to a defined sum when adding all digits together
    """)
    input("Press Enter to continue...")


def isAValidYear(number: str) -> bool:
    if(number.isnumeric() and len(number) < 5):
        return True
    return False


def askUserForSettings():
    print()  # Add a blank line for styling

    global chosen_year
    global chosen_number

    chosen_year = input(
        "For which year would you like to make the calculation: ")
    while(not isAValidYear(chosen_year)):
        chosen_year = input(
            f"The input {chosen_year} is not valid, please enter a valid year, ex '2021': ")

    chosen_number = input("What sum should the program check for: ")
    while(not chosen_number.isnumeric()):
        chosen_number = input(
            f"The input {chosen_number} is not valid, please enter a number, ex '7': ")

    chosen_year = int(chosen_year)
    chosen_number = int(chosen_number)
    print(f"You have chosen the year {chosen_year} and sum {chosen_number}")


def getFirstDateOfYear(year: int) -> datetime:
    return datetime.datetime(year, 1, 1)


def getSumOfLastTwoDigitsFromString(text: str) -> int:
    if(len(text) > 1):
        return (int(text[-1]) + int(text[-2]))
    else:
        return (int(text[-1]))


def getAllMatchingDates(year: int, number: int) -> list:
    matching_dates = []
    sum_of_year_digits = getSumOfLastTwoDigitsFromString(str(year))
    sum_of_month_digits = 0
    sum_of_day_digits = 0
    first_date_of_year = getFirstDateOfYear(year)
    print(first_date_of_year)

    while(first_date_of_year.year != year + 1):
        sum_of_month_digits = getSumOfLastTwoDigitsFromString(
            str(first_date_of_year.month))
        sum_of_day_digits = getSumOfLastTwoDigitsFromString(
            str(first_date_of_year.day))

        if(sum_of_year_digits+sum_of_month_digits+sum_of_day_digits is number):
            matching_dates.append(first_date_of_year)

        first_date_of_year += datetime.timedelta(days=1)

    return matching_dates


def printDatesFromList(dates: list):
    print()  # Add a blank line for styling
    print(
        f"In the year {chosen_year} the following dates add up to the sum {chosen_number}:")
    for date in dates:
        print(date)


def printOddsForMatchingDates(matching_dates: list):
    print()  # Add a blank line for styling
    days_in_year = 365
    if(calendar.isleap(chosen_year)):
        days_in_year = 366

    probability_of_a_matching_date = len(matching_dates)/days_in_year

    print(f"Amount of matching dates: {len(matching_dates)}")
    print(
        f"Probability for a date to be a match is: {probability_of_a_matching_date*100:.2f}%")


# Start of program
while (not close_program):
    welcomeUserToProgram()
    askUserForSettings()
    matching_dates = getAllMatchingDates(chosen_year, chosen_number)
    printDatesFromList(matching_dates)
    printOddsForMatchingDates(matching_dates)

    print()  # Add a blank line for styling
    close_program = True

    user_choice = input(
        "If you would like to rerun the program, write y, or press enter to close it: ")
    if(user_choice.lower() == "y".lower()):
        close_program = False
        print()  # Add a blank line for styling
        print("Restarting program...")
        print()  # Add a blank line for styling
