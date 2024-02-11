'''
Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
'''

Select Name from City
where population > 120000
and Countrycode = 'USA'
