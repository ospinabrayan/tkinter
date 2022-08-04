import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print('Es hora de ir a casa ')
else:
    print(f"que dan {18-int(hora)} horas y {59-int(minutos)} minutos para ir a casa")