'''
Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
'''
SELECT DISTINCT CITY 
FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u') AND RIGHT(CITY,1) NOT IN ('a','e','i','o','u') 

'''
Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

Input Format
'''
SELECT Name 
FROM STUDENTS
WHERE Marks > 75
ORDER BY RIGHT(Name,3), ID ASC

'''
Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.

Input Format

The Employee table containing employee data for a company is described as follows:



where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is their monthly salary.

'''
SELECT name
FROM Employee
ORDER BY name ASC

'''
Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  per month who have been employees for less than  months. Sort your result by ascending employee_id.
'''
SELECT name
FROM Employee
WHERE salary > 2000 and months <10
ORDER BY employee_id ASC
