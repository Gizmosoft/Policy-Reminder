import json
from datetime import date

def date_strip(date):
    if __name__ == '__date_strip__':
        date_strip()

    # this functions takes in a string and strips it into different components
    day = date.split('/')[0]
    month = date.split('/')[1]
    year = date.split('/')[2]

    return int(day), int(month), int(year)

def get_current_date():
    if __name__ == '__get_current_date__':
        get_current_date()

    today = date.today()
    # convert date to string and then send it to the date_strip function
    today = today.strftime("%d/%m/%Y")
    today_format = date_strip(today)
    # returns tuple
    return today_format


def calculate_delta(json_object):
    if __name__ == '__calculate_delta__':
        calculate_delta()

    # call get_current_date() to get today's date in tuple -> (Day, Month, Year)
    current_date = get_current_date()

    #put the maturity date elements in a tuple
    maturity_date = date_strip(json_object['Maturity Date'])

    # calucalate delta value
    d1 = date(maturity_date[2], maturity_date[1], maturity_date[0])
    d0 = date(current_date[2], current_date[1], current_date[0])

    delta = d1-d0
    return delta.days
