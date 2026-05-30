import pandas as pd

df = pd.read_csv('week_4/data/socioeconomic_analysis.csv')

#Uniqueness of canton-year records

duplicate = df.duplicated(subset=['year', 'canton'])
duplicate_rows = df[duplicate]

if duplicate_rows.empty:
    print("There are no duplicate year-canton records")
else:
    print("There are duplicate rows:\n", duplicate_rows)

#Completeness of values in GDP, population or GDP per capita

incomplete_values = (df[['gdp', 'population', 'gdp_pc']].isna().sum())

if incomplete_values.sum() == 0:
    print("There are no missing values")
else:
    print("Please check for mising values")    

#Amount of cantones/year

if df['canton'].count() == 82:
    print("All 82 cantones are present")
else:
    print("Incorrect number of cantones")

#All cantones are associated to a province and region

if df.loc[df['canton'].notna(), ['province', 'region']].notna().all(
    axis=None):
    print('All cantones are associated to a province and region')
else:
    print('Some cantones are missing a province and/or region')

#Growth type values limited to expected categories

if df['growth_type'].isin(['Inclusive', 'Efficiency Gain',
                            'Population-driven', 'Decline']).all():
    print('All growth type values are within the expected categories')
else:
    print('A growth type value is not in the selected categories')