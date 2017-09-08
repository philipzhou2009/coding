-- https://sqliteonline.com/
-- not null
SELECT 
    name
FROM
    employees
WHERE
    id not IN (SELECT 
            managerId
        FROM
            employees where managerId is not null)


-- union
select name from dogs union select name from cats
            