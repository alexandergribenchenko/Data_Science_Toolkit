
# CTEs (Expresiones Comunes Temporales)
Las Expresiones Comunes Temporales (CTE, por sus siglas en inglés) son una característica de SQL que permiten crear subconsultas de forma más clara y legible. Una CTE es una consulta que se define dentro de la cláusula WITH en una consulta principal y se puede utilizar varias veces en la misma consulta, sin tener que repetir la misma lógica en múltiples ocasiones.

La sintaxis básica para crear una CTE es la siguiente:

```sql
WITH cte_name (column1, column2, ...) AS (
  SELECT column1, column2, ...
  FROM table_name
  WHERE condition
)
SELECT ...
FROM cte_name
```
