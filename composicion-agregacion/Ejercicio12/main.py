from Hospital import Hospital
from Doctor import Doctor

h1 = Hospital("Hospital de la sierra")
h2 = Hospital("Hospital de villa tunari")

d1 = Doctor("Dr. Antonio Berruezo Sánchez", "Arritmias Cardíacas")
d2 = Doctor("Pedro Cavadas", "cirujano plástico y referente en trasplantes de manos")
d3 = Doctor("Dr. César Canales Bedoya","cirugías de tiroides y biliopancreáticas")
d4 = Doctor("Dr. Gonzalo Aldámiz-Echevarría del Castillo", "jefe de Cirugía Cardíaca")
d5 = Doctor("Dra. Manuela Camino López", "líder en Trasplante Cardíaco Infantil")

h1.agregarDoctor(d1)
h1.agregarDoctor(d2)

h2.agregarDoctor(d3)
h2.agregarDoctor(d4)
h2.agregarDoctor(d5)

h1.mostrarDoctores()
h2.mostrarDoctores()
