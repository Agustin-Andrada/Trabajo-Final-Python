from colorama import Fore
from database import conectar

#--------------- Funcion Agregar Producto ---------------

def agregar_producto():
    """Agrega un nuevo producto al inventario."""
    print(Fore.GREEN + "\n--- Registrar Producto ---")
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")
    bajo_stock = int(input("Umbral de bajo stock: "))
    
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria, bajo_stock)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria, bajo_stock))
    conexion.commit()
    conexion.close()
    print(Fore.CYAN + "Producto registrado con éxito.")


#--------------- Funcion Mostrar Producto ---------------

def mostrar_productos():
    """Muestra todos los productos del inventario."""
    print(Fore.GREEN + "\n--- Lista de Productos ---")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conexion.close()
    if productos:
        for producto in productos: # Este bucle imprime cada producto de forma que solo las etiquetas quedan en amarillo
            etiquetas = ["ID", "Nombre", "Descripción", "Cantidad", "Precio", "Categoría", "Bajo Stock"]
            for etiqueta, valor in zip(etiquetas, producto):  
                if etiqueta == "Precio":
                    valor = f"${valor:.2f}"  
                print(Fore.YELLOW + f"{etiqueta}:" + Fore.RESET + f" {valor}")
            print() 
    else:
        print(Fore.RED + "No hay productos registrados.")


#--------------- Funcion Actualizar Producto ---------------

def actualizar_producto():
    """Actualiza la cantidad de un producto específico."""
    print(Fore.GREEN + "\n--- Actualizar Producto ---")
    id_producto = int(input("ID del producto a actualizar: "))
    nueva_cantidad = int(input("Nueva cantidad: "))
    
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT bajo_stock FROM productos WHERE id = ?', (id_producto,))
    resultado = cursor.fetchone()
    
    
    if resultado: 
        bajo_stock = resultado[0] #Informe de bajo stock
        cursor.execute('''
            UPDATE productos SET cantidad = ? WHERE id = ?
        ''', (nueva_cantidad, id_producto))
        conexion.commit()
        print(Fore.CYAN + "Producto actualizado con éxito.")
        if nueva_cantidad <= bajo_stock:   # Si la nueva cantidad es menor o igual que el valor de bajo stock se genera el informe
            print(Fore.RED + f"¡ALERTA! El producto con ID {id_producto} está con bajo stock.")
    else:
        print(Fore.RED + "Producto no encontrado.")
    
    conexion.close()


##--------------- Funcion Buscar Producto ---------------

def buscar_producto():
    """Busca un producto por ID, nombre o categoría, con opción de salir."""
    while True:
        print(Fore.GREEN + "\n--- Buscar Producto ---")
        print(Fore.CYAN + "Opciones de búsqueda:")
        print(Fore.YELLOW + "1. Buscar por ID")
        print("2. Buscar por Nombre")
        print("3. Buscar por Categoría")
        print("4. Salir y volver al menú principal")
        opcion = input(Fore.YELLOW + "Seleccione una opción: ")

        # Mapa de campos para búsquedas
        campos = {"1": "id", "2": "nombre", "3": "categoria"}

        if opcion == "4":
            print(Fore.CYAN + "Volviendo al menú principal...")
            break

        if opcion not in campos:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")
            continue

        # Solicitar el criterio de búsqueda
        valor_busqueda = input(Fore.CYAN + f"Ingrese el {campos[opcion]} del producto: ")

        # Construir la consulta SQL
        query = f"SELECT * FROM productos WHERE {campos[opcion]} LIKE ?"

        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute(query, (f"%{valor_busqueda}%",))
            resultados = cursor.fetchall()

        # Mostrar resultados
        if resultados:
            print(Fore.CYAN + "\nResultados encontrados:")
            for producto in resultados:
                print(Fore.YELLOW + f"ID: {producto[0]}, Nombre: {producto[1]}, "
                                    f"Descripción: {producto[2]}, Cantidad: {producto[3]}, "
                                    f"Precio: ${producto[4]:.2f}, Categoría: {producto[5]}, "
                                    f"Bajo Stock: {producto[6]}")
        else:
            print(Fore.RED + "No se encontraron productos con los criterios ingresados. Intente nuevamente.")


#--------------- Funcion Eliminar Producto ---------------

def eliminar_producto():
    """Elimina un producto del inventario."""
    print(Fore.GREEN + "\n--- Eliminar Producto ---")
    id_producto = int(input("ID del producto a eliminar: "))
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    conexion.commit()
    conexion.close()
    print(Fore.CYAN + "Producto eliminado con éxito.")
