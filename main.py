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
    estado = input("Estado (En proceso, Inscrito, Activo, Inactivo): ")
    riesgo = input("Nivel de riesgo (alto, medio, bajo): ")
    
    cliente = {
        "id": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "celular": celular,
        "estado": estado,
        "riesgo": riesgo,
        "servicios_matriculados": []
    }
    datos["clientes"].append(cliente)
    guardar_datos(datos)
    print("Cliente registrado con exito.")


def registrar_servicio(datos):
    pass

def matricular_cliente(datos):
    pass

def generar_reportes(datos):
    print("\n--- MENU DE REPORTES ---")
    print("1. Listar clientes inscritos")
    print("2. Listar servicios y capacidad")
    print("3. Listar clientes con riesgo alto")
    opcion = input("Seleccione un reporte: ")
    
    if opcion == "1":
        for c in datos["clientes"]:
            print(c["id"] + " - " + c["nombres"] + " (" + c["estado"] + ")")
    elif opcion == "2":
        for s in datos["servicios"]:
            print(s["nombre"] + " | Capacidad: " + str(s["capacidad"]) + " | Inscritos: " + str(s["inscritos"]))
    elif opcion == "3":
        for c in datos["clientes"]:
            if c["riesgo"] == "alto":
                print(c["nombres"] + " " + c["apellidos"] + " - Riesgo Alto")

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