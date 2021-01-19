{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "running-carroll",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyodbc\n",
    "from pymongo import MongoClient\n",
    "import json\n",
    "from decimal import Decimal\n",
    "from bson.decimal128 import Decimal128"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "polyphonic-invite",
   "metadata": {},
   "outputs": [],
   "source": [
    "nombre_servidor = \"localhost\\SQLEXPRESS\"\n",
    "base_datos = \"FACTURACION\"\n",
    "\n",
    "conn_sql = pyodbc.connect('Driver={{SQL Server}};' 'Server={};''Database={};''Trusted_Connection=yes;'.format(\n",
    "                          nombre_servidor,\n",
    "                          base_datos))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "brief-arizona",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Andres              ', 'alquinga            ', Decimal('14'), Decimal('11'), 'amaznoas                                          ', 'andres@hotmail                ', Decimal('215412'))\n",
      "guardado exitosamente\n",
      "('sonia               ', 'altamirano          ', Decimal('15'), Decimal('11'), 'rio coca                                          ', 'asd@hotmail.com               ', Decimal('322333'))\n",
      "guardado exitosamente\n",
      "('Teresa              ', 'Pozo                ', Decimal('16'), Decimal('11'), 'puembo                                            ', 'teresa@hotmail.com            ', Decimal('44444'))\n",
      "guardado exitosamente\n",
      "('Carlos              ', 'michelena           ', Decimal('17'), Decimal('11'), 'amazonas                                          ', 'carlos@hotmail.com            ', Decimal('55555'))\n",
      "guardado exitosamente\n",
      "('Tania               ', 'Calle               ', Decimal('18'), Decimal('11'), 'solanda                                           ', 'tania@hotmail.com             ', Decimal('66666'))\n",
      "guardado exitosamente\n",
      "('hernan              ', 'Bueno               ', Decimal('19'), Decimal('22'), 'solanda                                           ', 'hernan@hotmail.com            ', Decimal('77777'))\n",
      "guardado exitosamente\n",
      "('AMANDA              ', 'LOPEZ               ', Decimal('1727582782'), Decimal('1708102834'), 'LA TOLA                                           ', 'amal@hotmail.com              ', Decimal('925632584'))\n",
      "guardado exitosamente\n",
      "('FERNANDO            ', 'JIMENEZ             ', Decimal('1542598562'), Decimal('1708102834'), 'CHILLOGALLO                                       ', 'fer3@hotmail.com              ', Decimal('996523659'))\n",
      "guardado exitosamente\n",
      "('CARLA               ', 'SALAZAR             ', Decimal('1562548896'), Decimal('1708102834'), 'LLANO CHICO                                       ', 'carlas@gmail.com              ', Decimal('990145114'))\n",
      "guardado exitosamente\n",
      "('FRED                ', 'MEJIA               ', Decimal('1002315221'), Decimal('1708102834'), 'QUITUMBE                                          ', 'fredd@hotmail.com             ', Decimal('994562458'))\n",
      "guardado exitosamente\n",
      "('DANNY               ', 'GUERRERO            ', Decimal('1548759621'), Decimal('1708102834'), 'LA CAROLINA                                       ', 'danig@hotmail.com             ', Decimal('965218994'))\n",
      "guardado exitosamente\n",
      "('JENNY               ', 'TOVAR               ', Decimal('1002315551'), Decimal('1708102834'), 'GUAJALO                                           ', 'jeny@gmail.com                ', Decimal('998526355'))\n",
      "guardado exitosamente\n",
      "('STEVEN              ', 'CAMPOSANO           ', Decimal('1624581521'), Decimal('1708102834'), 'MONSERRATE                                        ', 'steve@hotmail.com             ', Decimal('913452185'))\n",
      "guardado exitosamente\n",
      "('LUIS                ', 'ARTEAGA             ', Decimal('1709987943'), Decimal('1708102834'), 'LA ROLDOS                                         ', 'luis@gmail.com                ', Decimal('992145632'))\n",
      "guardado exitosamente\n",
      "('ANDREA              ', 'LOPEZ               ', Decimal('1804000915'), Decimal('1708102834'), 'EL DORADO                                         ', 'andre@hotmail.com             ', Decimal('999289221'))\n",
      "guardado exitosamente\n",
      "('JUAN                ', 'PEREZ               ', Decimal('1741579548'), Decimal('1708102834'), 'SAN CARLOS                                        ', 'juan@gmail.com                ', Decimal('945215211'))\n",
      "guardado exitosamente\n",
      "('PEDRO               ', 'JIMENEZ             ', Decimal('184712350'), Decimal('1708102834'), 'EL CALZADO                                        ', 'pedro@hotmail.com             ', Decimal('974512365'))\n",
      "guardado exitosamente\n",
      "('JORGE               ', 'ZURITA              ', Decimal('214256978'), Decimal('1708102834'), 'EL GIRON                                          ', 'jorge@gmail.com               ', Decimal('991452321'))\n",
      "guardado exitosamente\n",
      "('SONIA               ', 'MELIZALDE           ', Decimal('1402694578'), Decimal('1708102834'), 'CUENCA                                            ', 'sonia@gmail.com               ', Decimal('971254578'))\n",
      "guardado exitosamente\n",
      "('MARITZA             ', 'ZAMBRANO            ', Decimal('1714586421'), Decimal('1708102834'), 'EL RECREO                                         ', 'mario@hotmail.com             ', Decimal('951241523'))\n",
      "guardado exitosamente\n"
     ]
    }
   ],
   "source": [
    "cursor = conn_sql.cursor()\n",
    "cursor.execute('SELECT * FROM CLIENTES')\n",
    " \n",
    "conn_mongo = MongoClient('mongodb://localhost:27017')\n",
    "db = conn_mongo.sqlFacturacion\n",
    "collection = db.Clientes\n",
    " \n",
    "for row in cursor:\n",
    "    \n",
    "    print(row)\n",
    "    row2 = Decimal(row[2])\n",
    "    num2 = Decimal128(str(row2))\n",
    "    row3 = Decimal(row[3])\n",
    "    num3 = Decimal128(str(row3))\n",
    "    row6 = Decimal(row[6])\n",
    "    num6 = Decimal128(str(row6))\n",
    "    \n",
    "    doc = {'nombre': row[0], 'apellido':row[1], 'IDCliente': num, 'RUC Empresa':num3,'direccion cliente':row[4],'email cliente':row[5],'telefono cliente':num6}\n",
    "    collection.insert_one(doc)\n",
    "    print(\"guardado exitosamente\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "imperial-interval",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
