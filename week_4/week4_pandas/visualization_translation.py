import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#Creating a scatter plot for GDP CAGR vs GDP PC CAGR
df = pd.read_csv('week_4/data/socioeconomic_analysis.csv')

df[['gdp_cagr_100', 'gdp_pc_cagr_100']] = df[["gdp_cagr", "gdp_pc_cagr"]] * 100

plt.figure(figsize=(10, 6))

category_colors = {'Decline': 'red',
                   'Efficiency Gain': 'yellow',
                   'Inclusive': 'green',
                   'Population-driven': 'blue'
                    }

scatter_plot = plt.scatter(df['gdp_cagr_100'], df['gdp_pc_cagr_100'],
            c=df['growth_type'].map(category_colors), alpha=0.7)

plt.title("Growth type quadrants", weight='bold')
plt.xlabel("GDP CAGR (%)", weight='bold')
plt.ylabel("GDP per capita CAGR (%)", weight='bold')
plt.axvline(x=0, color='black')
plt.axhline(y=0, color='black')
plt.box(False)

legend = [
    Line2D([0], [0],
           marker='o', color='w',markerfacecolor=color, markersize=8, label=category)
    for category, color in category_colors.items()
]

plt.legend(handles = legend, bbox_to_anchor=(1.25, 0.6),
           frameon=False, title='Growth type', title_fontproperties={'weight':'bold'})

plt.tight_layout()
plt.savefig('week_4/week4_pandas/results/gdpcagr_vs_gdppccagr_scatter.png')

#Creating a ranked bar plot for highest GDP CAGR
df = pd.read_csv('week_4/data/socioeconomic_analysis.csv')
df['gdp_pc_cagr_100'] = df['gdp_pc_cagr'] * 100

df_ranked = df[['canton', 'gdp_pc_cagr_100']].sort_values(
    by='gdp_pc_cagr_100', ascending=False).head(5)

plt.figure(figsize=(10, 6))

hbars = plt.barh(df_ranked['canton'], df_ranked['gdp_pc_cagr_100'],
        color='green', edgecolor='black', height=0.6)

plt.gca().invert_yaxis()

plt.title("Highest GDP per capita growth", weight='bold')
plt.xlabel("GDP per capita CAGR (%)", weight='bold')
plt.ylabel("Canton", weight='bold')
plt.box(False)
plt.bar_label(hbars, padding=3, fmt='%.1f%%')

plt.tight_layout()
plt.savefig('week_4/week4_pandas/results/topcagr_rankedbar.png')