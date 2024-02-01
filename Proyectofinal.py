import os

CARPETA = 'contactos/'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

        

def app():
    #Revisar si la carpeta existe
    crear_directorio()

    #Muestra el menu de opciones
    mostrar_menu()

    #Prguntar al usaurio que desea hacer

    preguntar = True
    while preguntar:
        opcion = input('Selecciona una opcion: \r\n')
        opcion = int(opcion)

        #Ejecutar la opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida')

def eliminar_contacto():
    nombre = input('¿Que contacto desea eliminar?: ')
    
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n contacto eliminado \r\n')
    except:
        print('No existe ese contacto')
    app()

def buscar_contacto():
    nombre = input('¿Que contacto busca?: ')

    try:
        with open (CARPETA + nombre + EXTENSION) as contacto:
            print(' \r\n Informacion del contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
    app()

def mostrar_contacto():
    archivo = os.listdir(CARPETA)

    archivo_txt = [i for i in archivo if i.endswith(EXTENSION)]

    for archivo in archivo_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
        
def editar_contacto():
    print('Escribe que contacto deseas editar')
    nombre_anterior = input('nombre del contacto: ')

    existe = existe_contacto(nombre_anterior)

    if existe:
        with open (CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            
            nombre_contacto= input('Agrega el nuevo nombre: ')
            telefono_contacto = input('Agrega el nuevo telefono: ')
            categoria_contacto= input('Agrega la neuva categoria: ')


            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: '+contacto.nombre+'\r\n'.rstrip() )
            archivo.write('Telefono: '+contacto.telefono+'\r\n' .rstrip())
            archivo.write('Categoria: '+contacto.categoria+'\r\n' .rstrip())

            ruta_anterior = CARPETA + nombre_anterior + EXTENSION
            ruta_nueva = CARPETA + nombre_contacto + EXTENSION

            os.rename(ruta_anterior, ruta_nueva)

            print('\r\n Contacto creado con exito\r\n')

    else:
        print('Ese contacto no existe')

def agregar_contacto():
    print('Escribe los datos para agregar el contacto')
    nombre_contacto = input('Nombre del contacto: ')

    existe =  existe_contacto(nombre_contacto)
    if not existe:
    
        with open (CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            
            telefono_contacto = input('Agrega el telefono: ')
            categoria_contacto= input('Categoria contacto: ')

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            
            archivo.write('Nombre: '+contacto.nombre+'\r\n' )
            archivo.write('Telefono: '+contacto.telefono+'\r\n' )
            archivo.write('Categoria: '+contacto.categoria+'\r\n' )

            print('\r\n Contacto creado con exito\r\n')
            archivo.close()
    else:
        print('Ya existe ese contacto')
    app()

def mostrar_menu():
    print('selecciona del menu lo que desea hacer: ')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
app()
