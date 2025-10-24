edad =int(input("Dime tu edad: "))
if edad < 4:
    print("felicidades entras gratis")
elif edad == 4 or edad <= 18:
    print("Para entrar tienes que pagar 5 eurazos chaval")
elif edad > 18:
    print("Tienes que pagar 10 euros para poder entrar")
