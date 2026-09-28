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
    pass

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

def registrar_servicio(datos):
    print("\n--- REGISTRO DE SERVICIO ---")
    nombre = input("Nombre del servicio: ")
    capacidad = int(input("Capacidad maxima de personas: "))
    servicio = {"nombre": nombre, "capacidad": capacidad, "inscritos": 0}
    datos["servicios"].append(servicio)
    guardar_datos(datos)
    print("Servicio guardado.")

def matricular_cliente(datos):
    id_cliente = input("ID del cliente a matricular: ")
    print("Servicios disponibles:")
    for i in range(len(datos["servicios"])):
        print(str(i) + ". " + datos["servicios"][i]["nombre"])
        
    opcion = int(input("Seleccione el numero de servicio: "))
    servicio_seleccionado = datos["servicios"][opcion]
    
    if servicio_seleccionado["inscritos"] < servicio_seleccionado["capacidad"]:
        servicio_seleccionado["inscritos"] = servicio_seleccionado["inscritos"] + 1
        guardar_datos(datos)
        print("Matricula exitosa.")
    else:
        print("No hay cupos disponibles.")