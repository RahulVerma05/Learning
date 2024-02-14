'''
1.
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
'''
SELECT DISTINCT CITY 
FROM STATION
WHERE RIGHT(CITY,1) IN ('a','e','i','o','u')


'''
2.
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
'''
SELECT DISTINCT CITY 
FROM STATION
WHERE LEFT(CITY,1) IN ('a','e','i','o','u') AND RIGHT(CITY,1) IN ('a','e','i','o','u') 

'''
3.
Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
'''
SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u')

'''
4.
Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
'''
SELECT DISTINCT CITY
FROM STATION
WHERE RIGHT(CITY,1) NOT IN ('a','e','i','o','u')

'''
5.
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
'''
SELECT DISTINCT CITY 
FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u') OR RIGHT(CITY,1) NOT IN ('a','e','i','o','u') 
