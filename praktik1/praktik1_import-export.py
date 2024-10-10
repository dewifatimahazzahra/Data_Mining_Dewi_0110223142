import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Object Creation
s= pd.Series([1,3,5, np.nan, 6, 8])
dates = pd.date_range('2023-10-01', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

#Import export data
imported_df = pd.read_csv("C:/xampp/htdocs/DEWI/data mining/praktik1/sample_data.csv")

print("Importing and exporting data : ")
print("Exported DataFrame to CSV : ")
print(df)
print("\nImported DataFrame from CSV : ")
print(imported_df)
print("="*40)

df.to_csv('sample_data2.csv')