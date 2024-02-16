'''
Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.
'''
select sum(city.Population) 
from CITY
RIGHT JOIN COUNTRY
ON CITY.CountryCode = COUNTRY.Code
where Continent = 'Asia'

'''
Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
'''
select CITY.NAME
from CITY
INNER JOIN COUNTRY
ON CITY.CountryCode = COUNTRY.Code
where Continent = 'Africa'

'''
Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer
'''
select COUNTRY.Continent, floor(avg(CITY.POPULATION))
from CITY
INNER JOIN COUNTRY
ON CITY.CountryCode = COUNTRY.Code
Group by COUNTRY.Continent
