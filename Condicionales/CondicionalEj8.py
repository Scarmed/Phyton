puntuacion = float(input("dime la puntacion que obtuviste: "))
if puntuacion == 0.0 or puntuacion < 0.4:
    print("Tu puntacion es completamente inaceptable, no obtendras ningun beneficio monetario")
elif puntuacion == 0.4 or puntuacion < 0.6:
    dinero = int(2400)
    total = puntuacion * dinero
    print("Tu puntacion es promedia y recibiras un extra de: ",total)
elif puntuacion >= 0.6:
    dinero = int(2400)
    total = puntuacion * dinero 
    print("Tu puntacion es todo un merito y recibiras un extra de: ",total)