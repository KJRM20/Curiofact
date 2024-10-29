from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from models import db, Categoria, DatoCurioso

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

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
    app.run(debug=True)
