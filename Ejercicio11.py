Cantidad = input("cuando dinero quieres ingresar: ")
interes = 0.04
Incremento1= float(Cantidad)* float(1+interes)
Incremento2 = float(Incremento1)*float(1+interes)
Incremento3 =float(Incremento2)*float(1+interes)
print("Tu dinero el primer año con el intereses mejorar en: ",round(Incremento1,2))
print("Tu dinero el segundo año con el intereses mejorar en: ",round(Incremento2,2))
print("Tu dinero el tercer año con el intereses mejorar en: ",round(Incremento3,2))