-- 코드를 입력하세요
SELECT A.ANIMAL_ID,A.ANIMAL_TYPE,A.NAME
from ANIMAL_INS as A join ANIMAL_OUTS as B
on A.ANIMAL_ID= B.ANIMAL_ID
where A.SEX_UPON_INTAKE like "Intact%" AND (B.SEX_UPON_OUTCOME like "Spayed%" or B.SEX_UPON_OUTCOME like "Neutered%")
order by A.ANIMAL_ID