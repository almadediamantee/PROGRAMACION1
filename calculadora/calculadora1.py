def menuInicial():
    menu = '''
    ******************
    *     1-SUMA       *     
    *     2-RESTA      *
    *     3-MULTI      *
    *     4-DIVI       *
    *     5-SALIR      *
    ******************
    '''
    print(menu)
    opciones = int(input("ingrese la opcion deseada: "))
    return(opciones)

def suma(a,b):
    return(a+b)

def resta(a,b):
    return(a-b)

def multi(a,b):
    return(a*b)

def divi(a,b):


    if b == 0:
        b = int(input("No se puede dividir por cero, ingrese otro numero: "))
    else:
        return(a/b)
    def suma(a,b):
        return(a+b)

def resta(a,b):
    return(a-b)

def multi(a,b):
    return(a*b)

def divi(a,b):

    if b == 0:
        b = int(input("No se puede dividir por cero, ingrese otro numero: "))
    else:
        return(a/b)
