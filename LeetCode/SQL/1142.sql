SELECT ROUND(IFNULL(AVG(session_count), 0), 2) as average_sessions_per_user
FROM (
    WITH Constants as
        (SELECT "2019-07-27" as query_date, 30 as query_interval)
    SELECT COUNT(DISTINCT session_id) AS session_count
    FROM Activity, Constants C
    WHERE activity_date BETWEEN DATE_SUB(C.query_date, INTERVAL C.query_interval - 1 DAY) AND C.query_date
    GROUP BY user_id
) AS T