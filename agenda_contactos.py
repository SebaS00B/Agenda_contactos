

def mostrar_menu ():
    print("Menu:")
    print("1. Ingresar datos de un nuevo contacto: ")
    print("2. Eliminar contacto exsitent : ")
    print("3. Buscar contacto existente: ")
    print("4. Lista de Contactos  :") 
    print("5.  Salir")

def agregar_contacto (agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    email = input("Ingrese el correo del contacto: ")
    agenda[nombre] = {"telefono", telefono , "email", email}
    print("Contacto agregado con exito")

def eliminar_contacto (agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado con exito")
    else :
        print("Contacto no existe")

def buscar_contacto (agenda):
    nombre = input("Ingrese el nombre del contacto que desee buscar: ")
    if nombre in agenda:
        print("Contacto encontrado: ", agenda)
    else :
        print("Contacto no encontrado")

def agenda_contactos ():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Ingrese la opcion que desee: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
           eliminar_contacto (agenda) 
        elif opcion == "3":
            buscar_contacto (agenda)
        elif opcion == "4":
            print("Lista de Contactos: ", agenda)
        elif opcion == "5":
            print("Adios")
            break
        else :
            print("Opcion no valida, por favor ingrese una opcion valida")

agenda_contactos()