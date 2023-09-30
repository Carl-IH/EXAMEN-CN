def primo_test(valor):
    if valor <= 1:
        return False #ELIMINA TODOS LOS VALORES QUE SEAN NEGATIVOS Y/O MENORES A 1
    elif valor <= 3:
        return True
    elif valor % 2 == 0 or valor % 3 == 0:
        return False #SI EL VALOR SE PUEDE DIVIDIR SOBRE 2 O 3 SE ELIMINA
    i = 5
    while i * i <= valor:
        #print(i)
        if valor % i == 0 or valor % (i + 2) == 0:
            return False
        i += 6
    return True


def nextPrime(valor):
    primo_test(valor)
    valor +=1
    while True:
        if primo_test(valor):
            return valor
        valor += 1


def median(valores):
    valoresOrden = sorted(valores, reverse=True)
    #print(valoresOrden)
    print('La mediana de tus valores es ', valoresOrden[1])
    

def randomPasword():
    import random
    size = random.randint(7,10)
    password = []
    for _ in range(size):
        dato = chr(random.randint(33,126))
        password.append(dato)

    contrasena = ''.join(password)
    print('tu contraseña de ', size, ' digitos es: ',contrasena)


def hipo(a,b):
    from math import sqrt as raiz
    raizContenido = (a*a) + (b*b)
    c = raiz(raizContenido)
    print('la hipotenusa del triángulo es ',c,'u{}'.format(chr(178)))
