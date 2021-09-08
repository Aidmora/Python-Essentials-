print("Emnpezando a trabajar con python")
print ("Mi nombre es: Ariel Mora")
# En este codigo se va a consulta los tipos de los siguientes valores
# Tipos de datos , boleanos , alfanumericos , numericos.
print("El tipo de dato de 875 es" , type(875))
print("El tipo de dato de 4.89 es" , type(4.89))
print("El tipo de dato del texto: Now is better than never. es:" , type("Now is better than never"))
print("El tipo de dato de 1.32 es" , type(1.32))
# a partir de la anidación de funciones print y type ,  Con la función print podemos imprimir en pantalla el texto y con la función type la clase a la que pertenece ese dato.
#la función type nos permite identificar la clase de un dato , en este caso tenemos 3 numéricos y un alfanumerico o (STRING)
complejo= complex (5, 8)
# asignacion de  un valor a la variable , en este se le define a estos dos datos como numero complejo (5+8j)
print("El valor 5+8i corresponde a un valor entero?" , isinstance(complejo ,int))
# con la funcion print imprimimos en pantalla el string , y con la funcion isinstance realizamos una comparacion de valor entre la variable y la clase int. Asi dandonos un resultado lgico (Fasle)

print("El valor 8.2 corresponde a un valor entero?" , isinstance(8.2 ,int))
#la funcion print imprimimos en pantalla el string , y con la funcion isinstance realizamos una comparacion de valor entre el dato y la clase int. Asi dandonos un resultado lgico (Fasle)

print("El  texto: Readability counts. corresponde a un string ?", isinstance(" Readability counts." ,str))
#la funcion print imprimimos en pantalla el string , y con la funcion isinstance realizamos una comparacion de valor entre el dato y la clase str. Asi dandonos un resultado lgico (True)
