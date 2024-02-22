'''
Query the average population of all cities in CITY where District is California.
'''
select avg(population)
from city
where district = 'california'

'''
Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
'''
select sum(population)
from city
where countrycode = 'JPN'

'''
Query the difference between the maximum and minimum populations in CITY.
'''
select (max(population) - min(population))
from city
