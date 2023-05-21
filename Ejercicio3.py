#Carlos Alexis Rendon Sierra
#Ethel Padilla Rodriguez
#3BV2

#Diseña y escribe un programa que,empleando Orientación a Objetos, determine cuál es el par más cercano de puntos en 3D. Los puntos tendrán la estructura 𝑃(𝑥,𝑦,𝑧)
#Utilizar la distancia euclidiana para determinar la distancia entre dos puntos.
#Probarlo con 20 puntos generados aleatoriamente.

#Se importa la librería random para generar números aleatorios y la librería math para realizar operaciones matemáticas
import random
import math

#Se crea la clase Punto
class Punto:
    def __init__(self, x, y, z): #Se inicializan los atributos x, y, z desde el constructor de la clase Punto llamado __init__
        self.x = x
        self.y = y
        self.z = z

def distancia_euclidiana(punto1, punto2): #Se define la función distancia_euclidiana que recibe dos puntos y retorna la distancia euclidiana entre ellos
    dx = punto2.x - punto1.x #Se calcula la distancia en x entre los dos puntos
    dy = punto2.y - punto1.y #Se calcula la distancia en y entre los dos puntos
    dz = punto2.z - punto1.z #Se calcula la distancia en z entre los dos puntos
    distancia = math.sqrt(dx**2 + dy**2 + dz**2) #Se calcula la distancia euclidiana entre los dos puntos
    return distancia #Se retorna la distancia euclidiana entre los dos puntos

def encontrar_par_mas_cercano(puntos): #Se define la función encontrar_par_mas_cercano que recibe una lista de puntos y retorna el par más cercano de puntos
    if len(puntos) < 2: #Se valida que la lista de puntos tenga al menos dos puntos para poder calcular la distancia entre ellos
        return None #Si la lista de puntos tiene menos de dos puntos se retorna None
    
    par_mas_cercano = (puntos[0], puntos[1]) #Se inicializa el par más cercano de puntos con los dos primeros puntos de la lista de puntos
    distancia_minima = distancia_euclidiana(puntos[0], puntos[1]) #Se inicializa la distancia mínima con la distancia euclidiana entre los dos primeros puntos de la lista de puntos
    
    for i in range(len(puntos)): #Se crea un ciclo for que se ejecuta desde 0 hasta la longitud de la lista de puntos
        for j in range(i + 1, len(puntos)): #Se crea un ciclo for que se ejecuta desde i + 1 hasta la longitud de la lista de puntos
            distancia_actual = distancia_euclidiana(puntos[i], puntos[j]) #Se calcula la distancia euclidiana entre los puntos i y j
            if distancia_actual < distancia_minima: #Se valida si la distancia actual es menor que la distancia mínima
                distancia_minima = distancia_actual # Si la distancia actual es menor que la distancia mínima se actualiza la distancia mínima
                par_mas_cercano = (puntos[i], puntos[j]) #Si la distancia actual es menor que la distancia mínima se actualiza el par más cercano de puntos
    
    return par_mas_cercano #Se retorna el par más cercano de puntos

#Se crean puntos aleatorios entre -100 y 100 que se guardan en un arreglo llamado puntos
puntos = []
for i in range(20):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    z = random.randint(-100, 100)
    puntos.append(Punto(x, y, z))
#Se imprimen los puntos generados aleatoriamente
for punto in puntos:
    print(f"({punto.x}, {punto.y}, {punto.z})")

#Se llama a la función encontrar_par_mas_cercano que recibe la lista de puntos y se almacena en la variable par_mas_cercano
par_mas_cercano = encontrar_par_mas_cercano(puntos)

#Se imprime el par más cercano de puntos y la distancia entre ellos
print(f"El par más cercano de puntos es: ({par_mas_cercano[0].x}, {par_mas_cercano[0].y}, {par_mas_cercano[0].z}) y ({par_mas_cercano[1].x}, {par_mas_cercano[1].y},- {par_mas_cercano[1].z})")
print(f"La distancia entre ellos es: {distancia_euclidiana(par_mas_cercano[0], par_mas_cercano[1])}")
