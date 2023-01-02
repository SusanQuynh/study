﻿-- TAO DATABASE
CREATE DATABASE NHANSU

-- TAO TABLE PHONGBAN
CREATE TABLE DEPARTMENT (
DEPARTMENT_ID	VARCHAR(4)	PRIMARY KEY,
DEPARTMENT_NAME	VARCHAR(20)	NOT NULL,
MANAGER_ID	VARCHAR(6)	NULL,
LOCATION_ID	VARCHAR(6)	NULL)

-- TAO TABLE NHANVIEN
CREATE TABLE EMPLOYEES (
EMPLOYEE_ID	VARCHAR(12)	PRIMARY KEY,
FIRST_NAME	VARCHAR(20)	NOT NULL,
LAST_NAME	VARCHAR(25)	NOT NULL,
EMAIL	VARCHAR(25)	NOT NULL,
PHONE_NUMBER	VARCHAR(20)	NULL,
HIRE_DATE	DATE	NOT NULL,
JOB_ID	VARCHAR(10)	NOT NULL,
SALARY	DECIMAL(8,2)	NOT NULL,
COMMISSION_PCT	DECIMAL(2,2)	NULL,
MANAGER_ID	VARCHAR(6)	NULL,
DEPARTMENT_ID	VARCHAR(4)	NOT NULL)
INSERT INTO DEPARTMENT
VALUES('SE','SOFTWARE',NULL,NULL) 

INSERT INTO EMPLOYEES 
VALUES ('SE192','QUYNH','THAI','QUYNHTTA@GMAIL.COM',NULL,GETDATE(),'AI1707',1000,NULL,NULL,'SE')

-- TAO LIEN KET GIUA 2 BANG (XAC DINH FIELD KHOA NGOAI CHO TABLE NHANVIEN)
ALTER TABLE  EMPLOYEES -- BẢNG Ở QUAN HỆ NHIỀU
ADD CONSTRAINT AD001 --TỰ ĐẶT MÃ SỐ Ở ĐÂY, KHÁC BIỆT
	FOREIGN KEY (DEPARTMENT_ID) -- CỘT CHUNG CỦA 2 BẢNG 
	REFERENCES DEPARTMENT(DEPARTMENT_ID) --THAM CHIẾU ĐẾN TABLE CHỨA THUỘC TÍNH 

-- TAO TABLE HOADON
CREATE TABLE INVOICE (
INVOICE_NUMBER	NUMERIC(7) NOT NULL,
CUSTOMER_NUMBER	NUMERIC(5)	NOT NULL,
CUSTOMER_PO_NUMBER	VARCHAR(10)	NULL,
SHIP_VIA	VARCHAR(30)	NULL,
ORDER_DATE	DATE	NOT NULL)

-- THEM THUOC TINH KHOA CHINH --> THEM NHIEU FIELD LAM KHOA
ALTER TABLE INVOICE
ADD CONSTRAINT HD1
PRIMARY KEY (INVOICE_NUMBER)

-- THEM THONG TIN VAO TABLE
INSERT INTO DEPARTMENT (DEPARTMENT_ID,DEPARTMENT_NAME,MANAGER_ID,LOCATION_ID)
VALUES ('IT01','QUAN LY DU AN CNTT',NULL,NULL)
INSERT INTO DEPARTMENT
VALUES ('IT03','QUAN TRI NHAN SU', NULL,NULL)

--UPDATE THONG TIN VAO TABLE
UPDATE EMPLOYEES
SET SALARY = [SALARY]*2
WHERE DEPARTMENT_ID = 'SE'

-- XOA DU LIEU
DELETE FROM DEPARTMENT
WHERE DEPARTMENT_ID = 'IT01'
