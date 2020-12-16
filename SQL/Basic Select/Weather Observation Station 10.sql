/*
Enter your query here.
*/
select DISTINCT city from STATION where city NOT REGEXP '[aeiou]$';