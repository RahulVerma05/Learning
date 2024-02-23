/*
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with  sides of equal length.
Isosceles: It's a triangle with  sides of equal length.
Scalene: It's a triangle with  sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.
*/

select  case 
when A+B > C and B+C >A and C+A > B  then
case 
when A = B and B = C then 'Equilateral'
when A=B or A=C or B=C then 'Isosceles'
else 'Scalene' end
else 'Not A Triangle' end
from Triangles

/* 
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.:  average monthly salaries), and round it up to the next integer.
*/

select ceil(avg(salary) - avg(replace(salary,'0','')))
from employees
