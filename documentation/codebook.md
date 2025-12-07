# Codebook – WDI Merged Dataset (USA & China, 1990–2023)

This dataset merges three World Bank WDI indicators for the United States (USA) and China (CHN).  
All raw files share the same structure:

- **Country Name**
- **Country Code** (ISO3)
- **Year**
- **Value**

---

## Variables in Final Cleaned Dataset

### Identification Columns
| Variable | Description |
|---------|-------------|
| **country_name** | Country name (“China”, “United States”) |
| **iso3** | ISO3 country code (`CHN`, `USA`) |
| **year** | Calendar year (int) |

---

## Economic Indicators

### **1. Employment Rate**
- **Variable name:** `employment_rate`  
- **Source file:** employment_clean.csv  
- **WDI Code:** `SL.EMP.TOTL.SP.ZS`  
- **Definition:** Employment-to-population ratio, ages 15+, total (%)  

### **2. GDP Growth**
- **Variable name:** `gdp_growth`  
- **Source file:** gdp_growth.csv  
- **WDI Code:** `NY.GDP.MKTP.KD.ZG`  
- **Definition:** Annual percentage growth rate of real GDP.  

### **3. GDP Per Capita**
- **Variable name:** `gdp_per_capita`  
- **Source file:** gdp_per_capita_clean.csv  
- **WDI Code:** `NY.GDP.PCAP.KD`  
- **Definition:** GDP per capita (constant 2015 US dollars).  

---

## Cleaning Summary

1. Loaded the three raw WDI files.  
2. Standardized column names:
   - `Country Name` → `country_name`  
   - `Country Code` → `iso3`  
   - `Value` → indicator-specific variable names  
3. Converted `year` from float to integer.  
4. Filtered dataset to:
   - Countries: **USA** and **CHN**  
   - Years: **1990–2023**  
5. Merged the three datasets on `iso3` and `year`.  
6. Converted numeric fields; coerced invalid strings to NaN.  
7. Removed rows missing any indicator (listwise deletion).  
8. Saved merged dataset to:
