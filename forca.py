import os
import requests
import json
from deep_translator import GoogleTranslator


os.system('cls')
palavra_requisao = requests.get("https://random-word-api.herokuapp.com/word")
palavraalea = json.loads(palavra_requisao.text)

traduz = str(palavraalea[0])
letras = []
chances = 7
win = False
errada = []

tradutor = GoogleTranslator(source='en', target='pt')

palavra = tradutor.translate(traduz)

while True:
    # validar a letra ta dentro da palavra
    for i in palavra: # examina as letras dentro da palavra
        if i.lower() in letras: # se tem a letra na lista letras[]
            print(i, end=' ')
        else:
            print('_', end=' ')
    print(f'|-- Você tem {chances} chances --|')
    
    # mostra as letras erradas para o usuário
    print('Letras erradas:', *errada)
    
    # vai pegar a letra que o usuário digitar
    tentativa = input('Digite uma letra: ').lower()
    letras.append(tentativa)
    
    # coloca as letras erradas dentro da variavel errada[]
    if tentativa not in palavra:
        errada.append(tentativa)
    
    # validar se o usuário ganhou
    win = True
    for i in palavra:
        if i not in letras:
            win = False
    
    # ver se não esta dentro da palavra, se sim, tira uma chance
    if tentativa not in palavra:
        chances -= 1   
        
    # verifica se as chances são 0 ou se a variável win for igual a true
    if chances == 0 or win:
        print('')
        break
    os.system('cls')
        
        
if win: 
    print(f'Parabéns, você ganhou, a palavra era: {palavra}')
    print('')
else:
    print(f'Você pardeu!!! A palavra era: {palavra}')
    print('')
    
    


