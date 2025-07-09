from collections import deque

# Cola para pacientes en recepción (FIFO)
cola_pacientes = deque()

# Pila para medicamentos en farmacia (LIFO)
pila_medicamentos = []

def menu():
    while True:
        print("\n=== MENÚ DE CLÍNICA ===")
        print("1. Registrar paciente")
        print("2. Atender paciente")
        print("3. Agregar medicamento")
        print("4. Entregar medicamento")
        print("5. Ver pacientes en espera")
        print("6. Ver medicamentos en farmacia")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_paciente()
        elif opcion == '2':
            atender_paciente()
        elif opcion == '3':
            agregar_medicamento()
        elif opcion == '4':
            entregar_medicamento()
        elif opcion == '5':
            ver_pacientes()
        elif opcion == '6':
            ver_medicamentos()
        elif opcion == '7':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    cola_pacientes.append(nombre)
    print(f"Paciente '{nombre}' registrado correctamente.")

def atender_paciente():
    if cola_pacientes:
        atendido = cola_pacientes.popleft()
        print(f"Atendiendo al paciente: {atendido}")
    else:
        print("No hay pacientes en espera.")

def agregar_medicamento():
    medicamento = input("Ingrese el nombre del medicamento: ")
    pila_medicamentos.append(medicamento)
    print(f"Medicamento '{medicamento}' agregado a la farmacia.")

def entregar_medicamento():
    if pila_medicamentos:
        entregado = pila_medicamentos.pop()
        print(f"Entregado medicamento: {entregado}")
    else:
        print("No hay medicamentos en la farmacia.")

def ver_pacientes():
    if cola_pacientes:
        print("Pacientes en espera:")
        for paciente in cola_pacientes:
            print(f"- {paciente}")
    else:
        print("No hay pacientes en espera.")

def ver_medicamentos():
    if pila_medicamentos:
        print("Medicamentos en farmacia:")
        for medicamento in reversed(pila_medicamentos):  # Muestra desde el último agregado
            print(f"- {medicamento}")
    else:
        print("No hay medicamentos en la farmacia.")

# Ejecutar el menú
menu()
