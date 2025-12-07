import pandas as pd

# Load datasets from SAME DIRECTORY
employment = pd.read_csv("employment_clean.csv")
gdp_pc = pd.read_csv("gdp_per_capita_clean.csv")
gdp_growth = pd.read_csv("gdp_growth_clean.csv")

# Merge GDP per capita + Employment
merged = pd.merge(
    gdp_pc,
    employment,
    on=["Country Name", "Country Code", "Year"],
    how="inner",
    suffixes=("_gdp_pc", "_employment")
)

# Add GDP growth
merged = pd.merge(
    merged,
    gdp_growth,
    on=["Country Name", "Country Code", "Year"],
    how="inner"
)

# Rename columns
merged.rename(columns={
    "Value_gdp_pc": "gdp_per_capita",
    "Value_employment": "employment_rate",
    "Value": "gdp_growth"
}, inplace=True)

# Keep years only relevant for project
merged = merged[(merged["Year"] >= 1990) & (merged["Year"] <= 2024)]

# Save file in processed/
merged.to_csv("merged_data.csv", index=False)

print("Merged dataset created successfully!")
print(merged.head())

