import random
import time

print("Bem-vindo ao jogo de Matematica")
print("Responda o maximo que puder. Digite 'sair' parar encerrar.\n")

pontos = 0 
rodada = 1 

while True:
    # Gerará doi números e uma operação aleatória
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    operacao = random.choice(["+","-","*"])

    #Calculando o resultado certo 
    if operacao =="+":
        resultado_certo = n1 + n2
    elif operacao == "-":
        resultado_certo == n1 - n2 
    else:
        resultado_certo = n1 * n2

        print(f"pergunta {rodada}: Quanto é {n1} {operador} {n2}?")
        resposta = input("->")
        
        if