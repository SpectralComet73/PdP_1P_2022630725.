#Carlos Alexis Rendon Sierra
#Ethel Padilla Rodriguez
#3BV2

#1.Diseña e implementa una pila en la que adicionalmente a las operaciones push y pop, tengas una función min que proporcione el menor elemento en la pila.

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
    #Se define el método min que retorna el elemento mínimo de la pila
    def min(self):
        return min(self.items)
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
#Se imprime el elemento mínimo de la pila
print("\nEl elemento mínimo de la pila es: \n", pila.min())
#En una pila solo se puede eliminar el elemento que se encuentra en la cima de la pila 
#Se elimina el elemento que se encuentra en la cima de la pila
pila.pop()
#Se imprime la pila
print("\nLa pila después de eliminar el elemento que se encuentra en la cima de la pila es: \n", pila)
#Se imprime el elemento mínimo de la pila
print("\nEl elemento mínimo de la pila es: \n", pila.min())



