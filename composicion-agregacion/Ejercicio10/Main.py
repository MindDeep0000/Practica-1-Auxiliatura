from Evento import Evento
from herencia import Participante
from Charla import Charla

e = Evento("Coferencia para desarrollo de conocimiento de informatica")

p1 = Participante(nombre="Damian", apellido="Schasel", edad=21, ci=21324354, nroTicket=123)
p2 = Participante(nombre="Oscar", apellido="Urrutia", edad=23, ci=43641633, nroTicket=456)
p3 = Participante(nombre="Miguel", apellido="Arupanqui", edad=18, ci=12355362, nroTicket=351)
p4 = Participante(nombre="Maria", apellido="Prado fernanda", edad=25, ci=47294710, nroTicket=948)

ch1 = Charla(lugar="Edificio de las antillas", nmCharla="Inteligencia Artificial", nombre="Ben", apellido="Quiroz", edad=32, ci=55642789, esp="Aprendizaje automatico")
ch2 = Charla(lugar="Edificio de las antillas", nmCharla="Ciberseguridad", nombre="Linus", apellido="Torvals", edad=56, ci=34532412, esp="Programador desarrollador")

ch1.agregarParticipante(p1)
ch2.agregarParticipante(p2)

ch2.agregarParticipante(p3)
ch2.agregarParticipante(p4)

e.agregarCharla(ch1)
e.agregarCharla(ch2)

e.mostrarCharlas()

print(f"* * * \npromedio de edades en el evento {e.calcularProEdades()}")

e.existePersona("Damian", 21324354)
e.eliminarSpeaker(55642789)
e.mostrarCharlas()