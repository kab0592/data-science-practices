import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/socioeconomic_analysis.csv')

#Select the top 10 cantones by GDP PC growth (CAGR)
gdp_pc_cagr_highest = df.sort_values(by='gdp_pc_cagr', ascending=False).reset_index(drop=True)
gdp_pc_cagr_highest = gdp_pc_cagr_highest.head(10)

#Select the bottom 10 cantones by GDP PC growth (CAGR)
gdp_pc_cagr_lowest = df.sort_values(by='gdp_pc_cagr', ascending=True).reset_index(drop=True)
gdp_pc_cagr_lowest = gdp_pc_cagr_lowest.head(10)

def barh_generation(df, xvar, yvar, title, xlabel, ylabel, color):
    df_plot = df.iloc[::-1]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.barh(df_plot[yvar], df_plot[xvar], color=color, edgecolor='black')

    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
    ax.grid(True, axis='x', alpha=0.3)

    plt.tight_layout()
    output_name = title.lower().replace(' ', '_')
    plt.savefig(f'week6_matplotlib/results/{output_name}.png')
        
barh_generation(gdp_pc_cagr_highest, 'gdp_pc_cagr', 'canton', 'Top cantones by GDP per capita growth', 'GDP per capita CAGR', 'Canton', 'green')
print(f'Bar chart of top GDP per capita CAGR generated.')

barh_generation(gdp_pc_cagr_lowest, 'gdp_pc_cagr', 'canton', 'Bottom cantones by GDP per capita growth', 'GDP per capita CAGR', 'Canton', 'red')
print(f'Bar chart of bottom GDP per capita CAGR generated.')