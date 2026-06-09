import pandas as pd
import geopandas as gpd

#Read the datasets
cantones = gpd.read_file('data/geospatial/cantones_costarica_wgs84.shp')
df = pd.read_csv('data/socioeconomic_analysis.csv')
df_subset = df[['year', 'region', 'canton', 'gdp', 'exports', 'imports', 'population', 'gdp_2019', 'population_2019', 'exports_2019',
                'imports_2019', 'gdp_pc', 'trade_balance', 'gdp_pc_2019', 'gdp_cagr', 'gdp_pc_cagr', 'population_cagr', 'gdp_cagr_cat',
                 'gdp_pc_cagr_cat', 'growth_type']]

merged_cantones = cantones.merge(df_subset, on='canton', how='left')

#Inspect geodataframe CRS
initial_CRS = merged_cantones.crs
print(f'The CRS of the raw geodataframe is {initial_CRS}')

#Reproject geodataframe
reprojected = merged_cantones.to_crs(5367)
reprojected_check = reprojected.crs
print(f'The CRS of the reprojected geodataframe is {reprojected_check}')

#Create centroid points
reprojected['centroid'] = reprojected.geometry.centroid
print('Centroids calculated')

#Calculate canton area
reprojected['area_km2'] = reprojected.geometry.area / 1000000
print('Area of cantones calculated')
#print(reprojected.columns.tolist())

#Spatial metrics table and calculate highest GDP/km2
area_metrics = reprojected[['canton','province','area_km2', 'gdp']]
area_metrics['gdp_km2'] = area_metrics['gdp'] / area_metrics['area_km2']
area_metrics_sorted = area_metrics.sort_values(by='gdp_km2', ascending=False).reset_index(drop=True)
print(f'The 3 cantones with highest GDP/km2 are {area_metrics_sorted.loc[0, 'canton']}, {area_metrics_sorted.loc[1, 'canton']} and {area_metrics_sorted.loc[2, 'canton']}.')

area_metrics_sorted.to_csv('week6_geopandas/results/area_metrics.csv', index=False)