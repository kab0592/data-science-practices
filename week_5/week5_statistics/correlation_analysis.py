import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/socioeconomic_analysis.csv')

#Define a function so we can display several scatter plots
def correlation_plot(df, x_var, y_var, ax):

    x = df[x_var]
    y = df[y_var]

    correlation = round(x.corr(y), 2)
    r2 = round(correlation ** 2, 3)

    #Create the trendline
    slope, intercept = np.polyfit(x, y, 1)
    trendline = slope * x + intercept

    ax.scatter(x, y)

    #Add trendline to scatterplot
    ax.plot(x, trendline)

    ax.set_xlabel(x_var)
    ax.set_ylabel(y_var)
    ax.set_title(f'{x_var} vs {y_var}\n(r={correlation}, R²={r2})')

    return correlation

fig, axes = plt.subplots(1, 3, figsize = (18, 5))

correlation_plot(df, 'gdp', 'population_cagr', axes[0])

correlation_plot(df, 'gdp_pc', 'population_cagr', axes[1])

correlation_plot(df, 'trade_balance', 'population_cagr', axes[2])

plt.tight_layout()
fig.savefig('week5_statistics/results/corr_plots.png')
plt.show()

#Correlation matrix analysis
corr_vars = ['gdp', 'exports', 'imports', 'population',
                'gdp_pc', 'trade_balance', 'gdp_cagr',
                'gdp_pc_cagr']

corr_df = df[corr_vars]

matrix = corr_df.corr()

fig, ax = plt.subplots(figsize=(10, 8))

heatmap = ax.imshow(matrix,cmap = 'coolwarm')

ax.set_xticks(range(len(matrix.columns)))
ax.set_yticks(range(len(matrix.columns)))

ax.set_xticklabels(matrix.columns, rotation=45, ha='right')
ax.set_yticklabels(matrix.columns)

#Add correlation values to cells
for i in range(len(matrix)):
    for j in range(len(matrix)):
        ax.text(j, i, f'{matrix.iloc[i, j]:.2f}', 
            ha='center', va='center')

fig.colorbar(heatmap)

ax.set_title('Socioeconomic Correlation Matrix')

plt.tight_layout()
fig.savefig('week5_statistics/results/corr_matrix.png')
plt.show()