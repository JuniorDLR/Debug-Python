def buscar_numero(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:  
            return i  
    return -1

def main():
    numeros = [30, 20, 8, 40, 50]
    objetivo = 30
    resultado = buscar_numero(numeros, objetivo)  
    if resultado:
        print("Número encontrado en el índice", resultado)  
    else:
        print("Número no encontrado")

main()