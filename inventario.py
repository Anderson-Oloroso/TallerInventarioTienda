import json
from main import separador
def addProd():
    nombreProd = input("Nombre del Producto: ").strip()
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad de producto: "))
    encontrado = False
    nuevo = {
            "nombre": nombreProd,
            "precio": precio, 
            "cantidad": cantidad
    }
    with open("inventario.json", "r") as file:
        datos = json.load(file)

    for dato in datos:
            if nombreProd.lower() in dato['nombre'].lower():
                encontrado = True
                break
    
    if encontrado:
        separador()
        print("El producto que intenta agregar ya existe\n")
    else:
        datos.append(nuevo)
        with open("inventario.json", "w") as f:
            try:
                json.dump(datos, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("\nLibro agregado correctamente")