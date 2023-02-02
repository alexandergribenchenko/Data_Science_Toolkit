# Examples SQL

# Example 01.
SELECT DISTINCT c.customer_id
FROM customer c, purchase_order po, order_product op, product p, product_category pc
WHERE c.customer_id=po.customer_id 
	  AND po.order_id=op.order_id 
	  AND op.product_id=p.product_id 
	  AND p.product_category_id=pc.product_category_id 
	  AND pc.name IN ('Books', 'Garden')
ORDER BY c.customer_id

# Example 02.
SELECT DISTINCT PO.customer_id
FROM PURCHASE_ORDER PO
INNER JOIN ORDER_PRODUCT OP ON PO.order_id=OP.order_id
INNER JOIN PRODUCT P ON OP.product_id=P.product_id
INNER JOIN PRODUCT_CATEGORY PC ON P.product_category_id=PC.product_category_id
WHERE PC.name IN ('Books', 'Garden')
ORDER BY PO.customer_id ASC

# Example 03.
```sql
WITH 
start_dates_pr AS
(SELECT ROW_NUMBER () OVER (ORDER BY Start_Date) AS order_number, 
        Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)), 
end_dates_pr AS
(SELECT ROW_NUMBER () OVER (ORDER BY Start_Date) AS order_number,
		End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects))

SELECT start_date, end_date, DATEDIFF(day, Start_Date, End_Date) as project_duration
FROM start_dates_pr JOIN end_dates_pr on start_dates_pr.order_number=end_dates_pr.order_number
ORDER BY project_duration ASC, Start_Date DESC
```

# Example 04.
```sql
WITH 
FILTERED_ORDERS AS
(SELECT customer_id, MAX(order_id) as order_id, MAX(order_number) as order_number
FROM (SELECT *, ROW_NUMBER () OVER (PARTITION BY customer_id ORDER BY T.date) AS order_number
	  FROM PURCHASE_ORDER T) TB
WHERE order_number<3
GROUP BY customer_id),
ORDERS_PRICE AS
(SELECT order_id, SUM(price) as total 
 FROM ORDER_PRODUCT OP LEFT JOIN PRODUCT P ON OP.product_id = P.product_id
 GROUP BY order_id)

SELECT PO.order_id, PO.customer_id, PO.date, OPR.total, FO.order_number
FROM FILTERED_ORDERS FO LEFT JOIN PURCHASE_ORDER PO ON FO.order_id=PO.order_id
			LEFT JOIN ORDERS_PRICE OPR ON OPR.order_id = FO.order_id

ORDER BY customer_id ASC
```
