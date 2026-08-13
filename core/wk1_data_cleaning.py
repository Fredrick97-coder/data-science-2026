import seaborn as sns

df = sns.load_dataset("titanic")

print(df.shape)

print(df.isnull().sum())

df.info()

print(df.head())

print(df.describe())

