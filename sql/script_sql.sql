use Kaggle
GO
---en caso no existe la tabla
if not exists(select * from sys.tables where object_id = OBJECT_ID(N'dbo.olympics')AND type='U')
	create table dbo.olympics(
		NOC varchar(10),
		Gold INT,
		Silver INT,
		Bronze INT,
		Total INT
	)

go 

---si ya existe la tabla 
truncate table dbo.olympics;
go

---importar data desde archivo
bulk insert dbo.olympics
from 'C:\Users\LEGION\Desktop\CERTUS\proyecto_parcial\dataset\Athens 2004 Olympics Nations Medals.csv'
with
(
	
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0X0a' --salto de linea
)

GO



