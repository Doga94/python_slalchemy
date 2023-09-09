# Importamos el módulo `sqlalchemy`
# Este módulo proporciona las clases y funciones necesarias para trabajar con bases de datos relacionales.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definimos el nombre de la base de datos
# Este es el nombre del archivo de la base de datos
nombre_db = "empleados.sqlite"

# Creamos un motor para conectarnos a la base de datos
# El motor se conecta a la base de datos usando la URL especificada
engine = create_engine(f"sqlite:///{nombre_db}")

# Creamos un sessionmaker para crear sesiones
# Una sesión es un objeto que nos permite interactuar con la base de datos
Session = sessionmaker(bind=engine)

# Creamos una sesión
# Esta sesión es la que usaremos para insertar, actualizar, eliminar y consultar datos en la base de datos
session = Session()

# Creamos una base declarativa
# Una base declarativa se utiliza para crear clases que representan las tablas de la base de datos
ModeloBase = declarative_base()