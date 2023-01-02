-- Y1
-- Create database
CREATE DATABASE QLNHATRO_NHOM2 
GO
-- Use database
USE QLNHATRO_NHOM2
GO
-- Create NGUOIDUNG table
CREATE TABLE NGUOIDUNG (
	MAND		int				PRIMARY KEY,
	TENND		nvarchar(20)	NOT NULL,
	GIOITINH	bit				NOT NULL,
	DIENTHOAI	varchar(11)		NOT NULL,
	DIACHI		nvarchar(50)	NOT NULL,
	QUAN		nvarchar(50)	NOT NULL,
	EMAIL		varchar(50)		NOT NULL)
GO
-- Create LOAINHA table
CREATE TABLE LOAINHA (
	MALOAINT	varchar(2)		PRIMARY KEY,
	TENLOAINT	nvarchar(50)	NOT NULL)
GO
-- Create NHATRO table
CREATE TABLE NHATRO (
	MANT			int				PRIMARY KEY,
	LOAIHINHNT		varchar(2)		NOT NULL,
	DIENTICH		int				NOT NULL,
	GIAPHONG		money			NOT NULL,
	DIACHINT		nvarchar(50)	NOT NULL,
	QUAN			nvarchar(50)	NOT NULL,
	MOTA			nvarchar(50)	NOT NULL,
	NGAYDANG		date			NOT NULL,
	NGUOILIENHE		int				NOT NULL
	FOREIGN KEY (NGUOILIENHE) REFERENCES NGUOIDUNG(MAND),
	FOREIGN KEY (LOAIHINHNT) REFERENCES LOAINHA(MALOAINT))
GO
-- Create DANHGIA table
CREATE TABLE DANHGIA (
	MADG			int				PRIMARY KEY,
	NGUOIDG			int				NOT NULL,
	CHATLUONG		nvarchar(20)	NOT NULL,
	TRANGTHAIDG		bit				NOT NULL,
	NOIDUNGDG		nvarchar(50)	NOT NULL,
	MANT			int				NOT NULL,
	FOREIGN KEY (NGUOIDG) REFERENCES NGUOIDUNG(MAND),
	FOREIGN KEY (MANT)	REFERENCES NHATRO(MANT) ON DELETE CASCADE)
GO
-- Y2. Yêu cầu về bộ dữ liệu mẫu
-- Insert values into NGUOIDUNG table
INSERT INTO NGUOIDUNG
	VALUES (1, N'Minh', 0, '0978173990', N'506 Ba Tháng Hai', N'Quận 10', 'minhtn@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (2, N'Tâm', 1, '0123456789', N'7 Lý Thường Kiệt', N'Quận 10', 'tamlt@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (3, N'Lộc', 1, '01884981234', N'4 Ngô Gia Tự', N'Quận 10', 'loccd@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (4, N'Hoàn', 1, '0912345678', N'8 Điện Biên Phủ', N'Quận Bình Thạnh', 'hoannv@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (5, N'Nhân', 1, '09674456123', N'7 Điện Biên Phủ', N'Quận Bình Thạnh', 'nhannt@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (6, N'Hiếu', 1, '0965234567', N'8 Nguyễn Thái Sơn', N'Quận Gò Vấp', 'hieunt@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (7, N'Dung', 0, '0956123456', N'10 CMT8', N'Quận 1', 'dungnt@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (8, N'Yến', 0, '0977456789', N'23 Lý Tự Trọng', N'Quận 1', 'yentm@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (9, N'Anh', 0, '0945321654', N'610 Nguyễn Trãi', N'Quận 5', 'anhnt@gmail.com')
INSERT INTO NGUOIDUNG
	VALUES (10, N'Thịnh', 1, '0166894567', N'20 Kinh Dương Vương', N'Quận Bình Tân', 'thinhtpn@gmail.com')
GO
-- Insert values into LOAINHA table
INSERT INTO LOAINHA VALUES ('CC', N'Chung cư')
INSERT INTO LOAINHA VALUES ('NR', N'Nhà riêng')
INSERT INTO LOAINHA VALUES ('PT', N'Phòng trọ')
GO
-- Insert values into NHATRO table
INSERT INTO NHATRO
	VALUES (100, 'CC', 100, 10000000, N'23 Lý Thường Kiệt', N'Quận 10', N'Thoáng mát', '2013-01-22', 3)
INSERT INTO NHATRO
	VALUES (101, 'NR', 300, 30000000, N'73 Nơ Trang Long', N'Quận Bình Thạnh', N'Sạch sẽ', '2013-01-12', 5)
INSERT INTO NHATRO
	VALUES (102, 'PT', 25, 2000000, N'606 Ba Tháng Hai', N'Quận 10', N'An ninh', '2013-10-06', 1)
INSERT INTO NHATRO
	VALUES (103, 'PT', 35, 3000000, N'656 CMT8', N'Quận 10', N'Phòng đúc', '2013-09-09', 2)
INSERT INTO NHATRO
	VALUES (104, 'NR', 400, 60000000, N'8 Nguyễn Trãi', N'Quận 5', N'Mặt tiền', '2013-04-05', 1)
INSERT INTO NHATRO
	VALUES (105, 'NR', 300, 80000000, N'2 Bùi Thị Xuân', N'Quận 1', N'Mới xây', '2013-02-03', 1)
INSERT INTO NHATRO
	VALUES (106, 'CC', 150, 60000000, N'6 Ngô Gia Tự', N'Quận 10', N'Gần trường học', '2013-03-04', 4)
INSERT INTO NHATRO
	VALUES (107, 'CC', 600, 100000000, N'1 Nguyễn Du', N'Quận 1', N'Ngay trung tâm', '2013-02-03', 8)
INSERT INTO NHATRO
	VALUES (108, 'PT', 14, 1500000, N'2 Bạch Đằng', N'Quận Bình Thạnh', N'Gần chợ', '2013-05-06', 2)
INSERT INTO NHATRO
	VALUES (109, 'PT', 25, 3000000, N'6 Hoàng Văn Thụ', N'Quận Tân Bình', N'Gần sân bay', '2013-09-04', 6)
INSERT INTO NHATRO
	VALUES (110, 'CC', 250, 60000000, N'2D City Land', N'Quận 7', N'Mới xây', '2013-05-06', 9)
GO
-- Insert values into DANHGIA table
INSERT INTO DANHGIA VALUES (500, 8, N'Tốt', 1, N'Đẹp', 103)
INSERT INTO DANHGIA VALUES (501, 6, N'Kém', 0, N'Không an ninh', 108)
INSERT INTO DANHGIA VALUES (502, 8, N'Trung Bình', 0, N'Thiếu ánh sáng', 104)
INSERT INTO DANHGIA VALUES (503, 2, N'Tốt', 1, N'Giá cả hợp lý', 102)
INSERT INTO DANHGIA VALUES (504, 7, N'Tốt', 1, N'Giao thông thuận lợi', 108)
INSERT INTO DANHGIA VALUES (505, 1, N'Trung Bình', 0, N'Không an ninh', 104)
INSERT INTO DANHGIA VALUES (506, 8, N'Tốt', 1, N'Nhà đẹp', 103)
INSERT INTO DANHGIA VALUES (507, 9, N'Kém', 0, N'Ồn ào', 109)
INSERT INTO DANHGIA VALUES (508, 6, N'Trung Bình', 0, N'Đường đi hẹp', 105)
INSERT INTO DANHGIA VALUES (509, 3, N'Tốt', 1, N'Chủ nhà tốt', 107)
INSERT INTO DANHGIA VALUES (510, 8, N'Tốt', 1, N'Giá tốt', 103)
GO
-- Y3
-- 1. Thêm thông tin vào các bảng
-- SP thực hiện chèn dữ liệu vào bảng NGUOIDUNG
IF OBJECT_ID('spInsertNGUOIDUNG') IS NOT NULL
	DROP PROC spInsertNGUOIDUNG
GO
CREATE PROC spInsertNGUOIDUNG
	@MAND int = NULL,
	@TENND nvarchar(10) = NULL,
	@GIOITINH bit = NULL,
	@DIENTHOAI varchar(11) = NULL,
	@DIACHI nvarchar(50) = NULL,
	@QUAN nvarchar(50) = NULL,
	@EMAIL varchar(50) = NULL
AS
	BEGIN TRY
		BEGIN TRAN
			IF (@MAND IS NULL) OR (@TENND IS NULL) OR (@GIOITINH IS NULL) OR (@DIENTHOAI IS NULL) OR
			   (@DIACHI IS NULL) OR (@QUAN IS NULL) OR (@EMAIL IS NULL)
				BEGIN
					PRINT N'Hãy nhập dữ liệu đầy đủ'
					ROLLBACK TRAN
				END
			ELSE
				BEGIN
					INSERT INTO NGUOIDUNG VALUES (@MAND, @TENND, @GIOITINH, @DIENTHOAI, @DIACHI, @QUAN, @EMAIL)
					COMMIT TRAN
					PRINT N'Thêm mới thông tin thành công'
				END
	END TRY
	BEGIN CATCH
		PRINT N'Hãy kiểm tra dữ liệu nhập'
		ROLLBACK TRAN
	END CATCH
GO
EXEC spInsertNGUOIDUNG 
	@MAND=11, 
	@TENND=N'Thịnh', 
	@GIOITINH=1, 
	@DIENTHOAI='0166666567', 
	@DIACHI=N'20 Hùng Vương', 
	@QUAN=N'Quận 9', 
	@EMAIL='thinhdt@gmail.com'
EXEC spInsertNGUOIDUNG 
	@MAND=12, 
	@TENND=N'Bình', 
	@GIOITINH=1, 
	@DIENTHOAI='0160006567', 
	@DIACHI=N'69 Tân Kỳ Tân Quý', 
	@QUAN=N'Quận Thủ Đức'
GO
-- SP thực hiện chèn dữ liệu vào bảng NHATRO
IF OBJECT_ID('spInsertNHATRO') IS NOT NULL
	DROP PROC spInsertNHATRO
GO
CREATE PROC spInsertNHATRO
	@MANT int = NULL,
	@LOAIHINHNT varchar(2) = NULL,
	@DIENTICH int = NULL,
	@GIAPHONG money = NULL,
	@DIACHINT nvarchar(50) = NULL,
	@QUAN nvarchar(50) = NULL,
	@MOTA nvarchar(50) = NULL,
	@NGAYDANG date = NULL,
	@NGUOILIENHE int = NULL
AS
	BEGIN TRY
		BEGIN TRAN
			IF (@MANT IS NULL) OR (@LOAIHINHNT IS NULL) OR (@DIENTICH IS NULL) OR (@GIAPHONG IS NULL) OR (@DIACHINT IS NULL) OR
			   (@QUAN IS NULL) OR (@MOTA IS NULL) OR (@NGAYDANG IS NULL) OR (@NGUOILIENHE IS NULL)
				BEGIN
					PRINT N'Hãy nhập dữ liệu đầy đủ'
					ROLLBACK TRAN
				END
			ELSE
				BEGIN
					INSERT INTO NHATRO VALUES (@MANT, @LOAIHINHNT, @DIENTICH, @GIAPHONG, @DIACHINT, @QUAN, @MOTA, @NGAYDANG, @NGUOILIENHE)
					COMMIT TRAN
					PRINT N'Thêm mới thông tin thành công'
				END
	END TRY
	BEGIN CATCH
		PRINT N'Hãy kiểm tra dữ liệu nhập'
		ROLLBACK TRAN
	END CATCH
GO
EXEC spInsertNHATRO
	@MANT = 111,
	@LOAIHINHNT = 'CC',
	@DIENTICH = 65,
	@GIAPHONG = 6000.0000,
	@DIACHINT = N'Vinhome Grand Park',
	@QUAN = N'Quận 9',
	@MOTA = N'Đầy đủ tiện nghi',
	@NGAYDANG = '2022-08-03',
	@NGUOILIENHE = 11
EXEC spInsertNHATRO
	@MANT = 112,
	@LOAIHINHNT = 'CC',
	@DIENTICH = 60,
	@GIAPHONG = 6500.0000,
	@DIACHINT = N'Chung cư Sky9',
	@QUAN = N'Quận 9',
	@MOTA = N'An ninh tốt',
	@NGUOILIENHE = 12
GO
-- SP thực hiện chèn dữ liệu vào bảng DANHGIA
IF OBJECT_ID('spInsertDANHGIA') IS NOT NULL
	DROP PROC spInsertDANHGIA
GO
CREATE PROC spInsertDANHGIA
	@MADG int = NULL,
	@NGUOIDG int = NULL,
	@CHATLUONG	nvarchar(20) = NULL,
	@TRANGTHAIDG bit = NULL,
	@NOIDUNGDG nvarchar(50) = NULL,
	@MANT int = NULL
AS
	BEGIN TRY
		BEGIN TRAN
			IF (@MADG IS NULL) OR (@NGUOIDG IS NULL) OR (@CHATLUONG IS NULL) OR (@TRANGTHAIDG IS NULL) OR
			   (@NOIDUNGDG IS NULL) OR (@MANT IS NULL)
				BEGIN 
					PRINT N'Hãy nhập dữ liệu đầy đủ'
					ROLLBACK TRAN
				END
			ELSE
				BEGIN
					INSERT INTO DANHGIA VALUES (@MADG, @NGUOIDG, @CHATLUONG, @TRANGTHAIDG, @NOIDUNGDG, @MANT)
					COMMIT TRAN
					PRINT N'Thêm thông tin thành công'
				END
	END TRY
	BEGIN CATCH
		PRINT N'Hãy kiểm tra dữ liệu nhập'
		ROLLBACK TRAN
	END CATCH
GO
EXEC spInsertDANHGIA
	@MADG = 511,
	@NGUOIDG = 11,
	@CHATLUONG = N'Tốt',
	@TRANGTHAIDG = 1,
	@NOIDUNGDG = N'Đẹp',
	@MANT = 111
EXEC spInsertDANHGIA
	@MADG = 512,
	@CHATLUONG = N'Trung bình',
	@TRANGTHAIDG = 1,
	@NOIDUNGDG = N'Hơi nóng',
	@MANT = 111
GO
-- 2. Truy vấn thông tin
-- a. SP thực hiện tìm kiếm thông tin các phòng trọ thoả mãn điều kiện tìm kiếm theo: 
--		quận, phạm vi diện tích, phạm vi ngày đăng tin, khoảng giá tiền, loại hình nhà trọ
--	  SP này trả về thông tin các phòng trok, gồm các cột có định dạng sau:
--		* Cột thứ nhất: có định dạng ‘Cho thuê phòng  trọ tại’ + <Địa chỉ phòng trọ> + <Tên quận/Huyện>
--		* Cột thứ hai: Hiển thị diện tích phòng trọ dưới định dạng số theo chuẩn Việt Nam + m2. Ví dụ 30,5 m2
--		* Cột thứ ba: Hiển thị thông tin giá phòng dưới định dạng số theo định dạng chuẩn Việt Nam. Ví dụ 1.700.000
--		* Cột thứ tư: Hiển thị thông tin mô tả của phòng trọ
--		* Cột thứ năm: Hiển thị ngày đăng tin dưới định dạng chuẩn Việt Nam. Ví dụ: 27-02-2012
--		* Cột thứ sáu: Hiển thị thông tin người liên hệ dưới định dạng sau:
--			Nếu giới tính là Nam. Hiển thị: A. + tên người liên hệ. Ví dụ A.Thắng
--			Nếu giới tính là Nữ. Hiển thị: C. + tên người liên hệ. Ví dụ C.Lan
--		* Cột thứ bảy: Số điện thoại liên hệ
--		* Cột thứ tám: Địa chỉ người liên hệ
IF OBJECT_ID('spSearchRentHouse') IS NOT NULL
	DROP PROC spSearchRentHouse
GO
CREATE PROC spSearchRentHouse
	@QUAN nvarchar(20) = '%',
	@DIENTICHMAX int = NULL,
	@DIENTICHMIN int = 0,
	@NGAYDANGTINMAX date = NULL,
	@NGAYDANGTINMIN date = '2000-01-01',
	@GIATIENMAX money = NULL,
	@GIATIENMIN money = 0,
	@LOAIHINHNHATRO varchar(2) = '%'
AS
	IF @DIENTICHMAX IS NULL
		SELECT @DIENTICHMAX = MAX(DIENTICH) FROM NHATRO
	IF @NGAYDANGTINMAX IS NULL
		SELECT @NGAYDANGTINMAX = MAX(NGAYDANG) FROM NHATRO
	IF @GIATIENMAX IS NULL
		SELECT @GIATIENMAX = MAX(GIAPHONG) FROM NHATRO
	SELECT (N'Cho thuê phòng trọ tại ' + NHATRO.DIACHINT + ' ' + NHATRO.QUAN) AS N'Địa chỉ',
		   (REPLACE(CONVERT(varchar(50), NHATRO.DIENTICH),'.',',') + ' m2') AS N'Diện tích',
		   FORMAT(NHATRO.GIAPHONG, 'N', 'en-us') AS N'Giá tiền',
		   NHATRO.MOTA AS N'Mô tả',
		   CONVERT(varchar, NHATRO.NGAYDANG, 105) AS N'Ngày đăng',
		   (CASE NGUOIDUNG.GIOITINH
				WHEN 1 THEN 'A.' + NGUOIDUNG.TENND
				ELSE 'C.' + NGUOIDUNG.TENND
			END) AS N'Người liên hệ',
		   NGUOIDUNG.DIENTHOAI AS N'SĐT liên hệ',
		   NGUOIDUNG.DIACHI AS N'Địa chỉ liên hệ'
	FROM NHATRO JOIN NGUOIDUNG ON NHATRO.NGUOILIENHE = NGUOIDUNG.MAND
	WHERE NHATRO.QUAN LIKE @QUAN AND
		  NHATRO.LOAIHINHNT LIKE @LOAIHINHNHATRO AND
		  NHATRO.GIAPHONG >= @GIATIENMIN AND
		  NHATRO.GIAPHONG <= @GIATIENMAX AND
		  NHATRO.DIENTICH >= @DIENTICHMIN AND
		  NHATRO.DIENTICH <= @DIENTICHMAX AND
		  NHATRO.NGAYDANG >= @NGAYDANGTINMIN AND
		  NHATRO.NGAYDANG <= @NGAYDANGTINMAX
GO
EXEC spSearchRentHouse 
	@QUAN = N'Quận 10',
	@DIENTICHMAX = 300,
	@DIENTICHMIN = 14,
	@NGAYDANGTINMAX = '2022-08-05',
	@GIATIENMAX = 60000000,
	@GIATIENMIN = 1000000,
	@LOAIHINHNHATRO = 'CC'
EXEC spSearchRentHouse 
GO
-- b. Hàm có các tham số đầu vào tương ứng với tất cả các cột của bảng NGUOIDUNG. 
--	  Hàm này trả về mã người dùng (giá trị của cột khóa chính của bảng NGUOIDUNG) thỏa mãn các giá trị được truyền vào tham số.
IF OBJECT_ID('fnSearchMAND') IS NOT NULL
	DROP FUNCTION fnSearchMAND
GO
CREATE FUNCTION fnSearchMAND
	(@TENND	nvarchar(20) = '%',
	 @GIOITINH bit = NULL,
	 @DIENTHOAI	varchar(11) = '%',
	 @DIACHI nvarchar(50) = '%',
	 @QUAN	nvarchar(50) = '%',
	 @EMAIL	varchar(50) = '%')
	RETURNS int
BEGIN
	RETURN 
	   (SELECT MAND
		FROM NGUOIDUNG 
		WHERE TENND LIKE @TENND AND 
			GIOITINH = @GIOITINH AND 
			DIENTHOAI LIKE @DIENTHOAI AND 
			DIACHI LIKE @DIACHI AND 
			QUAN LIKE @QUAN AND 
			EMAIL LIKE @EMAIL)
END 
GO
PRINT N'Mã người dùng: ' + CONVERT(varchar, dbo.fnSearchMAND(N'Minh', 0, '0978173990', N'506 Ba Tháng Hai', N'Quận 10', 'minhtn@gmail.com'))
GO
-- c. Hàm có tham số đầu vào là mã nhà trọ (cột khóa chính của bảng NHATRO). 
--	  Hàm này trả về tổng số LIKE và DISLIKE của nhà trọ này.
IF OBJECT_ID('fnCountLikeDislike') IS NOT NULL
	DROP FUNCTION fnCountLikeDislike
GO
CREATE FUNCTION fnCountLikeDislike
	(@MANT int)
	RETURNS table
RETURN
	(SELECT MANT AS N'Mã nhà trọ', 
			SUM (CASE TRANGTHAIDG 
					WHEN 1 THEN 1
					ELSE 0
				 END) AS [Số Like],
			SUM (CASE TRANGTHAIDG
					WHEN 0 THEN 1 
					ELSE 0
				 END) AS [Số Dislike]
	 FROM DANHGIA
	 WHERE MANT = @MANT
	 GROUP BY MANT)
GO
SELECT * FROM dbo.fnCountLikeDislike(103)
GO
-- d. View lưu thông tin của TOP 10 nhà trọ có số người dùng LIKE nhiều nhất gồm các thông tin sau:
--		Diện tích 30 m2
--		Giá
--		Mô tả
--		Ngày đăng tin
--		Tên người liên hệ
--		Địa chỉ
--		Điện thoại
--		Email
CREATE VIEW TopNhaTro
AS
	SELECT TOP 10 REPLACE(CONVERT(varchar, NHATRO.DIENTICH),'.',',') + 'm2' AS N'Diện tích',
		   REPLACE(CONVERT(varchar, NHATRO.GIAPHONG),'.',',') AS N'Ngày đăng',
		   NGUOIDUNG.TENND AS N'Tên người liên hệ',
		   NGUOIDUNG.DIACHI AS N'Địa chỉ',
		   NGUOIDUNG.DIENTHOAI AS N'Điện thoại',
		   NGUOIDUNG.EMAIL,
		   COUNT(DANHGIA.TRANGTHAIDG) AS [Lượt like]
	FROM NHATRO INNER JOIN NGUOIDUNG ON NHATRO.NGUOILIENHE = NGUOIDUNG.MAND
	     INNER JOIN DANHGIA ON NHATRO.MANT = DANHGIA.MANT
	WHERE TRANGTHAIDG = 1
	GROUP BY NHATRO.DIENTICH, NHATRO.GIAPHONG, NHATRO.MOTA, NGUOIDUNG.TENND, NGUOIDUNG.DIACHI, 
			 NHATRO.NGAYDANG, NGUOIDUNG.DIENTHOAI, NGUOIDUNG.EMAIL
	ORDER BY [Lượt like] DESC
GO
SELECT * FROM TopNhaTro
GO
-- e. Stored Procedure nhận tham số đầu vào là mã nhà trọ (cột khóa chính của bảng NHATRO). 
--	  SP này trả về tập kết quả gồm các thông tin sau:
--			Mã nhà trọ
--			Tên người đánh giá
--			Trạng thái LIKE hay DISLIKE
--			Nội dung đánh giá
IF OBJECT_ID('spSearchReview') IS NOT NULL
	DROP PROC spSearchReview
GO
CREATE PROC spSearchReview
	@MANT int
AS
	SELECT DANHGIA.MANT AS N'Mã nhà trọ', 
		   NGUOIDUNG.TENND AS N'Tên người đánh giá', 
		   (CASE DANHGIA.TRANGTHAIDG
				WHEN 1 THEN 'Like'
				ELSE 'Dislike'
			END) AS N'Trạng thái', 
		   DANHGIA.NOIDUNGDG AS N'Nội dung đánh giá'
	FROM DANHGIA JOIN NGUOIDUNG ON DANHGIA.NGUOIDG = NGUOIDUNG.MAND
	WHERE DANHGIA.MANT = @MANT
GO
spSearchReview 103
GO
-- 3. Xoá thông tin
-- 1. SP nhận một tham số đầu vào kiểu int là số lượng DISLIKE. 
--	  SP này thực hiện thao tác xóa thông tin của các nhà trọ và thông tin đánh giá của chúng, 
--				nếu tổng số lượng DISLIKE tương ứng với nhà trọ này lớn hơn giá trị tham số được truyền vào.
--	  Yêu cầu: Sử dụng giao dịch trong thân SP, để đảm bảo tính toàn vẹn dữ liệu khi một thao tác xóa thực hiện không thành công.
IF OBJECT_ID('spDeleteGreatDislike') IS NOT NULL
	DROP PROC spDeleteGreatDislike
GO
CREATE PROC spDeleteGreatDislike
	@DISLIKE int = NULL
AS
	BEGIN TRY
		BEGIN TRAN
			IF (@DISLIKE IS NULL) OR (@DISLIKE < 0)
				BEGIN
					PRINT N'Hãy kiểm tra dữ liệu nhập'
					ROLLBACK TRAN
				END
			ELSE
				BEGIN
					DELETE NHATRO 
					FROM NHATRO 
						 JOIN 
						 (SELECT MANT,
								 SUM(CASE TRANGTHAIDG 
											WHEN 0 THEN 1
											ELSE 0
									 END) AS SODISLIKE
						 FROM DANHGIA
						 GROUP BY MANT) BADNT ON NHATRO.MANT = BADNT.MANT
					WHERE BADNT.SODISLIKE > @DISLIKE
					COMMIT TRAN
					PRINT N'Xoá thông tin thành công'
				END
	END TRY
	BEGIN CATCH
		PRINT N'Xoá thông tin không thành công'
		ROLLBACK TRAN
	END CATCH
GO
spDeleteGreatDislike 1
GO
spDeleteGreatDislike -1
GO
-- 3.2. SP nhận hai tham số đầu vào là khoảng thời gian đăng tin. 
--	  SP này thực hiện thao tác xóa thông tin những nhà trọ được đăng trong khoảng thời gian được truyền vào qua các tham số.
--	  Lưu ý: SP cũng phải thực hiện xóa thông tin đánh giá của các nhà trọ này.
--	  Yêu cầu: Sử dụng giao dịch trong thân SP, để đảm bảo tính toàn vẹn dữ liệu khi một thao tác xóa thực hiện không thành công.
IF OBJECT_ID('spDeleteDateInRange') IS NOT NULL
	DROP PROC spDeleteDateInRange
GO
CREATE PROC spDeleteDateInRange
	@NGAYDANGMIN date = NULL,
	@NGAYDANGMAX date = NULL
AS
	BEGIN TRY
		BEGIN TRAN
			IF (@NGAYDANGMIN IS NULL) OR (@NGAYDANGMAX IS NULL) OR (@NGAYDANGMIN > @NGAYDANGMAX)
				BEGIN
					PRINT N'Hãy kiểm tra dữ liệu nhập'
					ROLLBACK TRAN
				END
			ELSE
				BEGIN
					DELETE FROM NHATRO 
					WHERE NGAYDANG >= @NGAYDANGMIN AND
						  NGAYDANG <= @NGAYDANGMAX
					COMMIT TRAN
					PRINT N'Xoá thông tin thành công'
				END
	END TRY
	BEGIN CATCH
		PRINT N'Xoá thông tin không thành công'
		ROLLBACK TRAN
	END CATCH
GO
spDeleteDateInRange '2013-01-01', '2013-02-01' 
GO
spDeleteDateInRange '2013-03-01', '2013-02-01' 
GO