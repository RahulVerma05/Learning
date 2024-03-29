'''
Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than . Truncate your answer to  decimal places.
'''
select Truncate(max(LAT_N),4)
from station
where LAT_N < 137.2345

'''
Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.
'''
select round(LONG_W,4)
from station
where LAT_N = (select max(LAT_N) 
               from station 
               where LAT_N< 137.2345)
'''
Query the smallest Northern Latitude (LAT_N) from STATION that is greater than . Round your answer to  decimal places.
'''
select round(min(LAT_N),4)
from station
where LAT_N > 38.7780

'''
Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than . Round your answer to  decimal places.
'''
select round(LONG_W,4)
from station
where LAT_N = (select min(LAT_N)
              from station
              where LAt_N > 38.7780)
