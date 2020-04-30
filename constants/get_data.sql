select 
    public_matches.match_id
    
from 
    public_matches

where
    lobby_type = 7 
    and avg_mmr > 4000
inner join 
parsed_matches on parsed_matches.match_id = public_matches.match_id
order by public_matches.match_id desc