import random
# Elementops del tablero 
#MURO_DESTRUCTIBLE = '#'
#MURO_INDESTRUCTIBLE = '▧'
#JUGADOR1 = 'P1'
#JUGADOR2 = 'P2'
#BOMBA = ''💣︎
#jugadores = ["P1", "P2"]

Tamano = int(input("Ingresa el tamaño del tablero: "))      

if Tamano >= 6:

    Tablero = [["x" if i == 0 or i == Tamano - 1 or j == 0 or j == Tamano - 1 else "." for j in range(Tamano)] for i in range(Tamano)]      Es una lista que dice "x" if ... else ".": Se decide qué poner en cada celda dependiendo de si está en el borde o no.
                                                                                                                                            for j in range(Tamano): Itera sobre las columnas.
                                                                                                                                            for i in range(Tamano): Itera sobre las filas en el nivel superior para crear fil

# Colocar al jugador "A" en la esquina superior izquierda                                                                                   Es una lista con las coordenadas de cada jugador siendo 
    Tablero[1][1] = "P1"

# Colocar al jugador "B" en la esquina inferior derecha
    Tablero[Tamano - 2][Tamano - 2] = "P2"

# Función para colocar muros aleatorios
    
    def colocar_muros(tamano, cant_ind, cant_destr): #definiendo cantidades                                                                Define una función llamada colocar_muros que toma tres parámetros: tamano, cant_ind (cantidad de muros indestructibles) y cant_destr (cantidad de muros destructibles).
        colocados = 0                                                                                                                        Inicializa la variable colocados en 0. Esta variable servirá como contador para llevar el registro de cuántos muros se han colocado en total.
        while colocados < cant_ind + cant_destr:                                                                                               Inicia un bucle while que continuará ejecutándose mientras el número de muros colocados sea menor que la suma de muros indestructibles y destructibles.
            fila = random.randint(1, tamano - 2)                                                                                                 Genera coordenadas aleatorias para una celda del tablero, asegurándose de que no caiga en los bordes (de 1 a tamano - 2) Para colocar muros en posiciones aleatorias dentro del área jugable del tablero.
            col = random.randint(1, tamano - 2)
        
        
            if Tablero[fila][col] == ".":           # Asegurarse de que no haya un jugador o muro ya en esa posición                               Verifica si la celda en las coordenadas aleatorias (fila, col) está vacía (es un ".").
                if colocados < cant_ind:           # Colocar muros indestructibles primero                                                           Comprueba si el número de muros colocados es menor que la cantidad de muros indestructibles que se deben colocar. Para decidir si se debe colocar un muro indestructible o destructibl
                    Tablero[fila][col] = "▧"                                                                                                          Coloca un muro indestructible ("▧") en la posición seleccionada aleatoriamente.
                else:                               # Luego colocar muros destructibles                                                                  Si ya se han colocado suficientes muros indestructibles, coloca un muro destructible ("#") en la misma posición.
                    Tablero[fila][col] = "#"
                colocados += 1                                                                                                                                Incrementa el contador colocados en 1. Para mantener un seguimiento de cuántos muros se han colocado hasta ahora, de modo que el bucle pueda finalizar cuando se alcance el número deseado.

# Definir la cantidad de muros a colocar
    cant_ind = (Tamano * Tamano) // 10 # Ejemplo: 10% del tablero como muros indestructibles - deja el 10 del tablero vacio                                            Calcula el área total del tablero en términos de celdas. Por ejemplo, si el tamaño es 10, entonces 10 * 10 = 100   Divide el área total por 10 utilizando división entera. Esto da como resultado el 10% del total de celdas del tablero. Siguiendo el ejemplo anterior, 100 // 10 sería 10.             
    cant_destr = (Tamano * Tamano) // 10 # Ejemplo: 10% del tablero como muros destructibles                                                                               La idea es que se designe un porcentaje del tablero (en este caso, el 10%) para muros indestructibles. Esto asegura que haya una cantidad fija de obstáculos en el tablero, sin importar su tamaño.

# Colocar los muros en el tablero
    colocar_muros(Tamano, cant_ind, cant_destr) # se llama la funcionn                                                                                                       La llamada a la función activa la lógica definida en colocar_muros. Sin esta llamada, la función existiría en el código, pero no se ejecutaría, por lo que no se colocarían los muros en el tablero.


# Colocar una bomba en el centro del tablero
    bomba_pos = (Tamano // 2, Tamano // 2)  # Centro del tablero divide entre 2 para colocarlo en el centro                                                                     Utiliza la división entera para encontrar la mitad del tamaño del tablero. La tupla (Tamano // 2, Tamano // 2) resulta en coordenadas que indican el centro del tablero.
    Tablero[bomba_pos[0]][bomba_pos[1]] = "💣︎"  # '💣︎' representa la bomba colo ca labomba segun el resultado de bomba_pos

# Mostrar el tablero
    for fila in Tablero:
        print(" ".join(fila)) #quita las comas y '' de la matriz

else:
    print("Ingresar número mayor a 6")
