# Trabajo-Final-Python

Este codigo funciona de la siguiente manera:
 Primero se presenta un menu interactivo con distintas opciones en donde para seleccionar una opcion se le pedira al usuario ingresar el numero de la opcion que desee.

 1. Al registrar un producto nuevo se le pide al usuario que ingrese el nombre del producto, una pequeña descripcion, la cantidad, el precio, la categoria a la que pertenece el producto y
 la cantidad del producto por la cual se debera generar un reporte de bajo stock.


 2. La opcion de mostrar producto muestra todos los productos que estan registrados en la base de datos mostrando el ID del producto, el nombre, la descripcion, la cantidad, la categoria, el precio y el umbral de bajo stock para el reporte.


 3. La opcion de actualizar producto permite actualizar la cantidad actual del producto seleccionado mediante su ID. El sistema de reporte de stock esta integrado en este apartado. Si el caso de que la nueva cantidad sea igual o inferior a la cantidad de bajo stock se generara un reporte que avisa al usuario que hay bajo stock de ese producto.

 
 4. La opcion de eliminar producto permite al usuario eliminar un producto registrado en la base de datos mediante el ID del mismo. Se le pide al usuario el ID del producto que desea eliminar y una vez ingresado el producto se elimina de la base de datos.

 5. La opcion de busqueda de producto permite al usuario buscar un producto por su nombre o ID. Tambien permite buscar productos por categoria funcionando mas como un filtro que como un campo de busqueda. Tambien añadi una opcion de salir y volver al menu principal por si el usuario se equivoco al seleccionar una opcion. En caso de no seleccionar una de las opciones al usuario le saldra un mensaje de opcion no valida.

 6. Finalmente si el usuario quiere finalizar el programa solamente tiene que seleccionar la opcion numerada Salir.
