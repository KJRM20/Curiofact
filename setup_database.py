from app import app, db  # Importa la instancia de `app` y `db` desde `app.py`
from models import Categoria, DatoCurioso

# Ejecuta `create_all()` dentro del contexto de la aplicación
with app.app_context():
    db.create_all()
    print("Base de datos creada exitosamente.")
