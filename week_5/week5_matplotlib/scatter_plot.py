import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/socioeconomic_analysis.csv')

x = df['population']
y = df['gdp']

correlation = round(x.corr(y), 2)
r2 = round(correlation ** 2, 3)

#Create the trendline
slope, intercept = np.polyfit(x, y, 1)
trendline = slope * x + intercept

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(x, y)

#Add trendline to scatterplot
sort_idx = np.argsort(x)
ax.plot(x.iloc[sort_idx], trendline.iloc[sort_idx],color='black')

ax.grid(True, alpha=0.3)
ax.set_xlabel('Population')
ax.set_ylabel('GDP (USD)')
ax.set_title(f'Population vs GDP\n(r={correlation}, R²={r2})')
ax.ticklabel_format(style='plain', axis='y')

plt.tight_layout()
plt.savefig('week5_matplotlib/results/example_plot.png')
plt.show()