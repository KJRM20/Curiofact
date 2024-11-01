from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from models import db, Categoria, DatoCurioso
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
print("DATABASE_URL:", os.getenv('DATABASE_URL'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def verificar_y_crear_tablas():
    try:
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        with engine.connect() as connection:
            print("Conexión exitosa a la base de datos.")
        db.create_all()
        print("Base de datos creada exitosamente.")
    except OperationalError as e:
        print(f"Error al conectar con la base de datos: {e}")


# Endpoint para obtener datos curiosos por categoría
@app.route('/datos/<string:categoria>', methods=['GET'])
def obtener_datos_por_categoria(categoria):
    categoria_obj = Categoria.query.filter_by(nombre=categoria).first()
    if not categoria_obj:
        return jsonify({'error': 'Categoría no encontrada'}), 404
    datos = DatoCurioso.query.filter_by(categoria_id=categoria_obj.id).all()
    return jsonify([
        {
            'dato': dato.dato,
            'imagen': dato.imagen,
            'referencia': dato.referencia,
            'enlace': dato.enlace
        } for dato in datos
    ])

# Endpoint para obtener un dato aleatorio de una categoría
@app.route('/dato_aleatorio/<string:categoria>', methods=['GET'])
def obtener_dato_aleatorio(categoria):
    categoria_obj = Categoria.query.filter_by(nombre=categoria).first()
    if not categoria_obj:
        return jsonify({'error': 'Categoría no encontrada'}), 404
    
    dato_aleatorio = DatoCurioso.query.filter_by(categoria_id=categoria_obj.id).order_by(func.random()).first()
    if not dato_aleatorio:
        return jsonify({'error': 'No hay datos en esta categoría'}), 404
    
    return jsonify({
        'dato': dato_aleatorio.dato,
        'imagen': dato_aleatorio.imagen,
        'referencia': dato_aleatorio.referencia,
        'enlace': dato_aleatorio.enlace
    })

if __name__ == '__main__':
    app.run(debug=True) #Local
    #app.run()

