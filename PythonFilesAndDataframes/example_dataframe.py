

import json
import sys
import argparse
import pandas as pd

# First we create an empty dataframe. It will have null value (NaN)
print("Creating an empty dataframe ")
print

df = pd.DataFrame(columns=['a','b','c','d'], index=['x','y','z'])
print("initial dataframe is \n {0}".format(df))
print

# Set values for row y
print("Setting row y to values 1, 5, 2, 3 ")
df.loc['y'] = pd.Series({'a':1, 'b':5, 'c':2, 'd':3})

print("\n")
print("Updated dataframe is \n {0}".format(df))
print

# add a new row
print("Adding row a values 90, 91, 92, 93 ")

rowDict = {'a':90, 'b':91, 'c':92, 'd':93}

newRow = pd.DataFrame(rowDict, index=['a'])  # Create a row for this domain
newDF = pd.concat([df, newRow])  # Add the row to the table

print("\n")
print("Updated dataframe is \n {0}".format(newDF))
print

# Output the dataframe to a csv (spreadsheet) so you can look at it in MS Excel

newDF.to_csv("pandas_sheet1.csv")

# Now you add code to do the following in the dataframe

# 1. Set values for row x and row z
# 2. Add a new row to the data frame
# 3. Change the value in row y, column c
# 4. Each time, create the csv file again.




