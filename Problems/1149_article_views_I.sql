SELECT DISTINCT(author_id) AS id
FROM Views
WHERE author_id = viewer_id

GROUP BY author_id, view_date
HAVING COUNT(*) > 1

ORDER BY author_id ASC
;
