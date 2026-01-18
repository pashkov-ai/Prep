SELECT DISTINCT title
FROM TVProgram
LEFT Join Content
ON TVProgram.content_id = Content.content_id
WHERE Kids_content = 'Y'AND content_type = 'Movies'
AND MONTH(program_date) = 6 AND YEAR(program_date) = 2020