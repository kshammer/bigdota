WITH match_ids AS (
    SELECT
        match_id
    FROM
        public_matches
    WHERE
        TRUE
        AND start_time > ?
        AND match_id < ? $ { order }
    LIMIT
        100
)
SELECT
    *
FROM
    (
        SELECT
            *
        FROM
            public_matches
        WHERE
            match_id IN (
                SELECT
                    match_id
                FROM
                    match_ids
            )
    ) matches
    JOIN (
        SELECT
            match_id,
            string_agg(hero_id :: text, ',') radiant_team
        FROM
            public_player_matches
        WHERE
            match_id IN (
                SELECT
                    match_id
                FROM
                    match_ids
            )
            AND player_slot <= 127
        GROUP BY
            match_id
    ) radiant_team USING(match_id)
    JOIN (
        SELECT
            match_id,
            string_agg(hero_id :: text, ',') dire_team
        FROM
            public_player_matches
        WHERE
            match_id IN (
                SELECT
                    match_id
                FROM
                    match_ids
            )
            AND player_slot > 127
        GROUP BY
            match_id
    ) dire_team USING(match_id)