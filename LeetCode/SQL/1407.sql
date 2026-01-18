SELECT
    name, IFNULL(SUM(distance), 0) as travelled_distance
FROM Users
LEFT JOIN Rides
ON Rides.user_id = Users.id
GROUP BY user_id
ORDER BY travelled_distance DESC, name ASC