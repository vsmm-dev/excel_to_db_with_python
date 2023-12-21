# Update database with Python

Este proyecto permite actualizar coordenadas de latitud y longitud de un excel a una base de datos en Python.

### Instalación de Python

Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Instalación de Bibliotecas

Las siguientes bibliotecas de Python son necesarias para ejecutar el script:

- `requests`: Para realizar solicitudes HTTP a la API de Google Maps.
- `pandas`: Para manejar datos en formato tabular.
- `openpyxl`: Para leer y escribir archivos de Excel.

Puedes instalar estas bibliotecas utilizando el siguiente comando:

```bash
pip install pandas openpyxl mysql-connector-python
```
### Uso
Para utilizar el script:

Asegúrate de que tus latitudes y logitudes estén en un archivo Excel en una columna específica.

Ejecuta el script con Python:
```bash
python excel_to_db.py
```

### Script excel_to_db.py
El script excel_to_db.py lee latitudes y longitudes de un archivo Excel, escribe estas coordenadas en el la base de datos.
