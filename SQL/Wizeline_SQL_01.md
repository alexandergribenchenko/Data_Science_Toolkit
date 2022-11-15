# Q_01
```sql
SELECT project_name, team_lead, income
FROM Projects
ORDER BY internal_id ASC
```

# Q_02
```sql
SELECT * 
FROM countries 
WHERE continent = 'Africa'
ORDER BY name ASC
```

# Q_03
```sql
SELECT  id, 
        (scholarship / 12) AS scholarship 
FROM scholarships
ORDER BY id ASC
ORDER BY name ASC
```

# Q_04
```sql
SELECT DISTINCT name 
FROM projectLog 
ORDER BY name ASC
```

# Q_05
```sql
SELECT email
FROM users
WHERE role NOT IN ("admin", "premium")
ORDER BY email
```

# Q_06
```sql
SELECT *
FROM results
ORDER BY wins
```

# Q_07
```sql
SELECT name
FROM Products
ORDER BY price*quantity DESC, name LIMIT 1
```
```sql
SELECT MIN(name) as name
FROM Products
WHERE price*quantity = (SELECT MAX(price*quantity) FROM Products)
```

# Q_08
```sql

```

# Q_XX
```sql

```

# Q_XX
```sql

```

# Q_XX
```sql

```
# Q_XX
```sql

```
