import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Week 1 · Data Cleaning — Step 1: find the mess
"""
Intuition. Before you clean anything, you diagnose. 
A doctor doesn't prescribe before examining. 
The first question on any real dataset is always: where are the holes, and what type is each column actually?
Two commands answer that: .info() (types + non-null counts) and .isnull().sum() (missing values per column).
"""
df = sns.load_dataset("titanic")

print(df.shape)

df.info()

print(df.head())

# print(df.describe())



# Week 1 · Cleaning — Step 2: decide before you fix
"""
You've found four holes. The instinct is to rush to fill them, but the right move is to decide a strategy per column first,
because the fix depends entirely on how much is missing and what the column is. The framework:

A trickle missing (embarked: 2 of 891, ~0.2%) → tiny. Either drop those 2 rows, or fill with the most common value. Low stakes either way.
A meaningful chunk (age: 177, ~20%) → too many rows to throw away — you'd be deleting a fifth of your data.
This calls for imputation: filling the gaps with a sensible estimate (a median, ideally a smart one).
Mostly empty (deck: 688, ~77%) → the column is more hole than data.
Usually you drop the whole column — or, if the fact of being missing is itself informative, engineer a "known/unknown" flag.

Mini-challenge — reason it out before any code. For each of these three, tell me what you'd do and why:

deck (77% missing)
age (20% missing)
embarked (2 rows missing)
"""

df = df.drop(columns=["deck"])
# global median (fine)
df["age"] = df["age"].fillna(df["age"].median())

# smarter: median age within each passenger class
# df["age"] = df["age"].fillna(df.groupby("pclass")["age"].transform("median"))

# embarked: 2 rows missing -> fill with the most common port
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

df = df.drop(columns=["class", "alive", "embark_town"])
print(df.isnull().sum())
print(f"The new size is: {df.shape}")


"""
Week 1 · Cleaning — Step 4: categorical encoding

Why this exists. Your data is clean, but it's not yet modelable. Almost every ML algorithm is math under the hood — it multiplies and adds numbers.
Hand it the string "male" and it has nothing to compute. So we translate categorical text into numbers. That translation is encoding, and how you translate depends on whether the categories have an order.

Two kinds, two tools — and picking wrong quietly breaks your model:

1. Ordinal → the categories have a real order. Map them to numbers that preserve it.
pclass already is this (1<2<3). A column like who doesn't have a natural order, so this is not the tool for it.

2. Nominal → categories with no order (sex, embarked). Here's the trap: if you just map male→0, female→1, ... and there are 3+ categories,
the model reads the numbers as quantities and invents a fake ranking — it'll think embarked=2 is "more than" embarked=0, which is meaningless.
The fix is one-hot encoding: give each category its own 0/1 column. "Was this passenger's port S? (0/1). Was it C? (0/1). Was it Q? (0/1)." No fake order, because there's no single number to misread.

The intuition in one line: ordered → one column of ranked numbers; unordered → one 0/1 column per category.
"""

"""
That drop_first point matters and interviewers poke at it: with 2 categories you only need 1 column,
with 3 you need 2. The dropped one becomes the "baseline" — it's implied when all the others are 0.
Carrying all of them is redundant information, the same "don't store a fact twice" idea you've already internalized.

Mini-challenge — reason first, then code:

Before writing anything: who has values man/woman/child.
Is that ordinal or nominal? Justify it in one sentence — that judgment decides the tool.
One-hot encode sex and embarked as above.
Then run df.head() and df.dtypes, and tell me: what type are the new encoded columns?
(Look closely — the answer has a small surprise that's worth seeing now rather than in a model later.)
"""

# Mini-challenge — reason first, then code

# # sex has 2 unordered categories. One-hot it.
# # drop_first=True drops the redundant first column:
# # if not-female, it must be male — you don't need both.
# df = pd.get_dummies(df, columns=["sex"], drop_first=True)
#
# # embarked has 3 unordered categories -> 3 (minus 1) columns
# df = pd.get_dummies(df, columns=["embarked"], drop_first=True)
# # -> 'embarked_Q', 'embarked_S' (C is the dropped baseline)

# make the encoding produce integers directly
df = pd.get_dummies(df, columns=["sex", "embarked"], drop_first=True, dtype=int)

print(f"New shape: {df.head()}")

print(df.dtypes)

df["fare"].hist(bins=50)
plt.xlabel("fare"); plt.ylabel("count")


df["fare_log"] = np.log1p(df["fare"]) # log(1 + fare), safe for zeros
df["fare_log"].hist(bins=50)

print(np.log1p(7.25))

plt.show()

