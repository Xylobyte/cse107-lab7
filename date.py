"""
A program that prompts the user for a date then converts the date to day of the year

file: date.py

author: Donovan Griego

Date: 10-10-2021

assignment: Lab 7
"""

days = {"january": 31, "february": 28, "march": 31, "april": 30, "may": 31, "june": 30,
        "july": 31, "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}

months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]


def get_doy(string):
    """
    returns a tuple with element 1 being the day of the year and element 2 telling if its a leap year

    string: the unparsed string with month date and year
    """
    string = [x.lower().replace(",", "") for x in string.split(" ")]
    if len(string) != 3:
        print("Error; invalid number of arguments")
        exit(1)
    leap = is_leap(int(string[2]))
    total = int(string[1])
    try:
        index = months.index(string[0])
    except ValueError:
        print("Error; invalid month '{}'".format(string[0]))
        exit(1)
    if int(string[1]) > days[string[0]] or int(string[1]) <= 0:
        print("Error; invalid date entered")
        exit(1)
    for i in [months[e] for e in range(index)]:
        total += days[i]
        if i == "february":
            total += (1 if leap else 0)
    return (total, leap)


def is_leap(year):
    """
    returns if the year is a leap year or not

    year: year to check
    """
    year = int(year)
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def main():
    while True:
        print("Type stop or enter a month, day, and year.")
        string = input("> ")
        if string.strip() == "stop":
            break
        tp = get_doy(string)
        print("Day of the {}: {}".format(
            "leap year" if tp[1] else "year", tp[0]))


if __name__ == "__main__":
    main()


# def find_days(): months_and_days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31} months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] print("enter a month, day of the month, and year") inputdata = [indata.strip() for indata in input().split(',')] entered_month = inputdata[0] entered_day = int(inputdata[1]) entered_year = int(inputdata[2]) mon_feb = False is_leap = (entered_year % 4 == 0 and entered_year % 100 != 0) or entered_year % 400 == 0 if(months_and_days.get(entered_month, -1) == -1): return -1 elif(is_leap and entered_month.find("February") != -1): mon_feb = True if(entered_day > 29): return -1 elif((not mon_feb) and (months_and_days.get(entered_month, -1) < entered_day)): return -1 days = 0 for month in months: if(month.find(entered_month) == -1): days = days + months_and_days.get(month) if(is_leap and month == "February"): days = days + 1 else: days = days + entered_day break return days if __name__ == '__main__': days = find_days() print(days)
