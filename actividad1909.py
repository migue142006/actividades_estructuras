n=int(input("Ingrese un numero: "))

def factorial(n):
    if n==0:
        resultado=1
    else:
        resultado=n*factorial(n-1)
    return resultado   
print(f"El factorial de {n} es {factorial(n)}")

numero=int(input("ingrese desde que numero desea sumar: "))

def acumulador(numero):
    if numero==0:
        total=0
    else:
        total=numero+acumulador(numero-1)
    return total
print(f"La suma acumulada desde {numero} hasta 0 es {acumulador(numero)}")

print("hola mundo prueba")

