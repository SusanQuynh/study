/* Liet ke tat ca NV co Luong tren 50000*/
SELECT*
FROM tblEmployee
WHERE empSalary> 50000
/* Create a table with the attribute that user want*/
SELECT empName AS "Ho và tên", empSalary AS "Luong"
FROM tblEmployee
WHERE empSalary> 50000
SELECT empName AS "Ho và tên",empSex AS "Gioi tính nè", ( (YEAR(GETDATE())-YEAR(empBirthday))  AS "Tuoi"
FROM tblEmployee
WHERE (empSex= 'F' and ( <40))