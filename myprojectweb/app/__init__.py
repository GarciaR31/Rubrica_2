from flask import Flask
import pyodbc

aplicacion = r"C:\Users\ALAIN\Documents\myprojectweb\app\config.py"
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ALAIN\Documents\myprojectweb\database.accdb;')

app = Flask(__name__)
try:
    with open(aplicacion, "r") as file:
        code = file.read()
        exec(code)
except FileNotFoundError:
    print(f"El archivo {aplicacion} no se a encontrado.")
except Exception as e:
    print(f"Error en el archivo {aplicacion}: {str(e)}")
    
if __name__ == '__main__':
    app.run(debug=True)