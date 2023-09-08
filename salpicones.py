class Fruta:
    def __init__(self, id, nombre, precio_unitario, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def costo_total(self):
        return self.precio_unitario * self.cantidad


def ingresar_frutas():
    n = int(input("Ingrese la cantidad de frutas: "))
    frutas = []

    for i in range(1, n + 1):
        print(f"Ingrese los detalles de la fruta {i}:")
        nombre = input("Nombre: ")
        precio_unitario = float(input("Precio Unitario: "))
        cantidad = int(input("Cantidad: "))
        fruta = Fruta(i, nombre, precio_unitario, cantidad)
        frutas.append(fruta)

    return frutas


def costo_total_salpicon(frutas):
    costo_total = sum(fruta.costo_total() for fruta in frutas)
    print(f"El costo total del salpicón es: {costo_total}")

def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x.costo_total(), reverse=True)
    print("Frutas ordenadas por costo de mayor a menor:")
    for fruta in frutas_ordenadas:
        print(f"{fruta.nombre}: {fruta.costo_total()}")


def mostrar_fruta_mas_barata_y_mas_cara(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x.precio_unitario)
    fruta_mas_barata = frutas_ordenadas[0]
    fruta_mas_cara = frutas_ordenadas[-1]
    print(f"La fruta más barata es: {fruta_mas_barata.nombre} ({fruta_mas_barata.precio_unitario} por unidad)")
    print(f"La fruta más cara es: {fruta_mas_cara.nombre} ({fruta_mas_cara.precio_unitario} por unidad)")


frutas = ingresar_frutas()
costo_total_salpicon(frutas)
mostrar_frutas_ordenadas(frutas)
mostrar_fruta_mas_barata_y_mas_cara(frutas)
