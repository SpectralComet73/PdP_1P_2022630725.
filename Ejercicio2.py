#Carlos Alexis Rendon Sierra
#Ethel Padilla Rodriguez
#3BV2

#2. Diseña y escribe un programa que ordene una pila de tal forma que los elementos más pequeños estén enla parte superior. 
#Es posible emplear una pila auxiliar, pero no será posible copiar todos los valores a un arreglo.
# La pila deberá implementar las operaciones push,pop, isEmpty y peek (visualizar el contenido de la pila).

#Se crea la clase Pila
class Pila:
    #Se inicializa el constructor de la clase Pila
    #self.items es una lista que almacena los elementos de la pila 
    def __init__(self): #self es una referencia a la instancia de la clase Pila que se esta creando 
        self.items = []
    #Se define el método push que agrega un elemento a la pila
    def push(self, item):
        self.items.append(item)
    #Se define el método pop que elimina un elemento de la pila
    def pop(self):
        return self.items.pop()
    #Se define el método isEmpty que retorna True si la pila esta vacía y False en caso contrario
    def isEmpty(self):
        return self.items == []
    #Se define el método peek que retorna el elemento que se encuentra en la cima de la pila
    def peek(self):
        return self.items[len(self.items)-1]
    #Se define el método __str__ que retorna un string con los elementos de la pila
    def __str__(self):
        return str(self.items)
#Se crea un objeto de la clase Pila
pila = Pila()
#Se le pregunta al usuaario cuantos elementos desea agregar a la pila
n = int(input("\n¿Cuantos elementos desea agregar a la pila? \n"))
#Se crea un ciclo for para agregar los elementos a la pila
for i in range(n):
    #Se le pregunta al usuario el elemento que desea agregar a la pila
    elemento = int(input("\nIngrese el elemento que desea agregar a la pila: \n"))
    #Se agrega el elemento a la pila
    pila.push(elemento)
#Se imprime la pila
print(pila)
#Se crea una pila auxiliar
pilaAux = Pila()
#Se crea un ciclo while que se ejecuta mientras la pila no este vacía
while not pila.isEmpty():
    #Se almacena el elemento que se encuentra en la cima de la pila en la variable aux
    aux = pila.pop()
    #Se crea un ciclo while que se ejecuta mientras la pila auxiliar no este vacía y el elemento que se encuentra en la cima de la pila auxiliar sea mayor que aux
    while not pilaAux.isEmpty() and pilaAux.peek() > aux:
        #Pila auxiliar elimina el elemento que se encuentra en la cima de la pila auxiliar y lo almacena en la variable temp 
        temp = pilaAux.pop()
        #Se agrega el elemento temp a la pila
        pila.push(temp)
    #Se agrega el elemento aux a la pila auxiliar
    pilaAux.push(aux)
#Se crea un ciclo while que se ejecuta mientras la pila auxiliar no este vacía
while not pilaAux.isEmpty():
    #Se almacena el elemento que se encuentra en la cima de la pila auxiliar en la variable temp
    temp = pilaAux.pop()
    #Se agrega el elemento temp a la pila
    pila.push(temp)
#Se imprime la pila
print("\nLa pila ordenada con los elementos menores en la cima es: \n", pila)


    