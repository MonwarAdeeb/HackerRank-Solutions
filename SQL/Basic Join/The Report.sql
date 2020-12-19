/*
Enter your query here.
*/
SELECT Students.Name, Grades.Grade, Students.Marks FROM Students INNER JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark WHERE Grades.Grade > 7 ORDER BY Grades.Grade DESC, Students.Name ASC;
SELECT null, Grades.Grade, Students.Marks FROM Students INNER JOIN Grades ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark WHERE Grades.Grade <= 7 ORDER BY Grades.Grade DESC, Students.Marks ASC;