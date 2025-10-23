edad = int(input("Dime tu edad chaval: "))
if(edad > 16 ):
    tributar = int(input("Dime cuanto tributas mensualmente "))
    if(tributar > 1000):
        print("perfecto puedes tributar en españita siempre que quieras")
    else:
        print("no tienes el dinero suficiente para que tengas que tributar")
else:
    print("Aun eres muy joven no deberias estar aqui.")