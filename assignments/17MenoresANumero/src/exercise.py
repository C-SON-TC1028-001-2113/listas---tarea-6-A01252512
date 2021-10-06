def menoresADiez(matrix):
    menorADiez = []
    for i in range(len(matrix)):
        
        for j in range(len(matrix[i])):
            if matrix[i][j] < 10:
                menorADiez.append(matrix[i][j])
    
    return menorADiez

def entradaDatos():
    matriz = []
    filas = int(input())
    column = int(input())

    for i in range(filas):
        matriz.append([])

        for j in range(column):
            dato = int(input())
            matriz[i].append(dato)
    
    return menoresADiez(matriz)


def main():
    print(entradaDatos())



if __name__=='__main__':
    main()