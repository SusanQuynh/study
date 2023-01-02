DECLARE @A int = 1, @B int = 3, @C nvarchar(20) = N'Hello FPT'
SELECT @A, @B, @C

DECLARE @A int = 1, @B int = 3, @C nvarchar(20) = N'Hello FPT'
SELECT @A as A , @B as B, @C as C

DECLARE @A int = 1, @B int = 3, @C nvarchar(20) = N'Hello FPT'
SET @A = 20
SET @B = 50
SELECT @A as A, @B as B, @C as C

DECLARE @A int = 1, @B int = 3, @C nvarchar(20) = N'Hello FPT'
SELECT @A = 50, @B = 100 , @C = N'Hello everybody'
SELECT @A AS A, @B AS B, @C AS C

DECLARE @VendorIDVar int, @MaxInvoice money, @MinInvoice money
SET 	@VendorIDVar  =  95
SET 	@MaxInvoice  =  (SELECT MAX(InvoiceTotal) FROM Invoices WHERE VendorID  =  @VendorIDVar)

SELECT 	@MaxInvoice