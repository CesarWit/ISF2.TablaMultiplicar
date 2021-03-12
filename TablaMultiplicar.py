## Ingresa el número con el que se realizarán las operaciones de la tabla
## convierte el string en entero y detiene el programa si no encuentra un entero positivo
tabla = input("¿Que número desea multiplicar?")
try:
    t = int(tabla)
    if t <0:
        quit()
except:
    print("Favor de ingresar un número entero positivo")
    quit()

## Ingresa donde se iniciará la tabla de multiplicar
## convierte el string en entero y detiene el programa si no encuentra un entero positivo

start = input("¿Desde donde desea que inicie la tabla?")

try:
    s = int(start)
    if s <0:
        quit()
except:
    print("Favor de ingresar un número entero positivo")
    quit()
## Ingresa donde se terminará la tabla de multiplicar
## convierte el string en entero y detiene el programa si no encuentra un entero positivo

end = input("¿Hasta donde desea que termine la tabla?")

try:
    e = int(end)
    if e < s:
        quit()
except:
    print("Favor de ingresar un número entero mayor al inicio")
    quit()

## Generación de un contador sencillo que imprime las tablas de acuerdo a las entradas anteriores
while s <= e:
    print(tabla," * ", s, " = ", t*s)
    s += 1
