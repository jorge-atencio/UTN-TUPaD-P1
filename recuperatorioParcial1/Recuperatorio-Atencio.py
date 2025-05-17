#Recuperatorio 1er parcial Programación I
#Alumno ATENCIO, jorge Ignacio
#Comisión 24

# Se inician las listas a utilizar
nombres = []
cantidades = []

# Se inicia variable salir 
salir = False

# Se crea el menú
while not salir:
    # Mostrar menú
    print("\n Menú de opciones:")
    print("1- Agregar producto")
    print("2- Ver productos agotados")
    print("3- Actualizar stock")
    print("4- Ver todos los productos")
    print("5- Salir")
    
    opcion = 0

    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ").strip()
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad en stock:"))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("Ingrese un número válido.")
        nombres.append(nombre)
        cantidades.append(cantidad)
        print("El producto due agregado")
    elif opcion == "2":
        print("Productos agotados:")
        agotados = False
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print("- " + nombres[i])
                agotados = True
        if not agotados:
            print("los productos tienen stock.")
 
    elif opcion == "3":
        producto = input("Ingrese el nombre del producto:").strip()
        encontrado = False
        for i in range(len(nombres)):
            if nombres[i] == producto:
                encontrado = True
                while True:
                    try:
                        nueva_cantidad = int(input("Ingrese la nueva cantidad:"))
                        if nueva_cantidad < 0:
                            print("La cantidad no puede ser negativa")
                        else:
                            break
                    except ValueError:
                        print("Ingrese un número válido")
                        
                cantidades[i] = nueva_cantidad
                print("Stock actualizado")
                break
        if not encontrado:
            print("Producto no encontrado")
    elif opcion == "4":
        print("\nListado de productos:")
        if len(nombres) == 0:
            print("No hay productos registrados.")
        else:
            for i in range(len(nombres)):
                print(f"- {nombres[i]}: {cantidades[i]} unidades")
    elif opcion == "5":
        print("Gracias por usar nuestro sistema")
        salir = True
    else:
        print("Opción inválida")
