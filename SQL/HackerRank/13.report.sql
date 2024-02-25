/*
Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.
*/
Select 
    Case 
        when g.grade > 7 then s.name
        else "NULL"
    end as x,
g.grade, s.marks
from Students as s
left join 
grades as g
on s.marks between g.min_mark and g.max_mark
order by
g.grade desc, 
    case 
        when g.grade > 7 then x
    end,
s.marks 
