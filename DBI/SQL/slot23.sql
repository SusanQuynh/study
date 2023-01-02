USE AP 
IF OBJECT_ID('spCopyinvoices') IS NOT NULL
DROP PROC spCopyInvoices
GO

CREATE PROC spCopyInvoices
AS 
	IF OBJECT_ID('spCopyInvoices') IS NOT NULL
		DROP TABLE InvoiceCopy
	SELECT* INTO InvoiceCopy FROM Invoices


CREATE PROCEDURE spInvTotal1
	@InvTotal   money OUTPUT,
	@DateVar    smalldatetime,
	@VendorVar  varchar(40) = '%'
AS
IF @DateVar IS NULL
	SELECT @DateVar = MIN(InvoiceDate) FROM Invoices

SELECT @InvTotal = SUM(InvoiceTotal)
FROM Invoices JOIN Vendors
ON Invoices.VendorID = Vendors.VendorID
WHERE (InvoiceDate >= @DateVar) AND (VendorName LIKE @VendorVar)

DECLARE @MyInvTotal money
EXEC spInvTotal1 @MyInvTotal OUTPUT, '2008-06-01', 'P%'
SELECT @MyInvTotal

DECLARE @MyInvTotal1 money
EXEC    spInvTotal1   @DateVar = '2008-06-01', @VendorVar = 'P%', @InvTotal = @MyInvTotal OUTPUT
SELECT @MyInvTotal1

DECLARE  @MyInvTotal2 money
EXEC     spInvTotal1   @DateVar = '2008-06-01', @InvTotal = @MyInvTotal OUTPUT
SELECT   @MyInvTotal2



CREATE PROC spInvCount
       @DateVar   smalldatetime = NULL,
       @VendorVar varchar(40) = '%'
AS
IF @DateVar IS NULL
   SELECT @DateVar  =  MIN(InvoiceDate)  FROM  Invoices
  
DECLARE @InvCount int
SELECT   @InvCount  =  COUNT(InvoiceID)
FROM Invoices  JOIN  Vendors
ON Invoices.VendorID = Vendors.VendorID
WHERE ((InvoiceDate >= @DateVar) AND (VendorName LIKE @VendorVar))
RETURN @InvCount

DECLARE  @InvCount1 int
EXEC @InvCount1 = spInvCount '2008-06-01', 'P%'
PRINT 'Invoice count: ' + CONVERT(varchar, @InvCount)

CREATE VIEW OUTSANDING