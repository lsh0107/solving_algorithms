select 'Low Salary' as category, count(case when income < 20000 then "Low Salary" end) as accounts_count
from accounts

union all

select 'Average Salary' as category, count(case when income >= 20000 and income <= 50000 then "Average Salary" end) as accounts_count
from accounts

union all

select 'High Salary' as category, count(case when income > 50000 then "High Salary" end) as accounts_count
from accounts