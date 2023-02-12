# SQL - Windows Functions

## ROW_NUMBER()

```sql
SELECT id_vuelo, fecha_salida, fecha_llegada, aeronave, aeropuerto_origen,
       ROW_NUMBER() OVER (ORDER BY aeronave) AS secuencia_row_number
FROM vuelos;

SELECT id_vuelo, fecha_salida, fecha_llegada, aeronave, aeropuerto_origen,
       ROW_NUMBER() OVER (PARTITION BY aeropuerto_origen) AS secuencia_row_number
FROM vuelos;

SELECT id_vuelo, fecha_salida, fecha_llegada, aeronave, aeropuerto_origen,
       ROW_NUMBER() OVER (PARTITION BY aeropuerto_origen ORDER BY aeronave) AS secuencia_row_number
FROM vuelos;
```   

