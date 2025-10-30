from Bateria import bateria
from Celular import celular
from DiscoDuro import discoDuro
from Laptop import laptop

l1 = laptop(micro="core i5", ram=120, DiscoDuro="SSD", Bateria=bateria("100mA", "hierro"))
l2 = laptop(micro="quad 4", ram=120, Bateria=bateria("100mA", "hierro"))
l3 = laptop(ram=50, DiscoDuro="HDD", Bateria=bateria("100mA", "hierro"))

c1 = celular(marca="Infinix", modelo="hot i5", amp="250mA", material="platino")
c2 = celular(marca="Techno", modelo="poco 1", amp="400mA"   )

print("celulares\n----------------------------------------")
print(l1)
print(l2)
print(l3)
print("----------------------------------------")
print("laptops\n-------------------------------------------------------------------")
print(c1)
print(c2)
print("-------------------------------------------------------------------")