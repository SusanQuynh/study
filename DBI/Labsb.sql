IF OBJECT_ID('spBalanceRange') IS NOT NULL
	DROP PROC spBalanceRange
GO

CREATE PROC spBalanceRange
	@VendorVar varchar(50) = NULL,
	@BalanceMin money = 0,
	@BalanceMax money = NULL
AS
	IF @BalanceMax IS NULL
		SELECT @BalanceMax = MAX(InvoiceTotal-PaymentTotal-CreditTotal) FROM Invoices
	IF @VendorVar IS NULL
		SELECT @VendorVar = '%'
	SELECT v.VendorName, i.InvoiceNumber, i.InvoiceTotal-i.PaymentTotal-i.CreditTotal AS BalanceDue
	FROM Vendors v, Invoices i
	WHERE v.VendorID = i.VendorID
			AND v.VendorName LIKE @VendorVar
			AND (i.InvoiceTotal-i.PaymentTotal-i.CreditTotal) >= @BalanceMin
			AND (i.InvoiceTotal-i.PaymentTotal-i.CreditTotal) <= @BalanceMax
	ORDER BY BalanceDue DESC
GO

EXEC spBalanceRange @VendorVar='Z%'

EXEC spBalanceRange @BalanceMin=200, @BalanceMax=1000

EXEC spBalanceRange @VendorVar='[FC]%', @BalanceMax=200