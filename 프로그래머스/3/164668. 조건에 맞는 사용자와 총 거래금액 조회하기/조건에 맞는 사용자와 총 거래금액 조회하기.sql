-- 코드를 입력하세요
SELECT b.USER_ID,b.NICKNAME,SUM(PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as a
join USED_GOODS_USER as b
on a.WRITER_ID=b.USER_ID
where STATUS="DONE"
GROUP by a.WRITER_ID
HAVING TOTAL_SALES >=700000
ORDER BY TOTAL_SALES