'''
    Autor : Matheus Yasuo Ribeiro Utino

    Trata-se de um programa que pega uma imagem e criar um histograma a partir dela, sendo um gráfico portanto da frequência de aparecimento de uma cor por sua intensidade.
    É bem útil no tratamento de imagem, assim como sua análise.
    Bons estudos para todos!!!
'''

#Importando as bibliotecas necessárias
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Lenna.jpg") #Lendo a imagem escolhida
color = ('b', 'g', 'r') #A cor é composta por três tipos ([azul/blue],[verde/green] e [vermelhor/red])

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256]) #Criando o histograma
    plt.plot(histr, color = col) #Plotando o histograma
    plt.xlim([0, 256]) #Definindo a intensidade
cv2.imshow("Imagem Original", img) #Exibindo a imagem
plt.show() #Exibindo o hisograma

cv2.waitKey(0)
cv2.destroyAllWindows()