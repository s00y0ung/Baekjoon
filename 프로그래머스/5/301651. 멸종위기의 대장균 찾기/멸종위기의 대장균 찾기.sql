-- 코드를 작성해주세요 
with recursive g as (
    select id,1 as generation from ecoli_data where parent_id is null
    union all
    select e.id, g.generation+1 from ecoli_data as e join g on e.parent_id = g.id
)

select count(*) as count, generation
from g left join ecoli_data as e on g.id = e.parent_id
where e.id is null
group by generation
order by generation