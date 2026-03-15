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
    
    if encontrado == True:
        print("\nEl producto que intenta agregar ya existe")
    else:
        datos.append(nuevo)
        with open("inventario.json", "w") as f:
            try:
                json.dump(datos, f, indent=4)
            except Exception as e:
                 print("Error: ", e)
            else:
                print("\nProducto agregado correctamente")

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

def actCantidad():
    try:
        with open("inventario.json", "r") as file:
            datos = json.load(file)
    except Exception as e:
        print("Error: ",e)

    producto = input("Nombre del producto a actualizar: ").lower().strip()
    encontrado = True
    for dato in datos:
        if producto in dato['nombre'].lower():
            encontrado = True
            print(f"\nProducto encontrado.")
            nuevo = int(input("Nueva Cantidad disponible: "))
            dato['cantidad'] = nuevo
            break
        else:
            encontrado = False

    if encontrado == False:
        print("\nEl producto que intenta actualizar no existe")
    else:
        with open("inventario.json", "w") as f:
            try:
                json.dump(datos, f, indent=4)
                print("\nCantidad actualizada correctamente")
            except Exception as e:
                print("Error: ", e)
                

def delProduct():
    try:
        with open("inventario.json", "r") as file:
            datos = json.load(file)
    except Exception as e:
        print("Error: ",e)
    encontrado = True
    producto = input("Nombre del producto a eliminar: ").lower().strip()
    for i, dato in enumerate(datos):
            if producto not in dato['nombre'].lower():
                encontrado = False
                break
    
    if encontrado == False:   
        print("\nEl producto que intenta eliminar no existe")
    else:
        _ = 0
        while _ < len(datos):
            if producto in datos[_]['nombre'].lower():
                datos.pop(_)
            else:
                _+= 1

        with open("inventario.json", "w") as f:
            try:
                json.dump(datos, f, indent=4)
            except Exception as e:
                print("Error: ", e)
            else:
                print("\nProducto eliminado correctamente")

def valTotalInventario():
    total = 0
    try:
        with open("inventario.json", "r") as file:
            datos = json.load(file)
    except Exception as e:
        print("Error: ",e)

    _ = 0
    print("Valor total del inventario: Precio * Cantidad")
    for dato in datos:
        _ += 1
        valProducto = dato['precio'] * dato['cantidad']
        print(f"{_}. {dato['nombre']}: {dato['precio']} * {dato['cantidad']} = Q{valProducto:,.2f}")
        total += valProducto

    
    print(f"\nEl valor total del inventario es: Q{total:,.2f}")