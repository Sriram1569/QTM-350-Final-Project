import pandas as pd
import os

OUT = "figures"
os.makedirs(OUT, exist_ok=True)

INPUT = "data/processed/merged_data.csv"
df = pd.read_csv(INPUT)

df.rename(columns={"Country Code": "iso3", "Year": "year"}, inplace=True)
df['year'] = df['year'].astype(int)

df.head(20).to_csv(os.path.join(OUT,"clean_head.csv"), index=False)
desc = df.describe(include='all')
desc.to_csv(os.path.join(OUT,"descriptive_stats_all.csv"))
country_desc = df.groupby('iso3')[['gdp_per_capita','employment_rate','gdp_growth']].describe()
country_desc.to_csv(os.path.join(OUT,"descriptive_by_country.csv"))
miss = df.isnull().sum().to_frame(name='missing_count')
miss['pct_missing'] = miss['missing_count'] / len(df) * 100
miss.to_csv(os.path.join(OUT,"missingness.csv"))

print("Data description written to figures/: clean_head.csv, descriptive_stats_all.csv, descriptive_by_country.csv, missingness.csv")

