-- 코드를 작성해주세요
select a.id, b.fish_name, a.length
from fish_info as a join fish_name_info as b on a.fish_type = b.fish_type
where a.length = (select max(length) from fish_info as c where c.fish_type = a.fish_type)
order by a.id