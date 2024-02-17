'''
Query the following two values from the STATION table:

The sum of all values in LAT_N rounded to a scale of  decimal places.
The sum of all values in LONG_W rounded to a scale of  decimal places
'''
select  round(sum(LAT_N),2), round(sum(LONG_W),2)
from Station

'''
Query a count of the number of cities in CITY having a Population larger than 100000.
'''
select count(name)
from city
where Population > 100000

'''
Query the total population of all cities in CITY where District is California.
'''
select sum(population)
from city
where district = 'California'

'''
Query the average population for all cities in CITY, rounded down to the nearest integer.
'''
select round(avg(population),0)
from city
