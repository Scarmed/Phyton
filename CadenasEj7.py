correo = input('dime tu correo: ')
correo2 = correo.split('@')[0]
dominio = '@ceu.es'
NuevoCorreo = correo2 + dominio
print(NuevoCorreo)