import pandas as pd
# pandas_l2 mini challenge
"""
Average salary per department.
Count of employees per department.
Which department has the higher average salary? (Sort to make it obvious.)
"""
df = pd.DataFrame({
    "name":       ["Ama", "Kofi", "Yaa", "Kweku", "Esi"],
    "department": ["eng", "sales", "eng", "sales", "eng"],
    "salary":     [3000, 5200, 4100, 6000, 3500],
})

average_salary = (
    df.groupby("department")["salary"]
    .mean()
)

count_emp = (
    df.groupby("department")["name"]
    .count()
)

higher_average_salary = average_salary.idxmax()

# print(average_salary)
# print(count_emp)
print(higher_average_salary)

summary = df.groupby("department")["salary"].agg(["mean", "size"])

"""
1. One pass, not two. On Task 2 I said "one loop, not two." 
Here you ran groupby twice to get mean and count separately. 
.agg() does both in a single pass and hands you one tidy table:

python
summary = df.groupby("department")["salary"].agg(["mean", "count"])
#           mean  count
# eng    3533.33      3
# sales  5600.00      2

Watch for that instinct generally — when you're scanning the same data twice,
there's usually a way to do it once.

2. .size() vs .count() — a right-tool distinction (like Counter vs defaultdict earlier).
You used .count() on the name column, which works, but it forced you to arbitrarily pick a column.
df.groupby("department").size() counts rows directly, no column needed. The real difference: .count() counts non-null values in a column,
.size() counts all rows including missing ones. That gap matters the moment your data has holes — which is basically always.

3. "Which is highest" has a one-liner. You sorted to eyeball it (totally fine).
But when you just need the name of the top group: average_salary.idxmax() → 'sales'. idxmax/idxmin return the index label of the max/min.
Handy and interview-friendly.
"""

# print(summary)

# Best way for pandas_l2 mini challenge
"""
import pandas as pd

df = pd.DataFrame({
    "name":       ["Ama", "Kofi", "Yaa", "Kweku", "Esi"],
    "department": ["eng", "sales", "eng", "sales", "eng"],
    "salary":     [3000, 5200, 4100, 6000, 3500],
})

# 1 & 2: mean and count per department, in a single pass
summary = df.groupby("department")["salary"].agg(["mean", "count"])

# 3: department with the highest average salary
top_dept = summary["mean"].idxmax()

print(summary)
print(f"Highest average salary: {top_dept}")
"""