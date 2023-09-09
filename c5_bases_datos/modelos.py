# Importamos el módulo `sqlalchemy`
from conexion import ModeloBase
from sqlalchemy import Column, ForeignKey, Integer, String


# Creamos la clase `Departamento`
class Departamento(ModeloBase):
    # Declaramos el nombre de la tabla
    __tablename__ = "departamento"
    # Declaramos las columnas de la tabla
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False, unique=True)

    # Definimos el constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre

    # Definimos el método `__str__` para representar la clase como una cadena de texto
    def __str__(self):
        return f"{self.id} - {self.nombre}"


# Creamos la clase `Empleado`
class Empleado(ModeloBase):
    # Declaramos el nombre de la tabla
    __tablename__ = "empleado"

    # Declaramos las columnas de la tabla
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    documento = Column(String, nullable=False, unique=True)
    id_departamento = Column(Integer,ForeignKey("departamento.id"))

    # Definimos el constructor de la clase
    def __init__(self, nombre, apellido, documento, id_departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.id_departamento = id_departamento

    # Definimos el método `__str__` para representar la clase como una cadena de texto
    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellido}"
