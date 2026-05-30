import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('week_4/data/socioeconomic_analysis.csv')

metrics = ['gdp', 'gdp_pc', 'gdp_cagr']

summary = (df[metrics].agg(['mean', 'median', 'std']).T.reset_index().round(2))

summary.columns = ['variable', 'mean', 'median', 'stdev']

print(summary)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].hist(df['gdp'])
axes[0].set_title('GDP')
axes[0].set_xlabel("GDP")
axes[0].set_ylabel("Number of Cantons")

mean = df['gdp'].mean()
std = df['gdp'].std()

axes[0].axvline(mean, color='red')
axes[0].axvline(mean + std, color='orange')
axes[0].axvline(mean - std, color='orange')

axes[1].hist(df['gdp_pc'])
axes[1].set_title('GDP per Capita')
axes[1].set_xlabel("GDP per Capita")
axes[1].set_ylabel("Number of Cantons")

mean = df['gdp_pc'].mean()
std = df['gdp_pc'].std()

axes[1].axvline(mean, color='red')
axes[1].axvline(mean + std, color='orange')
axes[1].axvline(mean - std, color='orange')

axes[2].hist(df['gdp_cagr'])
axes[2].set_title('GDP CAGR')
axes[2].set_xlabel("GDP CAGR (%)")
axes[2].set_ylabel("Number of Cantons")

mean = df['gdp_cagr'].mean()
std = df['gdp_cagr'].std()

axes[2].axvline(mean, color='red')
axes[2].axvline(mean + std, color='orange')
axes[2].axvline(mean - std, color='orange')

plt.savefig('week_4/week4_statistics/summary_histogram.png')