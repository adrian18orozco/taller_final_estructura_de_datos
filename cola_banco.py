N = 14
CAPACIDAD_MAX = (N % 4) + 3


class ColaBanco:
    def __init__(self, capacidad_max):
        self.clientes = []
        self.capacidad_max = capacidad_max

    def esta_vacia(self):
        return len(self.clientes) == 0

    def esta_llena(self):
        return len(self.clientes) == self.capacidad_max

    def encolar(self, nombre):
        if self.esta_llena():
            print(f"La cola está llena (máximo {self.capacidad_max} clientes). No se pudo agregar a {nombre}.")
        else:
            self.clientes.append(nombre)
            print(f"{nombre} tomó turno en la posición {len(self.clientes)}.")

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía, no hay clientes para atender.")
        else:
            atendido = self.clientes.pop(0)
            print(f"Atendiendo a: {atendido}")

    def ver_frente(self):
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            print(f"Siguiente en ser atendido: {self.clientes[0]}")

    def mostrar(self):
        if self.esta_vacia():
            print("La cola está vacía.")
        else:
            print(f"Clientes en espera {len(self.clientes)}:")
            print(self.clientes)


cola = ColaBanco(CAPACIDAD_MAX)
print(f"N = {N}  |  capacidadMax = {CAPACIDAD_MAX}")

while True:
    print("\n--- BANCO: COLA DE TURNOS ---")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Ver siguiente cliente")
    print("4. Mostrar cola")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        cola.encolar(nombre)
        print("")

    elif opcion == "2":
        cola.desencolar()
        print("")

    elif opcion == "3":
        cola.ver_frente()
        print("")

    elif opcion == "4":
        cola.mostrar()
        print("")

    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. | Ingresa un valor entre el 1 y el 5")
        print("")