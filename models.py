from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    datos_curiosos = db.relationship('DatoCurioso', backref='categoria', lazy=True)

class DatoCurioso(db.Model):
    __tablename__ = 'datos_curiosos'
    id = db.Column(db.Integer, primary_key=True)
    dato = db.Column(db.String(500), nullable=False)
    imagen = db.Column(db.String(200), nullable=True)
    referencia = db.Column(db.String(200), nullable=True)
    enlace = db.Column(db.String(200), nullable=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
