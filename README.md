# CurioFact API
[![GitHub last commit](https://img.shields.io/github/last-commit/KJRM20/Curiofact)](#)<br><br>
CurioFact es una API que proporciona datos curiosos organizados en categorías como historia, ciencias, arte y espacio. Esta API permite obtener datos curiosos aleatorios de categorías específicas o todos los datos de una categoría, ideal para aplicaciones educativas o de entretenimiento.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Tecnologías](#tecnologías)
- [Contribuciones](#contribuciones)

## Descripción
CurioFact proporciona un acceso sencillo a datos curiosos en diferentes categorías a través de una API RESTful desarrollada con Flask y SQLAlchemy.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/CurioFact.git
   cd CurioFact
   ```
2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # En Linux/Mac
   .\env\Scripts\activate   # En Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
## Configuración de la Base de Datos
1. Configura  datos SQLite ejecutando el script ```setup_database.py```:
   ```bash
   python setup_database.py
   ```
   Esto creará el archivo database.db en la carpeta ```instance/```.

## Uso
Inicia la aplicación con el siguiente comando:
```bash
python app.py
```
La API estará disponible en ```http://127.0.0.1:5000```.

## Endpoints
- **Obtener todos los datos de una categoría**
  ```GET /curiofact/datos/<categoria>```
  - **Descripción**: Devuelve todos los datos curiosos de la categoría especificada.
  - **Ejemplo**: ```/datos/historia```
- **Obtener un dato aleatorio de una categoría**
  ```GET /curiofact/dato_aleatorio/<categoria>```
  - **Descripción**: Devuelve un dato curioso aleatorio de la categoría especificada.
  - **Ejemplo**: ```/dato_aleatorio/ciencias```

## Tecnologías
- Python
- Flask
- SQLAlchemy
- SQLite (para la base de datos local)

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue los pasos:

1. Haz un fork del repositorio.
2. Crea una rama nueva para tu funcionalidad (```git checkout -b feature/nueva-funcionalidad```).
3. Realiza tus cambios y haz un commit (```git commit -m 'Agrega nueva funcionalidad'```).
4. Sube tus cambios (```git push origin feature/nueva-funcionalidad```).
5. Abre un Pull Request.

------------
¡Gracias por interesarte en CurioFact! 🎉
<br><small>Realizado por Karen Rincón, 2024</small><br><br>
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KJRM20) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-100000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karen-rincon/) 
