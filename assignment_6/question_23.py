# Question 23
# Perform the following tasks using the pandas DataFrame object:
# (a) Create a DataFrame named temperatures from a dictionary of three temperature readings 
#     each for 'Maxine', 'James', and 'Amanda'.
# (b) Recreate the DataFrame temperatures in Part (a) with custom indices using the index 
#     keyword argument and a list containing 'Morning', 'Afternoon', and 'Evening'.
# (c) Select from temperatures the column of temperature readings for 'Maxine'.
# (d) Select from temperatures the row of 'Morning' temperature readings.
# (e) Select from temperatures the rows for 'Morning' and 'Evening' temperature readings.
# (f) Select from temperatures the columns of temperature readings for 'Amanda' and 'Maxine'.
# (g) Select from temperatures the elements for 'Amanda' and 'Maxine' in the 'Morning' and 'Afternoon'.
# (h) Use the describe method to produce temperatures' descriptive statistics.
# (i) Transpose temperatures.
# (j) Sort temperatures so that its column names are in alphabetical order.

import pandas as pd

# (a) Create a DataFrame from a dictionary
print("(a) DataFrame 'temperatures' from dictionary:")
temp_dict = {
    'Maxine': [30, 35, 28],
    'James': [32, 38, 29],
    'Amanda': [28, 33, 27]
}
temperatures = pd.DataFrame(temp_dict)
print(temperatures)
print()

# (b) Recreate with custom indices
print("(b) DataFrame with custom indices:")
temperatures = pd.DataFrame(temp_dict, index=['Morning', 'Afternoon', 'Evening'])
print(temperatures)
print()

# (c) Select column for 'Maxine'
print("(c) Column of temperature readings for 'Maxine':")
print(temperatures['Maxine'])
print()

# (d) Select row of 'Morning' temperature readings
print("(d) Row of 'Morning' temperature readings:")
print(temperatures.loc['Morning'])
print()

# (e) Select rows for 'Morning' and 'Evening'
print("(e) Rows for 'Morning' and 'Evening':")
print(temperatures.loc[['Morning', 'Evening']])
print()

# (f) Select columns for 'Amanda' and 'Maxine'
print("(f) Columns for 'Amanda' and 'Maxine':")
print(temperatures[['Amanda', 'Maxine']])
print()

# (g) Select elements for 'Amanda' and 'Maxine' in 'Morning' and 'Afternoon'
print("(g) Elements for 'Amanda' and 'Maxine' in 'Morning' and 'Afternoon':")
print(temperatures.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']])
print()

# (h) Use describe method
print("(h) Descriptive statistics:")
print(temperatures.describe())
print()

# (i) Transpose temperatures
print("(i) Transposed temperatures:")
print(temperatures.T)
# or: print(temperatures.transpose())
print()

# (j) Sort column names in alphabetical order
print("(j) DataFrame with column names in alphabetical order:")
print(temperatures[sorted(temperatures.columns)])
