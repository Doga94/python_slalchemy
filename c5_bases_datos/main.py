from modelos import Departamento, Empleado
from conexion import engine, ModeloBase, session

# Esta función guarda los datos en la base de datos
def guardar_datos():
    # Creamos un departamento de contabilidad
    contabilidad = Departamento("Contabilidad")
    session.add(contabilidad)
    # Creamos un departamento de tecnología
    tecnologia = Departamento("Tecnologia")
    session.add(tecnologia)
    # Confirmamos los cambios en la base de datos
    session.commit()
    # Creamos un empleado llamado David Gomez
    david = Empleado("David", "Gomez", 1235554, contabilidad.id)
    session.add(david)
    # Creamos un empleado llamado Orlando Alarcon
    orlando = Empleado("Orlando", "Alarcon", 985542, tecnologia.id)
    session.add(orlando)
    # Confirmamos los cambios en la base de datos
    session.commit()
    # Imprimimos el ID del departamento de contabilidad
    print(contabilidad.id)
# Esta función realiza consultas a la base de datos
def hacer_consultas():
    # Obtenemos el departamento con ID 1
    Departamento_1 =session.get(Departamento, 1)
    print(Departamento_1)
    # Contamos el número de departamentos
    cantidad_departamentos = session.query(Departamento).count()
    print(cantidad_departamentos)
    # Obtenemos todos los empleados del departamento de contabilidad
    empleados_contabilidad = session.query(Empleado).filter_by(
        id_departamento = Departamento_1.id
    ).all()
    print(empleados_contabilidad)
    # Imprimimos cada empleado del departamento de contabilidad
    for empleado in empleados_contabilidad:
        print(empleado)
# Esta sección se ejecuta cuando se importa el módulo
if __name__ == "__main__":
    # Creamos la base de datos
    ModeloBase.metadata.create_all(engine)

    # Ejecutamos la función `guardar_datos()`
    #guardar_datos()

    # Ejecutamos la función `hacer_consultas()`
    hacer_consultas()