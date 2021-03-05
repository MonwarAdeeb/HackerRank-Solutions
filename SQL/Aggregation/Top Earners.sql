/*
Enter your query here.
*/
SELECT (salary * months) as earnings,
COUNT(*) FROM Employee
GROUP BY 1
ORDER BY earnings DESC
LIMIT 1;