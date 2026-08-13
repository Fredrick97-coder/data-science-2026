import pandas as pd

"""
Intuition. groupby is the "per-category" tool.
Any time you hear "total sales per city," "average score per student," "count per group" — that "per X" is a groupby on column X. 
It works in three moves, nicknamed split–apply–combine: split the table into groups (one per city),
apply a calculation to each group (sum the revenue), combine the results back into one small table.
"""

df = pd.DataFrame({
    "city":    ["Accra", "Lagos", "Accra", "Nairobi"],
    "product": ["laptop", "phone", "phone", "laptop"],
    "revenue": [1200, 800, 850, 1500],
})

result = (
    df.groupby("city")["revenue"]   # split by city, look at the revenue column
    .sum()                        # apply: sum revenue within each city
    .sort_values(ascending=False) # combine + sort highest first
)

print(result)

"""
Two notes so nothing feels like magic:

After .groupby("city"), city becomes the index (the row labels), not a normal column. 
If you want it back as a plain column, tack on .reset_index(). Small thing, comes up constantly.
.sum() is just one choice — swap in .mean(), .count(), .max(), etc. Same skeleton, different verb.
"""