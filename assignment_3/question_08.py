# Question 8
# Write a Python program that takes the name of a month as input and returns the number of days in that month.
# Input: The name of the Month: February
# Output: No. of days: 28/29 days

def days_in_month(month_name):
    months = {
        "january": 31, "february": "28/29", "march": 31, "april": 30,
        "may": 31, "june": 30, "july": 31, "august": 31,
        "september": 30, "october": 31, "november": 30, "december": 31
    }
    
    month_name = month_name.lower()
    if month_name in months:
        return months[month_name]
    else:
        return "Invalid month name"

# Test
test_month = "February"
print(f"The name of the Month: {test_month}")
print(f"No. of days: {days_in_month(test_month)} days")
