# Exercício Python 21: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time 
contagem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for fogos in contagem: 
    time.sleep(1)
    print(fogos)

