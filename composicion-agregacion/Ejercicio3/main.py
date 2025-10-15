from Bateria import bateria
from Celular import celular
from DiscoDuro import discoDuro
from Laptop import laptop

l1 = laptop(micro="core i5", ram=120, DiscoDuro="SSD", Bateria=bateria("100mA", "hierro"))
l2 = laptop(micro="quad 4", ram=120, DiscoDuro=None, Bateria=bateria("100mA", "hierro"))
l3 = laptop(micro=None, ram=50, DiscoDuro="HDD", Bateria=bateria("100mA", "hierro"))

c1 = celular(marca="Infinix", modelo="hot i5", Bateria=bateria("250mA", "aluminio"))
c2 = celular(marca="Tecno", modelo=None, Bateria=bateria("200mA", "oro"))

print(l1)
print(l2)
print(l3)