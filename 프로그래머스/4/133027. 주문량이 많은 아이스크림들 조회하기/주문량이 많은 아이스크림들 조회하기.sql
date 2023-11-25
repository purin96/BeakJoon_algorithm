-- 코드를 입력하세요
SELECT A.FLAVOR
from FIRST_HALF as A join JULY as B
on A.FLAVOR=B.FLAVOR
group by FLAVOR
order by sum(A.TOTAL_ORDER+ B.TOTAL_ORDER) DESC
limit 3