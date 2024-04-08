USE ProyectoPar
GO
--EN CASO NO EXISTA LA TABLA, LA VOY A CREAR

IF not exists (Select * from SYS.TABLES Where object_id=OBJECT_ID(N'dbo.reporte')and type='U')
	CREATE TABLE dbo.reporte (
		Age INT,
		Gender VARCHAR(200),
		Marital_Status VARCHAR(200),
		Occupation VARCHAR(200),
		Monthly_Income VARCHAR(200),
		Educational_Qualifications VARCHAR(200),
		Family_size INT,
		latitude DECIMAL(10,2),
		longitude DECIMAL(10,2),
		Pin_code INT,
		Output_Output VARCHAR(200),
		Feedback VARCHAR(200),
	)
GO

--SI LA TABLA YA EXISTE, LA VAMOS A LIMPIAR
TRUNCATE TABLE dbo.reporte
GO

--IMPORTAR LA DATA DE MI ACHIVO CSV

BULK INSERT dbo.reporte
FROM 'C:\Users\Irving\Documents\Ruta para Analista de Data\CERTUS\DEVOPS\Proyecto_Parcial\Python\dataset\onlinefoods.csv' --- UBICACION DEL ARCHIVO
WITH
(
	FIRSTROW = 2, --- EMPIEZA A INSERTAR DATA DESDE LA FILA 2, YA QUE LA PRIMERA ES LA CABECERA
	FIELDTERMINATOR = ',', --- DELIMITADOR DE LOS CAMPOS DE LA COLUMNAS
	ROWTERMINATOR = '0x0a' ---DELIMITADOR DE LAS FILAS, EN ESTE CASO EL CODIGO ES SALTO DE FILA
)
GO