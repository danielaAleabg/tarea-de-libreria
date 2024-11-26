

import datetime

PRECIO_MOTO = 500
PRECIO_CARRO = 1000

vehiculos = []

def calcular_duracion(entrada, salida):
    formato = "%H:%M"  # Formato de 24 horas
    entrada_dt = datetime.datetime.strptime(entrada, formato)
    salida_dt = datetime.datetime.strptime(salida, formato)
    duracion = (salida_dt - entrada_dt).total_seconds() / 60
    return int(duracion)

def calcular_precio(duracion, tipo):
    fracciones = duracion // 15
    if duracion % 15 != 0:
        fracciones += 1
    if tipo == 'MOTO':
        return fracciones * PRECIO_MOTO
    elif tipo == 'CARRO':
        return fracciones * PRECIO_CARRO

def registrar_entrada():
    tipo = input("Ingrese el tipo de vehículo (MOTO/CARRO): ").upper()
    placa = input("Ingrese la placa del vehículo: ").upper()
    hora_entrada = input("Ingrese la hora de entrada (HH:MM en formato 24 horas): ")
    
    vehiculo = {
        'tipo': tipo,
        'placa': placa,
        'hora_entrada': hora_entrada,
        'hora_salida': None,
        'duracion': None,
        'precio': None
    }
    
    vehiculos.append(vehiculo)
    print(f"Vehículo {tipo} con placa {placa} registrado a las {hora_entrada}.\n")

def registrar_salida():
    placa = input("Ingrese la placa del vehículo que va a salir: ").upper()
    
    for vehiculo in vehiculos:
        if vehiculo['placa'] == placa and vehiculo['hora_salida'] is None:
            hora_salida = input("Ingrese la hora de salida (HH:MM en formato 24 horas): ")
            vehiculo['hora_salida'] = hora_salida
            duracion = calcular_duracion(vehiculo['hora_entrada'], hora_salida)
            vehiculo['duracion'] = duracion
            vehiculo['precio'] = calcular_precio(duracion, vehiculo['tipo'])
            
            print(f"Vehículo {vehiculo['tipo']} con placa {vehiculo['placa']} ha permanecido {duracion} minutos.")
            print(f"El valor a pagar es: ${vehiculo['precio']}.\n")
            return
    print("Vehículo no encontrado o ya registrado como salido.\n")

def mostrar_resumen():
    total_carros = sum(1 for v in vehiculos if v['tipo'] == 'CARRO')
    total_motos = sum(1 for v in vehiculos if v['tipo'] == 'MOTO')
    dinero_carros = sum(v['precio'] for v in vehiculos if v['tipo'] == 'CARRO' and v['precio'] is not None)
    dinero_motos = sum(v['precio'] for v in vehiculos if v['tipo'] == 'MOTO' and v['precio'] is not None)
    
    print(f"Resumen del día:")
    print(f"Total de carros ingresados: {total_carros}")
    print(f"Total de motos ingresadas: {total_motos}")
    print(f"Dinero recaudado por carros: ${dinero_carros}")
    print(f"Dinero recaudado por motos: ${dinero_motos}\n")

def menu():
    while True:
        print("1. Registrar entrada de vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar resumen del parqueadero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_entrada()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

menu()
