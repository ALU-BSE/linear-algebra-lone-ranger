import pandas as pd
import numpy as np

# Load data
# data = pd.read_csv('path/to/data') This line isn't necessary right now 

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

for i in range(len(Prices)): # len(Prices) gives the number of rows
    row_sum = 0
    for j in range(len(Prices[0])): # len(Prices[0]) gives the number of columns
        # COMPLETE THE MISSING LOGIC HERE
        row_sum += Prices[i][j] * Array2[j] # For each element in the current row being iterated through in the Prices matrix,  multiply by the corresponding column position in the Array2 list and then add to row sum to sum up the figurs i.e  Prices[0][0] = 300, * Array2[0] = 200, => 60000, Prices[0][1] = 500, * Array2[1] = 100, => 50000, Therefore 60000 + 50000 = 110,000
    Ans.append(row_sum) # Add answer to the Ans list and reiterate for the second Prices row


print(Ans)
