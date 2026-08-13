"""
Intuition. pandas is a spreadsheet that lives in Python.
A DataFrame is the whole sheet — rows and named columns.
A Series is a single column pulled out on its own.
That's 90% of the mental model: DataFrame = table, Series = one column.
"""
from collections import Counter

import pandas as pd

data = {
    "city":    ["Accra", "Lagos", "Accra", "Nairobi"],
    "product": ["laptop", "phone", "phone", "laptop"],
    "revenue": [1200, 800, 850, 1500],
}

df = pd.DataFrame(data)

# print(Counter(df["city"]))

df.head() # first 5 rows
df.tail() # last 5 rows
df.shape # (4, 3)  -> 4 rows, 3 columns


# --- SELECT a column -> this returns a Series (one column) ---
df["revenue"]          # the revenue column on its own

# --- VECTORIZE: operate on the whole column, no loop ---
df["revenue"] * 1.1    # every value * 1.1, all at once

df["rev_plus_tax"] = df["revenue"] * 1.1


# --- FILTER with a boolean mask (this is the big one) ---
df["revenue"] > 1000             # a Series of True/False, one per row
df[df["revenue"] > 1000]         # keep only the rows where that's True

# print(df[df["revenue"] > 1000])



