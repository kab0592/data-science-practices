import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

cantones = gpd.read_file('data/geospatial/cantones_costarica_wgs84.shp')
df = pd.read_csv('data/socioeconomic_analysis.csv')

merged_cantones = cantones.merge(df, on='canton', how='left')

colors = {'Decline': 'red', 'Efficiency Gain': 'yellow',
          'Inclusive': 'green', 'Population-driven': 'blue'}

merged_cantones['color'] = merged_cantones['growth_type'].map(colors)

fig, ax = plt.subplots(figsize = (12, 12))

merged_cantones.plot(color=merged_cantones['color'],
                     linewidth=0.4, edgecolor='black', ax=ax)

legend_elements = []
for category, color in colors.items():
    legend_item = Patch(facecolor=color, edgecolor='black',
                        label=category)
    legend_elements.append(legend_item)

ax.legend(handles=legend_elements,
        title='Growth Type', loc='lower left')

ax.set_title('Growth Type by Canton, Costa Rica - 2022', fontsize=14)
ax.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('week5_geopandas/results/growth_type_choropleth.png')
plt.show()

fig, ax = plt.subplots(figsize = (12, 12))

merged_cantones.plot(column='gdp_pc', cmap='YlOrRd', 
                    linewidth=0.4, edgecolor='black',
                    legend=True, ax=ax,
                    legend_kwds={'label': 'GDP per Capita (USD)',
                                 'orientation': 'vertical'})

ax.set_title('GDP per capita by Canton, Costa Rica - 2022', fontsize=14)
ax.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('week5_geopandas/results/gdp_pc_choropleth.png')
plt.show()