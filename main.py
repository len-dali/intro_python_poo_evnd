def suma():
    num1 = float(input("Ingrese el primer numero para sumar: "))
    num2 = float(input("Ingrese el segundo numero para sumar: "))
    return num1 + num2

def resta():
    num1 = float(input("Ingrese el primer numero para restar: "))
    num2 = float(input("Ingrese el segundo numero para restar: "))
    return num1 - num2

print("Hello Worl!")
print("Hola de nuevo, Mundo!")

resultado_suma = suma()
print(f"El resultado de la suma de los dos numeros es: {resultado_suma}")

resultado_suma = resta()
print(f"El resultado de la resta de los dos numeros es: {resultado_resta}")

