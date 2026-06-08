import pandas as pd
import numpy as np

df = pd.read_csv('data/socioeconomic_analysis.csv')

#Exercise 1: Sampling simulation and interpretation of sample size
full_mean = round(df['gdp'].mean(), 2)
random10_mean = round(df['gdp'].sample(n=10).mean(), 2)
random25_mean = round(df['gdp'].sample(n=25).mean(), 2)
random50_mean = round(df['gdp'].sample(n=50).mean(), 2)

print('Exercise 1 results')
print(f'The full dataset GDP mean is {full_mean}')
print(f'The 10 sample dataset GDP mean is {random10_mean}')
print(f'The 25 sample dataset GDP mean is {random25_mean}')
print(f'The 50 sample dataset GDP mean is {random50_mean}')

#Exercise 2: Confidence interval calculation (95%)
gdp_pc_mean = df['gdp_pc'].mean()
gdp_pc_std = df['gdp_pc'].std()
standard_error = (gdp_pc_std) / np.sqrt(df['gdp_pc'].count())
#For a population standard deviation and a sample size >= 30, the Z-score of 1.96 is used as the critical value
critical_value = 1.96
margin_error = standard_error * critical_value
lower_bound = round((gdp_pc_mean - margin_error), 2)
upper_bound = round((gdp_pc_mean + margin_error), 2)

print('Exercise 2 results')
print(f'The 95% confidence interval for GDP per capita is {lower_bound} - {upper_bound}')

#Exercise 3: Hypothesis testing introduction
#Do strong growth cantones have higher GDP per capita than cantones in economic decline?
df_strong_cantones = df.loc[df['gdp_pc_cagr_cat'] == 'Strong']
df_declining_cantones = df.loc[df['growth_type'] == 'Decline']

#Calculate variables
strong_cantones_mean = df_strong_cantones['gdp_pc'].mean()
strong_cantones_std = df_strong_cantones['gdp_pc'].std()
strong_cantones_n = df_strong_cantones['gdp_pc'].count()

decline_cantones_mean = df_declining_cantones['gdp_pc'].mean() 
decline_cantones_std = df_declining_cantones['gdp_pc'].std()
decline_cantones_n = df_declining_cantones['gdp_pc'].count()

summary_table = pd.DataFrame({
    'mean': [strong_cantones_mean, decline_cantones_mean],
    'std': [strong_cantones_std, decline_cantones_std],
    'count': [strong_cantones_n, decline_cantones_n]
}, index=['Strong', 'Decline']).round(2)

print('Exercise 3 results')
print(summary_table)