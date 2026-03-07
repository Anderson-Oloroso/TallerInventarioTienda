def addProd(datos):
    try:
        nombreProd = input("Nombre del Producto: ").strip()
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad de producto: "))
        nuevo = {
            "nombre": nombreProd,
            "precio": precio, 
            "cantidad": cantidad
        }

        datos.append(nuevo)
        print("Producto Agregado correctamente")
    except Exception as e:
        print("Error: ",e)