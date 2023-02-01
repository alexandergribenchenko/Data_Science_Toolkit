# Cheatsheet PostgreSQL

```sql
DROP TABLE IF EXISTS countryregioncurrency, currencyrate;

CREATE TABLE countryregioncurrency (
countryregioncode VARCHAR(3),
currencycode CHAR(3),
modifieddate DATE
);

CREATE TABLE currencyrate (
currencyrateid INTEGER,
currencyratedate DATE,
fromcurrencycode CHAR(3),
tocurrencycode CHAR(3),
averagerate FLOAT,
endofdayrate FLOAT,
modifieddate DATE
);

COPY countryregioncurrency 
FROM 'C:\Users\User\Downloads\extended_case_3_student\data\csvs\countryregioncurrency.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');

COPY currencyrate 
FROM 'C:\Users\User\Downloads\extended_case_3_student\data\csvs\currencyrate.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');
```
