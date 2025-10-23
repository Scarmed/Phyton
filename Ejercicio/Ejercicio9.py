capital= input('dime cuanto dinero quieres inventir: ')
tasa = input('Dime cuantos intereses hay actualmente para calcular las ganancias: ')
tiempo = input('Dime cuanto tiempo va a pasar desde esta transaccion: ')
porcentaje = capital*tasa/100
intereses = int(capital)*int(tiempo)*porcentaje
print("Las ganacias son: ", intereses)
