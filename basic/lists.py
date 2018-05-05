names = ["Victor", "Maria", "Joao", "Alcantara"]

print("Lenght: " + str(len(names)))
print("Ordered: " + str(sorted(names)))
names.append("Pedro")
print("Adicionando: " + str(names))
print(" & ".join(sorted(names)))
