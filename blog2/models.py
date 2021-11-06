from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from app import db

class Alumnado(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_alumnos = db.Column(db.Integer(), db.ForeignKey('alumnos.id', ondelete='CASCADE'), nullable=False)
    id_curso = db.Column(db.Integer(), db.ForeignKey('curso.id', ondelete='CASCADE'), nullable=False)
    id_division = db.Column(db.Integer(), db.ForeignKey('division.id', ondelete='CASCADE'), nullable=False)
    año = db.Column(db.Integer(), nullable=False)
    id_becas = db.Column(db.Integer(), db.ForeignKey('becas.id', ondelete='CASCADE'), nullable=False)

class Alumnos(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    apellido = db.Column(db.String(50), nullable=False) 
    nombre = db.Column(db.String(50), nullable=False) 
    dni = db.Column(db.Integer(), nullable=False)
    domicilio = db.Column(db.String(70), nullable=True) #ver si no poniendolo directamente es lo mismo que el nullable=True
    id_localidad = db.Column(db.Integer(), db.ForeignKey('localidad.id', ondelete='CASCADE'), nullable=False)
    id_pais_nac = db.Column(db.Integer(), db.ForeignKey('pais_nac.id', ondelete='CASCADE'), nullable=False)
    id_estado_civil = db.Column(db.Integer(), db.ForeignKey('estado_civil.id', ondelete='CASCADE'), nullable=True)
    id_sexo = db.Column(db.Integer(), db.ForeignKey('sexo.id', ondelete='CASCADE'), nullable=True)
    activo = db.Column(db.Integer(), nullable=False) #ver porque en la BD figura como Binary

    def get_all():
        return Alumnos.query.all()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
                self.title_slug = f'{self.title_slug}-{count}'    

        
class Becas(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    porcentaje_desc = db.Column(db.Numeric(), nullable=False) #ver porque en la BD figura como decimal (buscar el nombre del atributo Decimal)

class Concepto(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    estado = db.Column(db.String(50), nullable=False) 

class Contactos(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre_apellido = db.Column(db.String(100), nullable=False) 
    direccion = db.Column(db.String(100), nullable=True) 
    telefono = db.Column(db.String(100), nullable=True) 
    correo_electronico = db.Column(db.String(70), nullable=True) #este tendria que se Null=False para que este si o si porque se usa para ingresar

class Curso(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(25), nullable=False)

class Devengado(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_alumnado = db.Column(db.Integer(), db.ForeignKey('alumnado.id', ondelete='CASCADE'), nullable=False)
    id_concepto = db.Column(db.Integer(), db.ForeignKey('concepto.id', ondelete='CASCADE'), nullable=False)
    periodo = db.Column(db.Date, nullable=False)
    monto = db.Column(db.Integer(), nullable=False)
    pagado = db.Column(db.Integer(), nullable=True) #tambien es binary y deberia estar como null=true (creo)

class Division(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(1), nullable=False) 

class Estado_civil(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)  

class Localidad(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    id_provincia = db.Column(db.Integer(), db.ForeignKey('provincia.id', ondelete='CASCADE'), nullable=False)

class Pago(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_devengado = db.Column(db.Integer(), db.ForeignKey('devengado.id', ondelete='CASCADE'), nullable=False)
    fecha_pago = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(150), nullable=True)

class Pais_nac(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Provincia(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Relacion(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(70), nullable=False)

class Relacion_contactos(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_alumnos = db.Column(db.Integer(), db.ForeignKey('alumnos.id', ondelete='CASCADE'), nullable=False)
    id_contactos = db.Column(db.Integer(), db.ForeignKey('contactos.id', ondelete='CASCADE'), nullable=False)
    id_relacion = db.Column(db.Integer(), db.ForeignKey('relacion.id', ondelete='CASCADE'), nullable=False)

class Sexo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    inicial = db.Column(db.String(1), nullable=False)
    descripcion = db.Column(db.String(25), nullable=False)

    def get_all():
        return Sexo.query.all()#es necesaria para el metodo en la linea 21 de app.py