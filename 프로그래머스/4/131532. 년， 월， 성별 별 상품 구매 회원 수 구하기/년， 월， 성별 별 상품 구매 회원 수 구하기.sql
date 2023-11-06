-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) as YEAR	,MONTH(SALES_DATE) as MONTH	,a.GENDER	,count(DISTINCT a.USER_ID) as USERS
from USER_INFO as a
join ONLINE_SALE as b
on a.USER_ID=b.USER_ID
where GENDER is not null
group by  YEAR	,MONTH	,GENDER	
order by YEAR	,MONTH	,GENDER	