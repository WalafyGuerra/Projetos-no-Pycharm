texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#exemplo usando um iterável
for letra  in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()    #adicione uma quebra de linha

#exemplo usando a funçao built-in range
for número in range(0,9):
    print(número, end= "")