--1. Liet ke thong tin chi tiet cac nhan vien co luong trong khoang 300 den 500 ngan
SELECT *
FROM NHANVIEN
WHERE LUONG >= 300000 AND LUONG <= 500000

--2. cho biet co bao nhieu nhan vien nu va bao nhieu nhan vien nam
SELECT PHAI,COUNT(*)
FROM NHANVIEN
GROUP BY PHAI
--3. liet ke MNV ho va ten cua cac nhan vien co tuoi be hon 60
SELECT MANV,HOLOT,TENGOI,(YEAR(GETDATE()) - YEAR(NGAYSINH)) AS TUOI
FROM NHANVIEN
WHERE (YEAR(GETDATE()) - YEAR(NGAYSINH)) <= 60
--4. cho biet manv cua cac nhan vien bat dau bang L
SELECT MANV,TENGOI
FROM NHANVIEN
WHERE TENGOI LIKE 'L%'
--5. cho biet MAMV ho va ten ngay sinh cua nhung nhan vien co muc luong bang voi muc luong nu nho nhat
SELECT MANV,HOLOT,TENGOI,NGAYSINH
FROM NHANVIEN
WHERE LUONG = (SELECT MIN(LUONG)
				FROM NHANVIEN 
				WHERE PHAI = 'True')
--6. CHO BIET MANV ho va ten cua NV phu trach cac loai phieu nhap tu ngay 1/5/2003 den ngay 10/5/2003.
SELECT LOAI,NV.MANV,HOLOT,TENGOI
FROM NHAPXUAT NX JOIN NHANVIEN NV 
ON NX.MANV = NV.MANV
WHERE DAY(NGAY) >= 1 AND DAY(NGAY) <=10
ORDER BY LOAI ASC
--7.  cho biet tong tien cac loai phieu nhap xuat thu chi
SELECT LOAI,SUM(TIEN) AS TONGTIEN
FROM NHAPXUAT
GROUP BY LOAI
--8. cho biet tong tien cua nhan vien co ma Sp tai kho Thu Duc
SELECT MANV, MAKHO, SUM(TIEN) AS TONGTIEN
FROM NHAPXUAT
WHERE MANV LIKE 'SP02' AND MAKHO LIKE 'TD'
GROUP BY MANV, MAKHO