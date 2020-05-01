select 
    public_matches.match_id
from 
    public_matches
where
    public_matches.lobby_type = 7
    and public_matches.avg_mmr > 4000
    and public_matches.start_time < {yesterday}
order by public_matches.match_id desc
limit 200