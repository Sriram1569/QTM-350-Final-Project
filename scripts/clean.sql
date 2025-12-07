
DROP TABLE IF EXISTS gdp_per_capita;
CREATE TABLE gdp_per_capita AS
SELECT *
FROM read_csv_auto('data/raw/API_NY.GDP.PCAP.KD_DS2_en_csv_v2_2624.csv');

DROP TABLE IF EXISTS gdp_growth;
CREATE TABLE gdp_growth AS
SELECT *
FROM read_csv_auto('data/raw/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_2509.csv');

DROP TABLE IF EXISTS employment_rate;
CREATE TABLE employment_rate AS
SELECT *
FROM read_csv_auto('data/raw/API_SL.EMP.TOTL.SP.ZS_DS2_en_csv_v2_4653.csv');


