#FUNCIÓN LA CUAL NOS RETORNA EL NÚMERO DE VECES QUE SE REPITE UN CARACTER.
def contar(x,y):
    i = 0
    contador=0
    while i<len(x):
        if x[i]==y:
            contador+=1
        i+=1
    return contador
#FUNCIÓN LA CUAL NOS DEVUELVE LA POSICIÓN DE UN CARACTER.
def buscar(x,y):
    i=0
    while i<=len(x):
        if x[i:i+len(y)]==y:
            return i
        i+=1
    return -1

frase_encrip = input()
frase_desencriptada = ""
letra_buscada = 0
seguir_principal = True
seguir = True
contador = 0
while seguir_principal == True:    
    while seguir == True:
        
        espacios = buscar(frase_encrip," ") 
        if espacios == -1:
            seguir_principal = False
            espacios = len(frase_encrip)
        palabra = frase_encrip[:espacios] #Hoola
        for i in palabra:
            repeticion = contar(palabra,i)
            if repeticion == 2:
                letra_buscada = i
                contador +=1
        if contador == 0:
            letra_buscada = palabra[-1]
            contador = 0
        frase_desencriptada += letra_buscada
        seguir = False
        contador = 0
    seguir = True
    frase_encrip = frase_encrip[espacios+1:]
print(frase_desencriptada)