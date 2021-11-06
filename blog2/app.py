from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy #hace objetos a las tablas
from werkzeug.urls import url_parse
from pymysql import *
from forms import *
app = Flask(__name__) #tuve que poner esto por encima del ultimo importsino no funcionaba
from models import *





app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://BD2021:BD2021itec@143.198.156.171/apg_lp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.create_all()

@app.route("/")
def index():
    sexo = Sexo.get_all()
    return render_template("index.html", sexo=sexo)#creo que sexo=sexo es una convención

@app.route("/carga_alumnos/", methods=['GET', 'POST'], defaults={'alumnos_id': None})
def cargaAlumnos(alumnos_id):
    form = AlumnosForm()
    if form.validate_on_submit():
        apellido = form.apellido.data
        nombre = form.nombre.data
        sexo = form.sexo.data
        alumno = Alumnos(apellido=apellido, nombre=nombre, sexo=sexo)
        alumno.save()
    return render_template("carga_alumnos.html", form=form)

@app.route("/prueba/")
def prueba():
    form = ChoiceForm()
    return render_template("prueba.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)