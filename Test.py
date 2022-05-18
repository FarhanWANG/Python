
def CalculateDaysBetweenDates():
    print("This program calculates the number of days between two dates.")

    # get user input for the start and end date
    start_date = input("Enter a starting date (YYYY-MM-DD): ")
    end_date = input("Enter an ending date (YYYY-MM-DD): ")
    
    # convert the dates to datetime objects
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    # calculate the number of days between the dates
    num_days = (end_date - start_date).days

    # display the result
    print("There are {} days between {} and {}.".format(num_days, start_date, end_date))
