numero = input('Dime el numero de empresa con el formato +XX-XXXXXXXXX-XX: ')
PartesNum = numero.split('-')
SinPrefijo = PartesNum[1]
print('El numero de telofono escrito es:',SinPrefijo)
