import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 12:
        diff = datetime.date(year+1, 1, 1) - datetime.date(year, month, 1)
        return diff.days
    else:
    	diff = datetime.date(year, month+1, 1) - datetime.date(year, month,1)
    	return diff.days


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year >= 1 and year <=9999:
        if month >=1 and month <=12:
            if day >=1 and day <= days_in_month(year, month):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    if is_valid_date(year1, month1, day1) == False or is_valid_date(year2, month2, day2) == False:
        return 0
    elif year2 > year1:
        diff = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
        return diff.days
    elif year2 == year1:
        if month2 > month1:
            diff = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
            return diff.days
        elif month2 == month1:
            if day2 > day1:
                diff = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
                return diff.days
            else:
                return 0
        else:
            return 0
    else:
        return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day) == False:
        return 0
    elif datetime.date(year, month, day) > datetime.date.today():
        return 0
    else:
        age_in_days = datetime.date.today() - datetime.date(year, month, day)
        return age_in_days.days
