CREATE DATABASE EmploymentManagement
GO 

CREATE TABLE Department(
DepartmentID	char(5)		PRIMARY KEY,
Name	varchar(50)		NOT NULL)

CREATE TABLE Employee(
EmployeeID		char(5)		PRIMARY KEY,
Name		varchar(50)		NOT NULL,
DepartmentFK	char(5)		NOT NULL,
BirthDate		datetime	NOT NULL)

ALTER TABLE Employee
ADD CONSTRAINT	A1
FOREIGN	KEY	(DepartmentFK)
REFERENCES	Department(DepartmentID)

INSERT INTO Department
Values('1','WEB')
INSERT INTO Department
Values('2','DEV')
INSERT INTO Department
Values('3','HR')

INSERT INTO Employee
VALUES('1','Khoa','2','2003-06-19')
INSERT INTO Employee
VALUES('2','Ha','1','2003-09-23')
INSERT INTO Employee
VALUES('3','DANG','3','2003-06-06')

IF OBJECT_ID('FnEmployees') IS NOT NULL
	DROP FUNCTION FnEmployees
GO 

CREATE FUNCTION FnEmployees
(@Name		varchar(50)		,
@DepartmentFK	char(5)		,
@BirthDate		datetime	)
RETURNS char(5)
AS
BEGIN 
	RETURN(SELECT EmployeeID
			FROM Employee
			WHERE Name=@Name AND DepartmentFK=@DepartmentFK AND BirthDate=@BirthDate)
END
SELECT dbo.FnEmployees('Ha','1','2003-09-23')

IF OBJECT_ID ('ProcDeleteDepartment') IS NOT NULL 
	DROP PROC ProcDeleteDepartment
GO

CREATE PROC ProcDeleteDepartment
@DepartmentID	char(5)
AS 
DELETE FROM Employee WHERE DepartmentFK=@DepartmentID
DELETE FROM Department WHERE DepartmentID=@DepartmentID

IF OBJECT_ID ('DELETES') IS NOT NULL 
	DROP TRIGGER DELETES
GO 

CREATE TRIGGER DELETES 
ON Employee	AFTER DELETE
AS 
	SELECT *
	FROM deleted

EXEC ProcDeleteDepartment('1')

SELECT* FROM Department
SELECT* FROM Employee




