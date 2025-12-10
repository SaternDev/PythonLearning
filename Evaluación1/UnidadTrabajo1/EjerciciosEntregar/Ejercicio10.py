#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

calificacionPractica1 = float(input('Cual a sido tu calificación en la primera práctica '))
calificacionPractica2 = float(input('Cual a sido tu calificación en la segunda práctica '))
calificacionPractica3 = float(input('Cual a sido tu calificación en la tercera práctica '))

notaExamenFin = float(input('Cual ha sido tu nota final en el examen? '))

notaTrabajoFin = float(input('Cual ha  sido tu nota final en el trabajo? '))

notaPromedioPractica = (calificacionPractica1 + calificacionPractica2 + calificacionPractica3) / 3
notaFinal = ((notaPromedioPractica * 0.55) + (notaExamenFin * 0.3) + (notaTrabajoFin * 0.15))

print(f'Tu nota final es: {round(notaFinal, 2)}')