/*
Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:

Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.
*/
select c.company_code, c.founder, count(distinct(l.lead_manager_code)), count(distinct(s.senior_manager_code)), count(distinct(m.manager_code)) ,count(distinct(e.employee_code)) 
            
from Company as c
Inner join Lead_Manager as l
On c.company_code = l.company_code

Inner join Senior_Manager as s
On c.company_code = s.company_code

Inner join Manager as m
On c.company_code = m.company_code

Inner join Employee as e
On c.company_code = e.company_code

group by c.company_code, c.founder
order by c.company_code
