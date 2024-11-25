import pandas as pd

import numpy as np
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
print(df["City"])


c = np.array([20, 1, 2, 3, 4])
print(c)

d = c[0:5]
print(d)