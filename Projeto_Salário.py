# Para formatar textos, existem duas opções interessantes:

hora_teravita = 50.00
hora_maria_clara = 43.00
horas_trabalhas_tv = int(input("Quantas horas você trabalhou na Teravita? "))
horas_trabalhadas_maria = int(input("Quantas horas você trabalhou na Maria? "))
valor_teravita = hora_teravita * horas_trabalhas_tv
valor_maria = hora_maria_clara * horas_trabalhadas_maria
valor_geral = valor_teravita + valor_maria

# OPÇÃO 1 (Mais código e concatenação)

#final = "Você fez " + str(valor_teravita) + " na Teravita e fez " + str(valor_maria) + " na Maria, totalizando: " + str(valor_geral)
# Aqui, tivemos que puxar "str" para que os valores pudessem sair em texto, do contrário, ele não leria.

#print(final)

#OPÇÃO 2 (+ intuitiva e +viável. DANDO "F" de format, concatenação mais "simples")

final = f"Você fez R${valor_teravita:,.2f} na Teravita e fez R${valor_maria:,.2f} na Maria, totalizando: R${valor_geral:,.2f}"

# Eu acrescentei o ":" para abrir o modo de formatação na variável
# Acrescentei a , para dizer que quero aquele número separado na casa de milhar
# Acrescentei o . para dizer que quero casas decimais
# o 2 para indicar que são duas casas decimais
# o "f" indicando float, já que eu optei por casas decimais

print(final)
