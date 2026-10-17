from animal import Animal


luna = Animal("Luna", "Gato", 3)
rocky = Animal("Rocky", "Perro", 5)
kiwi = Animal("Kiwi", "Loro", 2)

luna.presentarse()
rocky.presentarse()
kiwi.presentarse()

luna.jugar()
luna.comer(150)
luna.dormir()

rocky.jugar()
rocky.jugar()
rocky.jugar()
rocky.comer(300)

kiwi.comer(100)
kiwi.dormir()

print(f"\n{luna.nombre}: energía {luna.energia}")
print(f"{rocky.nombre}: energía {rocky.energia}")
print(f"{kiwi.nombre}: energía {kiwi.energia}")
