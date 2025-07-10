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





-------------------------


from collections import deque
cola_pacientes = deque()


def menu_principal():
    while True:
        print("\nBIENVENIDO AL MENÚ PRINCIPAL CLÍNICA\n  ")
        print("1. Pacientes en recepción")
        print("2. Farmacia")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_pacientes()
        elif opcion == '2':
          print(" menu_farmacia()")
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Esta opción no es válida.  Intente nuevamente.")

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
            return
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
def turno_paciente():
    if cola_pacientes:
        paciente = cola_pacientes[0]  # Mostramos al primero sin sacarlo aún
        print("\n>>> TURNO DEL PACIENTE <<<")
        print(f"Nombre: {paciente['nombre']} {paciente['apellido']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Malestar: {paciente['malestar']}")

        confirmado = input("¿El paciente ya fue revisado? (s/n): ").lower()
        if confirmado == 's':
            cola_pacientes.popleft()
            print(f"Paciente {paciente['nombre']} ha sido atendido y removido de la cola.")
        else:
            print(f"Espere que haya finalizado la revisión del paciente: {paciente['nombre']}.")

    else:
        print("\nNo hay pacientes en espera.")

    decision = input("\n¿Desea regresar al MENÚ PACIENTES? (s/n): ").lower()
    if decision != 's':
        print("Saliendo del sistema. ¡Hasta pronto!")
        exit()



menu_principal()