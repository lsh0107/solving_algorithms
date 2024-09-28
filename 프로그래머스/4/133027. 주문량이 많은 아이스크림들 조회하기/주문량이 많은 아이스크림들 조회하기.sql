-- 코드를 입력하세요
SELECT fh.flavor
from first_half fh
left join (select flavor, sum(total_order) as total
           from july 
           group by flavor) j
on fh.flavor = j.flavor
group by fh.flavor
order by sum(fh.total_order + ifnull(j.total, 0)) desc
limit 3


