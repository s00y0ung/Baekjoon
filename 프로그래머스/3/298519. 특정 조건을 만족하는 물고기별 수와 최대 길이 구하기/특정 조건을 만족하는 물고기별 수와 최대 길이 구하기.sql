select count(*) FISH_COUNT, max(LENGTH) MAX_LENGTH,fish_type
from fish_info
group by fish_type
having avg(if(LENGTH is null,10,LENGTH))>=33
order by fish_type