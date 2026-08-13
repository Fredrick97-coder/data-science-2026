import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from displayfunction import display

# Load dataset into dataframe
df = sns.load_dataset("titanic")

import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns

def visualize(df):
    df.info()                          # prints on its own
    display(df.isnull().sum())         # need display() inside a function
    display(df.head())
    display(df["fare"].describe())
    df["fare"].hist(bins=50)
    plt.xlabel("fare"); plt.ylabel("count"); plt.title("Fare distribution")
    plt.show()

def clean_titanic(df):
    # deck: ~77% MISSING -> imputing that much fabricates signal -> drop
    df = df.drop(columns=["deck"])

    # age: ~20% MISSING -> too many rows to lose; median is robust to skew -> median fill
    df["age"] = df["age"].fillna(df["age"].median())

    # redundant TEXT twins -> keep coded, drop text (never drop the target 'survived')
    df = df.drop(columns=["class", "alive", "embark_town"])

    # embarked: 2 MISSING -> trivial share -> fill with most common port
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

    # nominal categories (no order) -> one-hot; dtype=int for 0/1; drop_first avoids redundancy
    df = pd.get_dummies(df, columns=["sex", "embarked", "who"], drop_first=True, dtype=int)

    # fare is right-skewed with 15 zero-fares -> log1p compresses the tail and is safe for 0s
    df["fare_log"] = np.log1p(df["fare"])
    return df

visualize(df)                    # inspect RAW data
df_clean = clean_titanic(df)     # assign, or the result is lost
print(df_clean.dtypes)
print(df_clean.shape)            # (891, 12)