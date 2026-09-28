import json
import os

archivo_datos = 'gimnasio.json'

def cargar_datos():
    if not os.path.exists(archivo_datos):
        return {"clientes": [], "servicios": [], "instructores": ["Carlos", "Maria", "Pedro"]}
    with open(archivo_datos, 'r') as archivo:
        return json.load(archivo)

def guardar_datos(datos):
    with open(archivo_datos, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def registrar_cliente(datos):
    print("\n--- REGISTRO DE CLIENTE ---")
    identificacion = input("Numero de identificacion: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Direccion: ")
    celular = input("Celular: ")

def registrar_servicio(datos):
    pass

def matricular_cliente(datos):
    pass

def generar_reportes(datos):
    pass

def main():
    datos = cargar_datos()
    while True:
        print("\n--- GIMNASIO FORCETECH ---")
        print("1. Gestionar Inscripciones")
        print("2. Gestionar Servicios")
        print("3. Matricular Cliente")
        print("4. Generar Reportes")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            registrar_cliente(datos)
        elif opcion == "2":
            registrar_servicio(datos)
        elif opcion == "3":
            matricular_cliente(datos)
        elif opcion == "4":
            generar_reportes(datos)
        elif opcion == "5":
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()