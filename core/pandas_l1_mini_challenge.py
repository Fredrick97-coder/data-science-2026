import pandas as pd
# pandas_l1 mini challenge
"""
Do three things:

Select just the salary column.
Add a new column annual_salary that is salary * 12 (vectorized — no loop).
Return only the rows where age is greater than 30.
"""
df = pd.DataFrame({
    "name":  ["Ama", "Kofi", "Yaa", "Kweku"],
    "age":   [25, 34, 29, 41],
    "salary":[3000, 5200, 4100, 6000],
})

print(df["salary"])          # shows the Series
df["annual_salary"] = df["salary"] * 12
print(df[df["age"] > 30])    # shows the filtered rows