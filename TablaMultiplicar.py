## Ingresa el número con el que se realizarán las operaciones de la tabla
## convierte el string en entero y detiene el programa si no encuentra un entero positivo

t = -1
while t < 0:
    tabla = input("¿Que número desea multiplicar?")
    try:
        t = int(tabla)
        if t <0:
            print("Favor de ingresar un número entero positivo")
    except:
        print("Favor de ingresar un número entero positivo")


## Ingresa donde se iniciará la tabla de multiplicar
## convierte el string en entero y detiene el programa si no encuentra un entero positivo

s = -1
while s < 0:
    start = input("¿Desde donde desea que inicie la tabla?")
    try:
        s = int(start)
        if s <0:
            print("Favor de ingresar un número entero positivo")
    except:
        print("Favor de ingresar un número entero positivo")
## Ingresa donde se terminará la tabla de multiplicar
## convierte el string en entero y detiene el programa si no encuentra un entero positivo

e = -1

while e <s:
    end = input("¿Hasta donde desea que termine la tabla?")
    try:
        e = int(end)
        if e < s:
            print("Favor de ingresar un número entero positivo")
    except:
        print("Favor de ingresar un número entero mayor al inicio")

## Generación de un contador sencillo que imprime las tablas de acuerdo a las entradas anteriores
while s <= e:
    print(tabla," * ", s, " = ", t*s)
    s += 1
