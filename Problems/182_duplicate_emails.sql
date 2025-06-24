SELECT a.email
FROM Person a
GROUP BY a.email
HAVING COUNT(*) > 1
;
