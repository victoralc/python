cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)

salario = float(input("Salario? "))
imposto = 27.
while imposto > 0:
    imposto = input('Imposto ou (s) para sair')
    if not imposto:
        imposto = 27.
    elif imposto == 's':
        break
    else:
        imposto = float(imposto)
        print("Valor real: {0}".format(salario - (salario * imposto * 0.01)))
