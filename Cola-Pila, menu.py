from collections import deque

cola_pacientes = deque()

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Pacientes en recepción")
        print("2. Farmacia")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_pacientes()
        elif opcion == '2':
            print("Funcionalidad de Farmacia aún no implementada.")
        elif opcion == '3':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_pacientes():
    while True:
        print("\n--- MENÚ PACIENTES ---")
        print("1. Agregar pacientes")
        print("2. Turno pacientes")
        print("3. Mostrar cola actual")
        print("4. Menú Principal")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_paciente()
        elif opcion == '2':
            turno_paciente()
        elif opcion == '3':
            mostrar_cola()
        elif opcion == '4':
            return  # Regresa al menú principal
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta pronto!")
            exit()
        else:
            print("Opción inválida. Intente de nuevo.")

def agregar_paciente():
    while True:
        print("\n>>> Ingreso de nuevo paciente")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        malestar = input("Malestar: ")

        paciente = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "malestar": malestar
        }

        cola_pacientes.append(paciente)
        print("Paciente agregado exitosamente.")

        decision = input("¿Desea agregar otro paciente? (s/n): ").lower()
        if decision != 's':
            break

def turno_paciente():
    if cola_pacientes:
        paciente = cola_pacientes.popleft()
        print("\n>>> Turno del siguiente paciente:")
        print(f"Nombre: {paciente['nombre']} {paciente['apellido']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Malestar: {paciente['malestar']}")
    else:
        print("\nNo hay pacientes en espera.")

    decision = input("¿Desea regresar al MENÚ PACIENTES? (s/n): ").lower()
    if decision != 's':
        print("Saliendo del sistema. ¡Hasta pronto!")
        exit()

def mostrar_cola():
    if cola_pacientes:
        print("\n>>> Cola actual de pacientes:")
        for i, paciente in enumerate(cola_pacientes, 1):
            print(f"{i}. {paciente['nombre']} {paciente['apellido']} - Edad: {paciente['edad']} - Malestar: {paciente['malestar']}")
    else:
        print("\nNo hay pacientes en espera.")

    decision = input("\n¿Desea regresar al MENÚ PACIENTES? (s/n): ").lower()
    if decision != 's':
        print("Saliendo del sistema. ¡Hasta pronto!")
        exit()


# Ejecutar el menú principal
menu_principal()