import psycopg2 as PBD

def dbConectar():
    ip = "localhost"
    puerto = 5432
    basedatos = "Empresa"

    usuario = "postgres"
    contrasena = "12345"

    print("---dbConectar---")
    print("---Conectando a Postgresql---")

    try:
        conexion = PBD.connect(user=usuario, password=contrasena, host=ip, port=puerto, database=basedatos)
        print("Conexión realizada a la base de datos",conexion)
        return conexion
    except PBD.DatabaseError as error:
        print("Error en la conexión")
        print(error)
        return None

# ------------------------------------------------------------------

def dbDesconectar():
    print("---dbDesconectar---")
    try:
        conexion.commit()
        conexion.close()
        print("Desconexión realizada correctamente")
        return True
    except PBD.DatabaseError as error:
        print("Error en la desconexión")
        print(error)
        return False

# ------------------------------------------------------------------

def dbMostrarEmpleados1():
    print("---dbMostrarEmpleados1---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM Empleados"
        cursor.execute(consulta)       
        for tupla in cursor:
            print(tupla)
        print("Número de registros recuperados:",cursor.rowcount)
        print('------------------------------')
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error en dbMostrarEmpleados1")
        print(error)

# ------------------------------------------------------------------

def dbMostrarEmpleados2():
    print("---dbMostrarEmpleados2---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM Empleados"
        cursor.execute(consulta)       
        tupla = cursor.fetchone()
        while tupla:
            print(tupla)        
            tupla = cursor.fetchone()
        print("Número de registros recuperados:",cursor.rowcount)
        print('------------------------------')
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error en dbMostrarEmpleados2")
        print(error)
              
# ------------------------------------------------------------------

def dbMostrarEmpleados3():
    print("---dbMostrarEmpleados3---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM Empleados"
        cursor.execute(consulta)       
        numTuplas = 5
        resul = cursor.fetchmany(numTuplas)
        for tupla in resul:
            print(tupla)
        print("Número de registros seleccionados:",len(resul))
        print("Número de registros recuperados:",cursor.rowcount)
        print('------------------------------')
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error en dbMostrarEmpleados3")
        print(error)
              
# ------------------------------------------------------------------

def dbMostrarEmpleados4():
    print("---dbMostrarEmpleados4---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM Empleados"
        cursor.execute(consulta)       
        resul = cursor.fetchall()
        for tupla in resul:
            print(tupla)
        print("Número de registros recuperados:",len(resul))
        print("Número de registros recuperados:",cursor.rowcount)
        print('------------------------------')
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error en dbMostrarEmpleados4")
        print(error)
                  
# ------------------------------------------------------------------

def dbObtenerEmpleados():
    print("---dbObtenerEmpleados---")

    # Por ejemplo, buscar Empleados con dni 123456789
    dniObjetivo = input("Introduce dni de Empleados: ")

    try:
        #Se establece la conexión con la base de datos de Oracle.
        cursor = conexion.cursor()
        #Se inicializa la petición a nuestra base de datos de Oracle. Para Oracle, a la hora de
        #realizar una petición, debemos inicializar los parametros de la consulta con :nom_propiedad. 
        #Esto nos permite evitar la inyección de código SQL.
        consulta = "SELECT * FROM Empleados  WHERE dni = %s"

        #Se ejecuta la consulta, guardando en el segundo parámetro, una lista con las variables que se utilizarán
        #en la consulta. En este caso, solo hay una variable, el dni.
        cursor.execute(consulta, [dniObjetivo])    

        #Se guarda en la variable "result" la información recuperada de la petición.   
        
        resul = cursor.fetchone()
        #Se imprime por pantalla la información recuperada.
        print(resul)

        cursor.close()
    except PBD.DatabaseError as error:
        print("Error. No se ha podido consultar la tupla", dniObjetivo)
        print(error)

# ------------------------------------------------------------------

def dbConsultarEmpleados():
    print("---dbConsultarEmpleados---")

    try:
         #Se establece la conexión con la base de datos de Oracle.
        cursor = conexion.cursor()
        #Se inicializa la petición a nuestra base de datos de Oracle. Para Oracle, a la hora de
        #realizar una petición, debemos inicializar los parametros de la consulta con %s. 
        #Esto nos permite evitar la inyección de código SQL.
        consulta = "SELECT * FROM Empleados"

        #Se ejecuta la consulta
        cursor.execute(consulta)    

        #Se guarda en la variable "result" la información recuperada de la petición.   
        #En este caso, se trata de todas las filas existentes en la tabla "Empleados"
        resul = cursor.fetchall()

        #Se imprime por pantalla la información recuperada. En este caso, como se trata de una lista, se itera
        for tupla in resul:
            print(f"DNI: ",tupla[0])
            print(f"Nombre: ",tupla[1])
            print(f"Fecha Nacimiento: ",tupla[2])
            print(f"CP: ",tupla[3])
            print(f"Sexo: ",tupla[4])
            print(f"Sueldo: ",tupla[5])
            print(f"Número de departamento: ",tupla[6])
            print('------------------------------')
        print("Número de registros recuperados:",len(resul))
        print("Número de registros recuperados:",cursor.rowcount)
        print('------------------------------')
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error. No se han podido consultar las tuplas de Empleados")
        print(error)

# ------------------------------------------------------------------
def mostrarValoresDepartamentos(tupla):
    print(f"Número de departamento: ",tupla[0])
    print(f"Nombre de departamento: ",tupla[1])
    print(f"Coste: ",tupla[2])
    print(f"%: ",tupla[3])
    print('------------------------------')


def dbConsultarDepartamentos():
    print("---dbConsultarDepartamentos---")

    try:
        #Se establece la conexión con la base de datos de Oracle.
        cursor = conexion.cursor()
        #Se inicializa la petición a nuestra base de datos de Oracle. Para Oracle, a la hora de
        #realizar una petición, debemos inicializar los parametros de la consulta con :nom_propiedad. 
        #Esto nos permite evitar la inyección de código SQL.
        consulta = "SELECT * FROM Departamentos"

        #Se ejecuta la consulta
        cursor.execute(consulta)    

        #Se guarda en la variable "result" la información recuperada de la petición.   
        #En este caso, se trata de todas las filas existentes en la tabla "Departamentos"
        resul = cursor.fetchall()

        #Se imprime por pantalla la información recuperada. En este caso, como se trata de una lista, se itera
        for tupla in resul:
            mostrarValoresDepartamentos(tupla)
        print("Número de registros recuperados:",len(resul))
        print("Número de registros recuperados:",cursor.rowcount)
        print('------------------------------')
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error. No se han podido consultar las tuplas de Departamentos")
        print(error)

# ------------------------------------------------------------------

def dbInsertarDepartamentos():
    print("---dbInsertarDepartamentos---")

    try:
        cursor = conexion.cursor()

        numDpto = input("Introduce el número del departamento: ")
        nombreDpto = input("Introduce el nombre del departamento: ")
        costeDto = input("Introduce el coste del departamento: ")
        porcentajeDpto = input("Introduce el porcentaje del departamento: ")

        consulta = "INSERT INTO Departamentos VALUES ( %s, %s , %s , %s )"

        cursor.execute(consulta, [numDpto, nombreDpto, costeDto, porcentajeDpto])

        print("Tupla insertada correctamente")
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error. No se ha podido insertar el Departamento")
        print(error)

# ------------------------------------------------------------------

def controlTeclado():
    print("1- Nombre del departamento")
    print("2- Coste del departamento")
    print("3- Porcentaje del departamento")
    eleccion = input("Elige qué propiedad quieres actualizar de este departamento. (1-3)")
    print(int(eleccion))
    while( not ( 1<= int(eleccion) <= 3) ):
        eleccion = input("Lo sentimos. Elige un valor aceptado (1-3)")

    return eleccion
    
def controlSalir():
    salir = input("¿Desea realizar otra operación? (S/N): ")
    while(salir.lower()!= 's' and salir.lower()!= 'n'):
        
        salir = input("Valor no valido")
    match salir.lower():
        case 's':
            return True
        case 'n':
            return False
            

            

def dbModificarDepartamentos():
    print("---dbModificarDepartamentos---")
    salir = False
    try:
        cursor = conexion.cursor()
        while(not salir):
            numDpto = input("Introduce el número del departamento a actualizar: ")
            eleccion = controlTeclado()
            # nombreDpto = input("Introduce el nuevo nombre del departamento que quieres poner: ")
            # costeDto = input("Introduce el coste del departamento: ")
            # porcentajeDpto = input("Introduce el porcentaje del departamento: ")



            match int(eleccion):
                case 1:
                    nuevo_valor = input("Introduce el nuevo nombre del departamento que quieres poner: ")
                    consulta = "UPDATE departamentos SET nombredpto = %s WHERE numerodpto = %s"
                case 2:
                    nuevo_valor = input("Introduce el nuevo coste del departamento que quieres poner: ")
                    consulta = "UPDATE departamentos SET coste = %s WHERE numerodpto = %s"
                case 3:
                    nuevo_valor = input("Introduce el nuevo porcentaje del departamento que quieres poner: ")
                    consulta = "UPDATE departamentos SET porcent = %s WHERE numerodpto = %s"
            
                    
            # consulta = "UPDATE departamentos SET nombredpto = %s WHERE numerodpto = %s"

            cursor.execute(consulta, [nuevo_valor,numDpto])

            print("Tupla actualizada correctamente")
            consulta_actualizacion = "SELECT * FROM Departamentos WHERE numerodpto = %s"
            cursor.execute(consulta_actualizacion, [numDpto])

            resul = cursor.fetchone()
            print("-------- tupla actualizada ------------")
            mostrarValoresDepartamentos(resul)
            print('------------------------------')

            salir = controlSalir()
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error. No se ha podido modificar el Departamento")
        print(error)

# ------------------------------------------------------------------

def dbBorrarDepartamentos():
    print("---dbBorrarDepartamentos---")

    try:
        cursor = conexion.cursor()

        numDpto = input("Introduce el número del departamento a actualizar: ")
        #nombreDpto = input("Introduce el nuevo nombre del departamento que quieres poner: ")
        # costeDto = input("Introduce el coste del departamento: ")
        # porcentajeDpto = input("Introduce el porcentaje del departamento: ")

        consulta = "DELETE FROM departamentos WHERE numerodpto = %s"

        cursor.execute(consulta, [numDpto])

        print("Tupla borrada correctamente")
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error. No se ha podido borrar el Departamento")
        print(error)

# ------------------------------------------------------------------

def dbInsertarMultiplesDepartamentos():
    print("---dbInsertarMultiplesDepartamentos---")

    datos = [
        ('5', 'INVESTIGACIÓN',0.0,0.0),
        ('6', 'MARKETING',0.0,0.0),
        ('7', 'VENTAS',0.0,0.0)
    ]

    try:
        cursor = conexion.cursor()

        for fila in datos:
            consulta = "INSERT INTO Departamentos VALUES ( %s, %s , %s , %s)"
            
            cursor.execute(consulta, [fila[0], fila[1], fila[2], fila[3]])

            print("Tupla insertada correctamente")
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error. No se han podido insertar múltipes Departamentos")
        print(error)
        cursor.close()

# ------------------------------------------------------------------

def dbBorrarMultiplesDepartamentos():
    print('---dbBorrarMultiplesDepartamentos---')

    datos = [['5'], ['6'], ['7']]

    try:
        cursor = conexion.cursor()

        
        for fila in datos:
            consulta = "DELETE FROM departamentos WHERE numerodpto = %s"
            
            cursor.execute(consulta, [fila[0]])
            print("Tupla borrada correctamente")
        cursor.close()
    except PBD.DatabaseError as error:
        print("Error. No se han podido borrar múltiples Departamentos")
        print(error)
        cursor.close()

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

print("---Programa principal---")

conexion=dbConectar()

if (conexion is None):
    print("ERROR DE CONEXIÓN")
else:
    print("CONEXIÓN REALIZADA")

    # dbMostrarEmpleados1()
    # dbMostrarEmpleados2()
    # dbMostrarEmpleados3()
    # dbMostrarEmpleados4()
    
    # dbObtenerEmpleados()
    # dbConsultarEmpleados()
    # dbConsultarDepartamentos()

    # dbInsertarDepartamentos()
    # dbConsultarDepartamentos()

    dbModificarDepartamentos()
    dbConsultarDepartamentos()

    # dbBorrarDepartamentos()
    # dbConsultarDepartamentos()

    # dbInsertarMultiplesDepartamentos()
    # dbConsultarDepartamentos()
    
    # dbBorrarMultiplesDepartamentos()
    # dbConsultarDepartamentos()
    
    dbDesconectar()

print("---Fin de programa---")