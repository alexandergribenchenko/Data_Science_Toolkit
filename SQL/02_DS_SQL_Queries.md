
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
En este ejemplo, la CTE se llama cte_name y se define dentro de la cláusula WITH. Las columnas incluidas en la CTE son column1, column2, etc. y son las mismas que se seleccionan en la consulta de la CTE. La CTE se utiliza en la consulta principal simplemente haciendo referencia a cte_name.

Las CTE tienen varias ventajas sobre otras técnicas de subconsultas, como la claridad y la legibilidad del código, ya que la lógica de la subconsulta se encuentra en un lugar central y se puede reutilizar fácilmente. Además, también mejoran el rendimiento ya que algunos motores de base de datos pueden resolver las CTE antes de realizar la consulta principal, lo que puede mejorar la velocidad de ejecución de la consulta.
