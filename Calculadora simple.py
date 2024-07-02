import math as m

resultado = 0
while True:
    operacion = input("Ingrese la operacion a realizar, tenga en cuenta que la divison entre 0 no es posible:\n")
    long = len(operacion)
    if long < 4:
        if '+' in operacion:
            sumar = operacion.split('+')
            suma = [float(suma1) for suma1 in sumar]
            resultado = sum(suma)
            print(resultado)

        if '-' in operacion:
            restar = operacion.split('-')
            resta = [float(resta1) for resta1 in restar]
            resultado = -sum(resta)
            print(resultado)

        if '*' in operacion:
            producto = operacion.split('*')
            mulit = [float(multi1) for multi1 in producto]
            resultado = m.prod(mulit)
            print(resultado)

        if '/' in operacion:
            dividir = operacion.split('/')
            for i in dividir:
                resultado /= i
            print(resultado)
    else:
        print("Ingrese de esta manera (num1 'el operando a utilizar' num2) sin espacios")

