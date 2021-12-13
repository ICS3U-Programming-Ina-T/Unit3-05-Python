#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Dec. 13, 2021
# This program asks the user for the month as a
# number between 1 and 12. It then displays the
# month as a string to the user.

# Returns the month in string format the given
# month. It is the switch case equivalent
def find_month(month):
    months = {
        1: "{} represents the month of January.". format(month),
        2: "{} represents the month of February.". format(month),
        3: "{} represents the month of March.". format(month),
        4: "{} represents the month of April.". format(month),
        5: "{} represents the month of May.". format(month),
        6: "{} represents the month of June.". format(month),
        7: "{} represents the month of July.". format(month),
        8: "{} represents the month of August.". format(month),
        9: "{} represents the month of September.". format(month),
        10: "{} represents the month of October.". format(month),
        11: "{} represents the month of November.". format(month),
        12: "{} represents the month of December.". format(month),
    }
    return months.get(month, "Error. {} does not represent a month.".
                      format(month))


if __name__ == "__main__":
    # displays the opening message:
    print("Today you will be told the month of the year")
    print("based on its numerical value!")
    print("")
    
    # collects the number of the month from the user
    user_month = int(input("Enter the number of a month "
                           "(i.e 1 for January): "))

    # prints the month associated with the number
    print(find_month(user_month))
