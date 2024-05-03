from flask import Flask ,render_template, request, redirect, url_for
from settings import config
#import pyodbc

#aplicacion = r"settings.py"
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Base_datos.accdb;')

app = Flask(__name__)
app.secret_key = "Pagame"
#try:
#    with open(aplicacion, "r") as file:
#        code = file.read()
#        exec(code)
#except FileNotFoundError:
#    print(f"El archivo {aplicacion} no se a encontrado.")
#except Exception as e:
#    print(f"Error en el archivo {aplicacion}: {str(e)}")
@app.route('/')
def index():
    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        print(request.form["Email"])
        print(request.form["Password"])
        return render_template("login.html")
    else:
        return render_template("login.html")
    
if __name__ == '__main__':
    app.config.from_object(config["development"])
    app.run(debug=True)