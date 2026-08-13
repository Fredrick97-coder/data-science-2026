import pandas as pd

url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
df = pd.read_csv(url)

# display first 5 entries
df.head()

df.info()

# sum of nulls of every feature/category label
df.isnull().sum()

# function to clean the telco data
def clean_telco(df):
    # blanks stored as text -> coerce to numeric (blanks become NaN)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # those 11 NaNs are tenure-0 new customers -> genuinely $0 billed, not median
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # unique identifier, zero predictive signal -> drop
    df = df.drop(columns=["customerID"])

    # "No internet/phone service" is redundant with InternetService/PhoneService -> collapse to "No", uniformly
    internet_add_ons = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
                        "TechSupport", "StreamingTV", "StreamingMovies"]
    df[internet_add_ons] = df[internet_add_ons].replace("No internet service", "No")
    df["MultipleLines"] = df["MultipleLines"].replace("No phone service", "No")

    # nominal categoricals -> one-hot; drop_first kills the redundant twin; int not bool
    nominal_cols = ["gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
                    "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                    "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
                    "PaperlessBilling", "PaymentMethod"]
    df = pd.get_dummies(df, columns=nominal_cols, drop_first=True, dtype=int)

    # target -> 0/1
    df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

    return df

# assign the cleaned dataset to cleaned_df
cleaned_df = clean_telco(df)


