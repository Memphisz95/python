import time

horaActual = time.localtime()
print('Hora actual: ' + str(horaActual.tm_hour) + ':' + str(horaActual.tm_min) + ':' + str(horaActual.tm_sec))

if horaActual.tm_hour >= 19:
    print('Es hora de ir a casa')
else:
    horaFin = time.strptime('18 59', '%H %M')
    horasRestantes = horaFin.tm_hour - horaActual.tm_hour
    minutosRestantes = horaFin.tm_min - horaActual.tm_min
    print('Quedan ' + str(horasRestantes) + ' horas y ' + str(minutosRestantes) + ' minutos para que sean las 19:00.')