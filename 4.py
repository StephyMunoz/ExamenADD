import pyodbc
from pymongo import MongoClient
import json
from decimal import Decimal
from bson.decimal128 import Decimal128

nombre_servidor = "localhost\SQLEXPRESS"
base_datos = "FACTURACION"

conn_sql = pyodbc.connect('Driver={{SQL Server}};' 'Server={};''Database={};''Trusted_Connection=yes;'.format(
                          nombre_servidor,
                          base_datos))


cursor = conn_sql.cursor()
cursor.execute('SELECT * FROM CLIENTES')
 
conn_mongo = MongoClient('mongodb://localhost:27017')
db = conn_mongo.sqlFacturacion
collection = db.Clientes
 
for row in cursor:
    
    print(row)
    row2 = Decimal(row[2])
    num2 = Decimal128(str(row2))
    row3 = Decimal(row[3])
    num3 = Decimal128(str(row3))
    row6 = Decimal(row[6])
    num6 = Decimal128(str(row6))
    
    doc = {'nombre': row[0], 'apellido':row[1], 'IDCliente': num, 'RUC Empresa':num3,'direccion cliente':row[4],'email cliente':row[5],'telefono cliente':num6}
    collection.insert_one(doc)
    print("guardado exitosamente")