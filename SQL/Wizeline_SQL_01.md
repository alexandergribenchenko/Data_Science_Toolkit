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
ORDER BY price*quantity DESC, name 
LIMIT 1
```
```sql
SELECT MIN(name) as name
FROM Products
WHERE price*quantity = (SELECT MAX(price*quantity) FROM Products)
```

# Q_08
```sql
SELECT name 
FROM leaderboard 
ORDER BY score DESC 
LIMIT 3,5;
```

# Q_09
```sql
SELECT	Name, 
		ID 
FROM	Grades 
WHERE	Final > (Midterm1 + Midterm2)/2 
		AND Final > ((Midterm1+Midterm2)/2 +Final)/2 
ORDER BY SUBSTRING(Name, 1, 3), ID ASC
```

# Q_10
```sql
SELECT 	(DAYOFWEEK(mischief_date) + 5) MOD 7  AS weekday,
	mischief_date, 
	author, 
	title 
FROM mischief 
ORDER BY weekday, 
	 CASE author
		WHEN 'Huey'  THEN 1
		WHEN 'Dewey' THEN 2
		WHEN 'Louie' THEN 3
		else 5 
	 END,
	 mischief_date, 
	 title
```

# Q_XX
```sql

```
# Q_XX
```sql

```
