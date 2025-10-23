nombre = input("dime tu nombre: ")
sexo = input("Dime que genero eres: ")
if (sexo == "chico" and nombre < "N" or sexo == "mujer" and nombre < "N"):
    print("perteneces al grupo A")
else:
    print("pertences al grupo B ")