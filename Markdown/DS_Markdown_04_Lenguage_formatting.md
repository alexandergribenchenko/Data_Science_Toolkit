
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```


```excel
=BUSCARV(E2;Jugadores!$A$2:$B$346;2;FALSO)
```

```sql
SELECT customer_id, 
        CASE
            WHEN COUNT(order_id) = 1 THEN MAX(order_id)
            WHEN COUNT(order_id) != 1 THEN MAX(order_id)
        END selc_order_id
FROM (SELECT *, ROW_NUMBER () OVER (PARTITION BY customer_id ORDER BY T.date) AS RN
	  FROM PURCHASE_ORDER T) TB
WHERE RN<3
GROUP BY customer_id
```

```python
def suma(a,b):
	return(a+b)
```

```sql
def suma(a,b):
	return(a+b)
```
