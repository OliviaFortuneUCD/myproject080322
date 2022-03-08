import warnings
import seaborn as sns
# Convert dataset to pandas dataframes
import pandas as pd
df = pd.read_csv("nyt1.csv")

#If they clicked but no impression
df[(df['Clicks']>0) & (df['Impressions']==0)].shape[0]


# Create a new variable 'age_group' to categorize users by age
bins = [0, 18, 25, 35, 45, 55, 65, 110]
labels = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
df['age_group'] = pd.cut(df.Age, bins, labels = labels,include_lowest = True)
df['CTR'] = round(df['Clicks']/df['Impressions'], 5)
# Plot the distribution of Click-through rate by age group
sns.boxenplot(x=df['age_group'], y=df['CTR'])