import pandas as pd
import sqlalchemy as sqla

df = pd.read_csv('data/socioeconomic_analysis.csv')

df.columns = [c.lower().replace(' ', '_') for c in df.columns]

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:Naci050792@localhost:5432/portfolio_practices')

df.to_sql("socioeconomic_analysis", engine, if_exists='replace', index=False)

print("Table successfully exported")