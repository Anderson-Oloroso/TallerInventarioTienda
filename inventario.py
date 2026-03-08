import json

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
    try:
        with open("inventario.json", "r") as file:
            datos = json.load(file)
    except Exception as e:
        print("Error: ",e)

    for dato in datos:
            if nombreProd.lower() in dato['nombre'].lower():
                encontrado = True
                break
    
    if encontrado:
        print("\nEl producto que intenta agregar ya existe")
    else:
        datos.append(nuevo)
        with open("inventario.json", "w") as f:
            try:
                json.dump(datos, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("\nLibro agregado correctamente")

def listProducts():
    try:
        with open("inventario.json", "r") as file:
            datos = json.load(file)
    except Exception as e:
        print("Error: ",e)

    _ = 0
    for dato in datos:
        _+=1
        print(f"{_}. Nombre: {dato['nombre']}\nPrecio: {dato['precio']}\nCantidad: {dato['cantidad']}\n")