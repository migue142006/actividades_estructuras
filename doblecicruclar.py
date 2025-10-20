class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

        self.anterior = None         # Referencia al nodo anterior 

class ListaDoble:
    def __init__(self):
        self.cabeza = None          # puntero al primer nodo de la lista
        self.cola = None         # puntero al último nodo de la lista

        self.cont = 0        # Contador de nodos 


    def agregar(self, dato):
        nuevo = NodoDoble(dato)   # Crea un nuevo nodo con el dato recibido

        # Si la lista está vacía (no hay cabeza)
        if not self.cabeza:
            # El nuevo nodo pasa a ser la cabeza
            self.cabeza = nuevo
            # Y también la cola este seria el unico nodo
            self.cola = nuevo
        else:
            # Si ya hay elementos, enlazamos el último con el nuevo
            # El siguiente de la cola actual será el nuevo nodo
            self.cola.siguiente = nuevo
            # El nuevo nodo apunta hacia atrás a la cola anterior
            nuevo.anterior = self.cola
            # Actualizamos la cola para que sea el nuevo nodo agregado
            self.cola = nuevo

        # para mantener la circularidad el siguiente de la cola apunta a la cabeza
        self.cola.siguiente = self.cabeza
        # observamos la circularidad, la anterior de la cabeza apunta a la cola
        self.cabeza.anterior = self.cola
        self.cont += 1  # Incrementa el contador de nodos porque se agregó uno nuevo

    def adelante(self):
        actual = self.cabeza
        i = 0
        # Recorremos mientras exista nodo y no hayamos mostrado todos (evita bucle infinito)
        while actual and i < self.cont:
            print(actual.dato)
            actual = actual.siguiente # Avanza al siguiente nodo

            i += 1

    def atras(self):
        # Comenzamos a recorrer desde la cola 
        actual = self.cola
        i = 0
        # Recorremos mientras exista nodo y no hayamos mostrado todos (evita bucle infinito)
        while actual and i < self.cont:
            print(actual.dato)
           
            actual = actual.anterior  # Retrocede al nodo anterior
            i += 1       # Incrementa el índice del recorrido



l1 = ListaDoble()
l1.agregar(456)
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

l1.adelante()         
print("=" * 50)
l1.atras()
