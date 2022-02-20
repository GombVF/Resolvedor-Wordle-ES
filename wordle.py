#Santiago Villegas Fernando.

c=""
letras={'a':12.53,'b':1.42,'c':4.68,'d':5.86,'e':13.68,'f':0.69,'g':1.01,'h':0.70,'i':6.25,
    'j':0.44,'k':0.02,'l':4.97,'m':3.15,'n':6.71,'ñ':0.31,'o':8.68,'p':2.51,'q':0.88,
    'r':6.87,'s':7.98,'t':4.63,'u':3.93,'v':0.90,'w':0.01,'x':0.22,'y':0.90,'z':0.52}

def maxPalabra(arreglo):
    maxfreq=0
    maxletr=0
    p=""
    for x in arreglo:
        numletras=len(set(x))
        if(numletras>maxletr):
            maxletr=numletras
    for x in arreglo:
        if(len(set(x))==maxletr):
            suma=letras.get(x[0],0.0)+letras.get(x[1],0.0)+letras.get(x[2],0.0)+letras.get(x[3],0.0)+letras.get(x[4],0.0)
            if (suma>maxfreq):
                maxfreq=suma
                p=x
        elif(len(set(x))==maxletr):
            suma=letras.get(x[0],0.0)+letras.get(x[1],0.0)+letras.get(x[2],0.0)+letras.get(x[3],0.0)+letras.get(x[4],0.0)
            if (suma>maxfreq):
                maxfreq=suma
                p=x
        elif(len(set(x))==maxletr):
            suma=letras.get(x[0],0.0)+letras.get(x[1],0.0)+letras.get(x[2],0.0)+letras.get(x[3],0.0)+letras.get(x[4],0.0)
            if (suma>maxfreq):
                maxfreq=suma
                p=x
        elif(len(set(x))==maxletr):
            suma=letras.get(x[0],0.0)+letras.get(x[1],0.0)+letras.get(x[2],0.0)+letras.get(x[3],0.0)+letras.get(x[4],0.0)
            if (suma>maxfreq):
                maxfreq=suma
                p=x
    return p


wds=[]
i=1
print("Introducir el resultado de Wordle.\nSi se obtuvieron letras correctas pero no en el lugar correcto ingresarlas en mayúsculas.")
print("Si se obtuvieron letras correctas en el lugar correcto ingresarlas en minúsculas.")
print("Si no se obtuvo nada, ingresar puntos por cada letra.")
print("Ejemplo: Si la palabra que te da el resolvedor es avion")
print("La respuesta puede ser A..o.")
print("Lo que significa que la A no va en esa posición pero la o si va en esa posición.")
print("Si no se sigue este orden podría fallar.")
while True:
    if(c==""):
        with open("wddb.txt","r",encoding="utf-8") as f:
            for x in f:
                if("\n" in x):
                    x=x[0:len(x)-1]
                if x not in wds:
                    wds.append(x)
    else:
        continua=True
        opciones=[]
        for x in wds:
            for l in set(mp)-set(c.lower()):
                if l not in x:
                    continua=True
                else:
                    continua=False
                    break
            if continua:
                continua=True
                for l in range(len(c)):                
                    if (c[l]!="."):
                        if(c[l].isupper() and c[l].lower() in x and c[l].lower() not in x[l]):
                            continua=True
                        elif(c[l].islower() and c[l] in x[l]):
                            continua=True
                        else:
                            continua= False
                            break
                if continua:
                    opciones.append(x)
        wds=opciones        

    mp=maxPalabra(wds)
    print("ingresar la siguiente palabra: "+str(mp))

    while True:
        print("INTENTO NÚMERO: "+str(i))
        c=input()
        if(len(c)!=5):
            print("Tiene que haber 5 caracteres la respuesta")
        else:
            break
    #verifica si terminamos el juego
    if(c.islower() and "." not in c):
        break
    i=i+1