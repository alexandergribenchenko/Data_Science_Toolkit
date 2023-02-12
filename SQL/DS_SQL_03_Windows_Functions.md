# SQL - Windows Functions

## ROW_NUMBER()

´´´sql
SELECT ROW_NUMBER() OVER(Partition By Left(LastName, 1) Order BY FirstName),
´´´    

