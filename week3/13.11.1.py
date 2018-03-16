lista = []
with open("13.11.1.input.txt", "r") as input:
    for line in input:
        lista.append(line)

with open("13.11.1.output.txt", "w") as output:
    last = len(lista) - 1
    for i in range(len(lista)):
        output.write(lista[last - i])
