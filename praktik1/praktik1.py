import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Object Creation
s= pd.Series([1,3,5, np.nan, 6, 8])
dates = pd.date_range('2023-10-01', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print("Object Creation : ")
print("Series : ")
print(s)
print("\nDataFrame : ")
print(df)
print("="*50)

# viewing data
print("Viewing Data : ")
print("First 3 Rows : ")
print(df.head(3))
print("\nLast 2 rows : ")
print(df.tail(2))
print("\nIndex and Columns : ")
print(df.index)
print(df.columns)
print("="*40)


#Selection
print("Selection : ")
print("Selecting a column(A) : ")
print(df['A'])
print("\nSelecting by label (row 0) : ")
print(df.iloc[1])
print("\nSelecting a subset of rows and columns : ")
print(df.loc[dates[1:3], ['A', 'B']])
print("="*40)


#Missing Data
df1 = df.reindex(index=dates[0:4], columns = list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1

print("Mising Dara : ")
print("DataFrame with missing values : ")
print(df1)
print("\nDropping rows woth missing values : ")
print(df1.dropna())
print("\nFilling missing values : ")
print(df1.fillna(value=0))
print("="*60)



# Operations
print("Operations : ")
print("Mean of each column : ")
print(df.mean())
print("\nSum of each row : ")
print(df.sum(axis=1))
print("="*40)


# Merge
left = pd.DataFrame(
    {'key': ['K0', 'K1', 'K2', 'K3'], 
     'A':   ['A0', 'A1', 'A2', 'A3'],
     'B':   ['B0', 'B1', 'B2', 'B3'] }
     )
right = pd.DataFrame(
    {'key': ['K0', 'K1', 'K2', 'K3'], 
    'C':   ['C0', 'C1', 'C2', 'C3'],
    'D':   ['D0', 'D1', 'D2', 'D3'] }
    )
merged_df = pd.merge(left, right,on='key')

print("Merge : ")
print("Merged DataFrame : ")
print(merged_df)
print("="*40)

# Grouping
grouped = df.groupby('A').sum()
print("Grouping : ")
print("Grouped DataFrame : ")
print(grouped)
print("="*40)



# Reshaping
staked = df.stack()
unstacked = staked.unstack()

print("Reshaping : ")
print("Staked DataFrame : ")
print(staked)
print("\nUnstaked DataFrame : ")
print(unstacked)
print("="*40)

# Time Series
ts = pd.Series(np.random.randn(1000), index=pd.date_range('2023-01-01', periods=1000))
cumulative_sum = ts.cumsum()

print("Time Series : ")
print(ts.head())
print("\nCumulative Sum : ")
print(cumulative_sum.head())
print("="*40)


# Categoricals

# Create a Categorical Series
s = pd.Series(["cat", "dog", "bird", "cat", "dog"], dtype="category")

#define new categories
new_categories = ["Category 1", "Category 2", "Category 3"]

#Create a Categorical Series with the new categories
s_new = s.cat.set_categories(new_categories)

print("Categoricals : ")
print("Original categorical series : ")
print(s)
print("\nNew Categorical Series with updates categories : ")
print(s_new)

#Plotting
df.plot()
plt.show()

print("Plotting : ")
print("="*40)