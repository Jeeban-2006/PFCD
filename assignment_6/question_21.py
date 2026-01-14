# Question 21
# Convert L=['Cry', 'Apple', 'Orange', 'Sky', 'Banana'] to a pandas series. Create a new 
# series with the elements which contain a vowel. Create another series starts with vowel.

import pandas as pd

# Convert list to pandas series
L = ['Cry', 'Apple', 'Orange', 'Sky', 'Banana']
series = pd.Series(L)

print("Original series:")
print(series)
print()

# Create a new series with elements which contain a vowel
vowels = 'aeiouAEIOU'

def contains_vowel(word):
    return any(char in vowels for char in word)

series_with_vowel = series[series.apply(contains_vowel)]
print("Series with elements containing a vowel:")
print(series_with_vowel)
print()

# Create a series that starts with a vowel
def starts_with_vowel(word):
    return word[0] in vowels

series_starts_with_vowel = series[series.apply(starts_with_vowel)]
print("Series with elements starting with a vowel:")
print(series_starts_with_vowel)
print()

# Alternative using str methods
print("Using string methods:")
series_with_vowel_alt = series[series.str.contains('[aeiouAEIOU]', regex=True)]
print("Series with elements containing a vowel:")
print(series_with_vowel_alt)
print()

series_starts_with_vowel_alt = series[series.str.match('^[aeiouAEIOU]')]
print("Series with elements starting with a vowel:")
print(series_starts_with_vowel_alt)
