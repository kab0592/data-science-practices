import pandas as pd

df = pd.read_csv('week_4/data/socioeconomic_analysis.csv')

#Exercise 1 - Regional summary 

df_regional_sum = df.groupby('region', as_index=False).agg(
    cantons=('canton', 'count'),
    avg_gdp_cagr=('gdp_cagr', 'mean'),
    avg_gdp_pc_cagr=('gdp_pc_cagr', 'mean'),
    avg_pop_cagr=('population_cagr', 'mean'),
    avg_gdp_pc=('gdp_pc', 'mean'),
    )

df_regional_sum.to_csv(
    'week_4/week4_pandas/results/regional_summary.csv', index=False)

print("Exercise 1 output saved")

#Exercise 2 - Growth type summary

df_growth_sum = df.groupby('growth_type', as_index=False).agg(
    cantons=('canton', 'count'),
    avg_gdp_cagr=('gdp_cagr', 'mean'),
    avg_gdp_pc_cagr=('gdp_pc_cagr', 'mean'),
    )

df_growth_sum.to_csv(
    'week_4/week4_pandas/results/growth_summary.csv', index=False)

print("Exercise 2 output saved")

#Exercise 3 - Province x Growth Type pivot table

socioeconomic_pivot = pd.pivot_table(df, 
                       values='canton', 
                       index='province', 
                       columns='growth_type', 
                       aggfunc='count').reset_index().fillna(0)

socioeconomic_pivot.to_csv(
    'week_4/week4_pandas/results/socioeconomic_pivot.csv', index=True)

print("Exercise 3 output saved")

#Exercise 4 - Pivot table to long format

socioeconomic_pivot_melt = pd.melt(socioeconomic_pivot,
                            id_vars='province',
                            var_name='growth_type',
                            value_name='canton_count')
                            
socioeconomic_pivot_melt.to_csv(
    'week_4/week4_pandas/results/socioeconomic_pivot_melt.csv', index=True)

print("Exercise 4 output saved")

#Exercise 5 - Top and bottom cantones (GDP per capita CAGR)

df_sorted = df.sort_values(by='gdp_pc_cagr',
                    ascending=False)

top_cantones = df_sorted[['canton', 'province', 'region', 'gdp_pc_cagr',
                'growth_type']].iloc[0:10]

bottom_cantones = df_sorted[['canton', 'province', 'region', 'gdp_pc_cagr',
                'growth_type']].iloc[-10:]

print("TOP CANTONES\n", top_cantones.head(10))
print("BOTTOM CANTONES\n", bottom_cantones.head(10))