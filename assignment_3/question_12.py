# Question 12
# Write a Python program using functions that prompt the user to enter today's date (in the format YYYY-MM-DD) 
# and the current day of the week. Then, ask the user to input a number of days. The program should calculate 
# and display the new date and the day of the week after the specified number of days have passed.
#
# Input:
# - Today's date: 2024-08-27
# - Today's day: Tuesday
# - Number of days: 5
#
# Output:
# - New date: 2024-09-01
# - New day: Sunday

from datetime import datetime, timedelta

def calculate_future_date(date_str, current_day, days_to_add):
    # Parse the input date
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Calculate new date
    new_date = current_date + timedelta(days=days_to_add)
    
    # Get the new day of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    new_day = days_of_week[new_date.weekday()]
    
    return new_date.strftime("%Y-%m-%d"), new_day

# Test with the example
today_date = "2024-08-27"
today_day = "Tuesday"
num_days = 5

new_date, new_day = calculate_future_date(today_date, today_day, num_days)

print("Input:")
print(f"Today's date: {today_date}")
print(f"Today's day: {today_day}")
print(f"Number of days: {num_days}")
print("\nOutput:")
print(f"New date: {new_date}")
print(f"New day: {new_day}")
