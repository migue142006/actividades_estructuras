class Nodo:
    def _init_(self, dato):
        # Se guarda el dato que va en el nodo
        self.dato = dato
        # Puntero que apuntará al siguiente nodo 
        self.siguiente = None

class Circular:
    def _init_(self):
        # Puntero al primer nodo de la lista 
        self.primero = None 
        self.cont = 0 # Contador de elementos para mostrar o recorrer
    
    def agregar(self, dato): # Método para agregar un nuevo nodo al final de la lista

        nuevo = Nodo(dato)
        if not self.primero: # Si la lista está vacía (no hay primer nod)
            
            self.primero = nuevo # El nuevo nodo pasa a ser el primero
           
            nuevo.siguiente = self.primero  # Y el nodo siguiente apunta a sí mismo (forma el círculo)

        else:         # Si ya existen nodos en la lista
            
            actual = self.primero
            # Recorremos la lista hasta encontrar el último nodo
            while actual.siguiente != self.primero:
                actual = actual.siguiente
                
                self.cont += 1 # Incrementamos el contador al recorrer cada nodo
           
            actual.siguiente = nuevo  # Una vez en el último nodo, lo conectamos con el nuevo
            
            nuevo.siguiente = self.primero # Y el nuevo nodo apunta al primero
           
            self.cont += 1  # Aumentamos el contador total de nodos
  
    def mostrar(self):   # metodo que muestra la lista
        actual = self.primero
        i = 0
  
        while actual and i < self.cont:       # Recorremos los nodos mientras no hayamos pasado por todos
            # Mostramos el dato del nodo actual
            print(actual.dato)
            # Avanzamos al siguiente nodo
            actual = actual.siguiente
            i += 1

k = Circular()

k.agregar(12)
k.agregar(9)
k.agregar(88)
k.agregar(8800)
k.agregar(9988)
k.mostrar()
