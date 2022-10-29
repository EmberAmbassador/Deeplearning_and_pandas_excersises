# Oschegow Nicolaj, Bruder Luca
# !!! NOTE: Only upload the Python (.py) or IPython Notebook (.ipynb) file. Do NOT try to upload the csv file. 
import pandas as pd
import numpy as np

## 0) Import the associated csv file as a Pandas DataFrame and call it "df". Do not change the name of the csv file or its contents.

d = open("ex21_data.csv", "r")
df = pd.read_csv("ex21_data.csv")

## 1) Display the number of valid elements (no NaN elements), the average, the standard deviation, and minima and maxima for each column.

def stats():
    print("Number of non-NaN elements in each column:")
    print(df.count())
    print("---------------------------------------------")

    print("The average of each column:")
    print(df.mean(axis=0))
    print("---------------------------------------------")

    print("The standard deviation of each column:")
    print(df.std(axis=0))
    print("---------------------------------------------")

    print("The minimum of each column:")
    print(df.min(axis=0))
    print("---------------------------------------------")

    print("The maximum of each column:")
    print(df.max(axis=0))
    # This signifies the end of the stats function
    print("_____________________________________________")

stats()

# What is problematic about the column "z"?
# Column "z" contains multiple problematic values with either inf or NaN elements.


## 2) Replace all +/-infinite values with NaN.

df = df.replace(float('Inf'), float('NaN'))
df = df.replace(-float('Inf'), float('NaN'))

## 3) Calculate (not by hand) how often NaN occurs in the DataFrame.

print("NaN values in each column:")
print(df.isna().sum())
print("_____________________________________________")

## 4) Delete all rows that contain a NaN.

df = df.dropna()

## 5) Display the number of elements, the average, the standard deviation, and minima and maxima for each column.

stats()

# What has changed compared to 1)?
# With the NaN and infinite values gone each column contains the same amount of non-NaN elements. This leads to actually useful values contrary to standard deviations of NaN and a maximum of infinite.

## 6) Sort the DataFrame by the z column (descending).

df = df.sort_values(by=['z'], ascending=False)

## 7) For each column, output the row that contains the maximum of the column.

# The following comands output the row with the maximum of the column in regards
# to the new order from the previous task. The new row 0 would for example be the
# old row 19.
# Furthermore 'Unnamed: 0' is not considered a column.

print("The maximum of column x is in row: " + str(df['x'].argmax()))
print("The maximum of column y is in row: " + str(df['y'].argmax()))
print("The maximum of column z is in row: " + str(df['z'].argmax()))
print("_____________________________________________")

## 8) Delete the z column in the DataFrame.

df = df.drop(columns=['z'])


## 9) Add a new column with the value x+y and the label 'x+y' to the DataFrame.

# Normally df.sum(axis=1) would be used. But since 'Unnamed: 0' is not a valid
# column and the code below throws a key exception, explicit addition was used.
#df['x + y'] = df['x', 'y'].sum(axis=1)

df['x + y'] = df['x'] + df['y']


# A simple function to display the necessary information for part 1 and 5
def stats():
    print("Number of non-NaN elements in each column:")
    print(df.count())
    print("---------------------------------------------")

    print("The average of each column:")
    print(df.mean(axis=0))
    print("---------------------------------------------")

    print("The standard deviation of each column:")
    print(df.std(axis=0))
    print("---------------------------------------------")

    print("The minimum of each column:")
    print(df.min(axis=0))
    print("---------------------------------------------")

    print("The maximum of each column:")
    print(df.max(axis=0))
    print("---------------------------------------------")
