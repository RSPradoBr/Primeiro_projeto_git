print("\nEm Python, a letra i é muito usada como variável de controle em laços de repetição, especialmente em for, mas não possui significado especial por si só. É apenas uma convenção adotada pelos programadores.")


for i in range(3):
    for j in range(3):
        print(i, j)

print("\n===Indice combinado numeros sequenciais e variaveis L8===")

lista = ["A", "B", "C"]
#quando usamos [] os dados que estão dentro já são os dados armazenadosfor i in range(len(lista)):
for i in range(len(lista)):
    print(i, lista[i])
#A linha acima pode ser traduzida como: printe a posição "i" "," combinando com o valor "lista" com [i] a posição que
#está sendo percorrida no momento.
print("\n===Usando i como índice L16===")

nomes = ["Ana", "Carlos", "Maria"]

for i in range(len(nomes)):
    print(i, nomes[i])

print("\nlen(lista): retorna o quantidade de elementos da lista.range(n): gera números de 0 até n-1.")

print("\n===Enumerando índice e valor ao mesmo tempo L25===")

nomes = ["Ana", "Carlos", "Maria"]

for i, nome in enumerate(nomes):
    print(i, nome)

print("\nenumerate(lista): retorna simultaneamente índice e valor.")

print("\n===Somando valores da lista L34===")

valores = [10, 20, 30]

soma = 0
#se alteral o valor inicial da variável soma, o resultado final será diferente.
for valor in valores:
    soma = soma + valor
#a linha acima também poderia ser escrita como: soma += valor

print(soma)

print("\n======================================")