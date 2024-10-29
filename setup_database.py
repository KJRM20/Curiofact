from app import app, db  # Importa la instancia de `app` y `db` desde `app.py`
from models import Categoria, DatoCurioso
from sqlalchemy.exc import SQLAlchemyError

# Ejecuta `create_all()` dentro del contexto de la aplicación
with app.app_context():
    try:
        db.create_all()
        print("Base de datos creada exitosamente.")
    except SQLAlchemyError as e:
        print("Error al crear la base de datos:", str(e))
