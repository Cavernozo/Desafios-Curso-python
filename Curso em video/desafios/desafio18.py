import math
ang = int(input('Angulo!: '))
rad = math.radians(ang)
seno = math.sin(rad)
coseno = math.cos(rad)
tangente = math.tan(rad)
print('com o angulo {:.2f} temos o seno {:.2f}, coseno {:.2f}, tangente {:.2f}' .format(ang, seno, coseno, tangente))