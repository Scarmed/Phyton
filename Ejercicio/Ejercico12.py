PanDia = 3.49
PanNoDia = float(PanDia)*0.4
BarrasVendidasNoDia = input("Cuantas barras de hace dias se vendieron: ")
TotalVendidoNoDia = PanNoDia * int(BarrasVendidasNoDia)
print("El precio de las barras de hoy es: ",PanDia,"pero el de ayer tiene un descuento del 60% quedando con un costo de:",PanNoDia,"y se vendio un total de pan del dia de ayer",round(TotalVendidoNoDia,2))