# Cheatsheet PostgreSQL

Enlaces de interes: 
- [Cómo añadir PostgreSQL a las variables de entorno de Windows 10](https://remot-technologies.com/como-anadir-postgresql-a-las-variables-de-entorno-de-windows-10/)

## Query 00.
```sql
CREATE DATABASE db_Test;
```

## Query 01.
```sql
SELECT *
FROM currencyrate
```

## Query 02.
```sql
SELECT t_03.productid, t_03.name, ROUND(AVG(t_07.rating),2) AS avg_rating
FROM product t_03
INNER JOIN productreview t_07 ON t_03.productid = t_07.productid
GROUP BY  t_03.productid, t_03.name
ORDER BY avg_rating DESc
LIMIT 5
```


## Query 03.
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
## Query 04.
```sql
DROP TABLE IF EXISTS product, productreview;

-- t_03 : product
CREATE TABLE product (
productid INTEGER,
name VARCHAR(50),
productnumber VARCHAR(25),
makeflag CHAR(1),
finishedgoodsflag CHAR(1),
color VARCHAR(15),
safetystocklevel INTEGER,
reorderpoint INTEGER,
standardcost FLOAT,
listprice FLOAT,
size VARCHAR(5),
sizeunitmeasurecode CHAR(3),
weightunitmeasurecode CHAR(3),
weight FLOAT,
daystomanufacture INTEGER,
productline CHAR(2),
class CHAR(2),
style CHAR(2),
productsubcategoryid INTEGER,
productmodelid INTEGER,
sellstartdate DATE,
sellenddate DATE,
discontinueddate DATE,
rowguidcol TEXT,
modifieddate DATE
);

-- t_07 : productreview
CREATE TABLE productreview (
productreviewid INTEGER,
productid INTEGER,
reviewername VARCHAR(50),
reviewdate DATE,
emailaddress VARCHAR(50),
rating INTEGER,
comments VARCHAR(3850),
modifieddate DATE
);

COPY product 
FROM 'C:\Users\User\Downloads\extended_case_3_student\data\csvs\product.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',', ENCODING 'UTF8');

COPY productreview 
FROM 'C:\Users\User\Downloads\extended_case_3_student\data\csvs\productreview.csv'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',', ENCODING 'UTF8');
```
