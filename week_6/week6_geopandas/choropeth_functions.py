import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#Read the datasets
cantones = gpd.read_file('data/geospatial/cantones_costarica_wgs84.shp')
df = pd.read_csv('data/socioeconomic_analysis.csv')

#Create a merged dataset
merged_cantones = cantones.merge(df, on='canton', how='left')

#Define function for generating choropleth maps
def make_choropleth(geodataframe, variable, title, legend_title, output_path):

    fig, ax = plt.subplots(figsize = (12, 12))

    choropleth = geodataframe.plot(column=variable, cmap='YlOrRd', 
                        linewidth=0.4, edgecolor='black',
                        legend=True, ax=ax,
                        legend_kwds={'label': legend_title,
                                    'orientation': 'vertical'})

    ax.set_title(title, fontsize=14)
    ax.axis('off')

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(output_path)
    print(f'Choropleth map of {variable} generated.')

#Generate two example maps
make_choropleth(merged_cantones, 'gdp_pc', 'GDP per capita in 2022', 'GDP per capita (USD)', 'week6_geopandas/results/gdp_pc_choropleth.png')
make_choropleth(merged_cantones, 'gdp_pc_cagr', 'GDP per capita CAGR in 2022', 'GDP per capita CAGR (USD)', 'week6_geopandas/results/gdp_pc_cagr_choropleth.png')