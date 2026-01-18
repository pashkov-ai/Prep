SELECT -- window function
    DISTINCT player_id,
    FIRST_VALUE(device_id) OVER (PARTITION BY player_id ORDER BY event_date ASC) as device_id
FROM Activity