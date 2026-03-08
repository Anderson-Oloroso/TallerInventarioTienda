import sys
from inventario import *
def separador():
    print("========================================")

def menu():
    mensaje = """    1. Agregar Producto
    2. Listar Productos
    3. Actualizar Cantidad
    4. Eliminar Producto
    5. Calcular valor total del inventario
    6. Salir
"""
    separador()
    print("      SISTEMA DE INVENTARIO")
    separador()
    print(mensaje)
    

def main():
    while True:
        menu()
        try: 
            op = int(input("Ingrese una opcion: "))
            if op == 1:
                separador()
                print("AGREGAR PRODUCTO")
                separador()
                addProd()
            elif op == 2:
                separador()
                print("LISTAR PRODUCTOS")
                separador()
                listProducts()
            elif op == 3: 
                separador()
                print("ACTUALIZAR CANTIDAD")
                separador()
                actCantidad()
            elif op == 4:
                separador()
                print("ELIMINAR PRODUCTO")
                separador()
                delProduct()
            elif op == 5:
                separador()
                print("CALCULAR EL VALOR DEL INVENTARIO")
                separador()
                valTotalInventario()
            elif op == 6:
                separador()
                print("SALIENDO DEL PROGRAMA ...")
                sys.exit(0)
            else:
                separador()
                print("Opción inválida")
        except ValueError as v:
            print("Error: ", v)
            
if __name__ == "__main__": 
    main() 