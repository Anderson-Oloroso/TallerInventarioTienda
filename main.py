def separador():
    print("="*20)

def menu():
    mensaje = """      SISTEMA DE INVENTARIO
    1. Agregar Producto
    2. Listar Productos
    3. Actualizar Cantidad
    4. Eliminar Producto
    5. Calcular valor total del inventario
    6. Salir
"""
    print(mensaje)
    op = int(input("Ingrese una opcion: "))

def main():
    separador
    op = menu()
    separador
    while True:
        if op == 1:
            separador()
            print("AGREGAR PRODUCTO")
        if op == 2:
            print("LISTAR PRODUCTOS")