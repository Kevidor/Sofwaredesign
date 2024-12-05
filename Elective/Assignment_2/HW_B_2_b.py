"""
Name: Holzmann Kevin
Date: 1 Dez 2024

Assigment:
Write a Python program that reads two integers representing a month and day, and prints the season for that month and day.

Expected Output:

Input the month (e.g., January, February, etc.): July  
Input the day: 31  
Season is autumn
"""

def determine_season(month: str, day: int) -> str:
    """Determine the season based on the given month and day.

    Args:
        month (str or int): The name of the month (e.g., "March") or its numeric value (e.g., 3).
        day (int): The day of the month.

    Returns:
        str: The season ("Winter", "Spring", "Summer", "Autumn") or "Invalid date" if input is invalid.
    """
    # The dict is used to convert a month in textform to an int 
    month_dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    # Convert the month to an int if vaild
    try:
        if isinstance(month, str) and month.isdigit():
            month = int(month)
        elif isinstance(month, str):
            month = month_dict.get(month.capitalize(), None)
            if month is None:
                print("ERROR: Invalid month name")
                return

        day = int(day)
    except:
        print("ERROR: Month must be of type int or str and Day must be of type int")
        return

    # Ckecks for a vaild day
    if not((month in [1, 3, 5, 7, 9, 11] and day in range(1, 32)) or 
           (month in [4, 6, 8, 10, 12] and day in range(1, 31)) or 
           (month == 2 and day in range(1, 29))): 
        print("ERROR: Invalid day")
        return

    # Return season based on the month and day
    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day < 21):
        return "Winter"
    elif (month == 3 and day >= 21) or (4 <= month <= 5) or (month == 6 and day < 21):
        return "Spring"
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 21):
        return "Summer"
    elif (month == 9 and day >= 21) or (10 <= month <= 11) or (month == 12 and day < 21):
        return "Autumn"
    else:
        return "Invalid date"
    
month = input("Give me a month (int or str): ")
day = input("Give me a day (int): ")

print(determine_season(month= month, day= day))
