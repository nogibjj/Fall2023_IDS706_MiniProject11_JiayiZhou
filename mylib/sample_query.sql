SELECT team AS Team, COUNT(*) AS TotalMatchesPlayed
            FROM (SELECT team1 AS team FROM default.matchesdb_one
                UNION ALL
                SELECT team2 AS team FROM default.matchesdb_one
                UNION ALL
                SELECT team1 AS team FROM default.wwc_matches_2_db
                UNION ALL
                SELECT team2 AS team FROM default.wwc_matches_2_db
                ) AS AllTeams
            GROUP BY Team
            ORDER BY TotalMatchesPlayed DESC;