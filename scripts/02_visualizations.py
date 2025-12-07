import pandas as pd
import matplotlib.pyplot as plt
import os

OUT = "figures"
os.makedirs(OUT, exist_ok=True)

INPUT = "data/processed/merged_data.csv"
df = pd.read_csv(INPUT)

df.rename(columns={"Country Code": "iso3", "Year": "year"}, inplace=True)
df['year'] = df['year'].astype(int)

plt.figure(figsize=(10,5))
for c in df['iso3'].unique():
    s = df[df['iso3']==c]
    plt.plot(s['year'], s['gdp_per_capita'], label=c)
plt.title('GDP per capita (constant 2015 US$)')
plt.xlabel('Year'); plt.ylabel('GDP per capita')
plt.legend(); plt.grid(alpha=0.2)
plt.tight_layout(); plt.savefig(os.path.join(OUT,'gdp_percap_timeseries.png')); plt.close()

plt.figure(figsize=(10,5))
for c in df['iso3'].unique():
    s = df[df['iso3']==c]
    plt.plot(s['year'], s['employment_rate'], label=c)
plt.title('Employment-to-population ratio (15+, %)')
plt.xlabel('Year'); plt.ylabel('Employment rate (%)')
plt.legend(); plt.grid(alpha=0.2)
plt.tight_layout(); plt.savefig(os.path.join(OUT,'employment_rate_timeseries.png')); plt.close()

plt.figure(figsize=(10,5))
for c in df['iso3'].unique():
    s = df[df['iso3']==c]
    plt.plot(s['year'], s['gdp_growth'], label=c)
plt.title('GDP growth (annual %)')
plt.xlabel('Year'); plt.ylabel('GDP growth (%)')
plt.axhline(0, color='k', linewidth=0.6)
plt.legend(); plt.grid(alpha=0.2)
plt.tight_layout(); plt.savefig(os.path.join(OUT,'gdp_growth_timeseries.png')); plt.close()

plt.figure(figsize=(7,6))
for c in df['iso3'].unique():
    s = df[df['iso3']==c]
    plt.scatter(s['employment_rate'], s['gdp_per_capita'], label=c, alpha=0.8, s=40)
plt.xlabel('Employment rate (%)'); plt.ylabel('GDP per capita')
plt.title('GDP per capita vs Employment rate')
plt.legend(); plt.tight_layout(); plt.savefig(os.path.join(OUT,'gdp_vs_employment_scatter.png')); plt.close()

print("Saved visualization PNGs to figures/: gdp_percap_timeseries.png, employment_rate_timeseries.png, gdp_growth_timeseries.png, gdp_vs_employment_scatter.png")

