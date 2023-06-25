# Imprimir y devolver 
def imprimir(lista):
    print(lista[0])
    return lista[1]


resultado = imprimir([1, 2])
print(resultado) 


# primero mas longitud 
def primero(lista):
    return lista[0] + len(lista)

resultado = primero([3, 1, 4, 1, 5, 9])
print(resultado)

# longitud
def crear_lista(tamaño, valor):
    lista = []
    for i in range(tamaño):
        lista.append(valor)
    return lista
mi_lista = crear_lista(4, "Hola")
print(mi_lista) 




