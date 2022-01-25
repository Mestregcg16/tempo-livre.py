import os
import time

import colorama
from colorama import Fore
import time
colorama.init(autoreset=True)

"""
Caso a "função" usada pra limpar a tela do terminal não funcionar é so pesquisar outro metodo
"""

# Variaveis
porcentagem = 0
erros = 0
# Perguntas e respostas
perguntas = {
    'pergunta 1': {
        'pergunta': 'Quantos anos tinha o Luffy quando começou sua jornada?',
        'respostas': {'a': '14', 'b': '19', 'c': '17'},
        'rsp_certa': 'c',
    },

    'pergunta 2': {
        'pergunta': 'Qual primeiro tripulante quando Luffy iniciou sua jornada?',
        'respostas': {'a': 'ussop', 'b': 'zoro', 'c': 'nami'},
        'rsp_certa': 'b',
    },

    'pergunta 3': {
        'pergunta': 'Qual o nome do pai de Luffy?',
        'respostas': {'a': 'garp', 'b': 'kaido', 'c': 'dragon', 'd': 'Gold D. rogger'},
        'rsp_certa': 'c',
    },
    'pergunta 4': {
        'pergunta': 'De qual divisão Ace era comandante?',
        'respostas': {'a': '2° divisão', 'b': '4° divisão', 'c': '1° divisão'},
        'rsp_certa': 'a',
    },

    'pergunta 5': {
        'pergunta': 'Qual comida a preferida de Luffy?',
        'respostas': {'a': 'sopa', 'b': 'bolinhos de arroz', 'c': 'carne', 'd': 'doce'},
        'rsp_certa': 'c',
    },

    'pergunta 6': {
        'pergunta': 'Qual o nome do segundo irmão de Luffy?',
        'respostas': {'a': 'coby', 'b': 'sabo', 'c': 'zefy', 'd': 'bug'},
        'rsp_certa': 'b',
    },
}


# Tela de inicio
class inicio():
    print(f"{Fore.YELLOW}#" * 20)
    print(f"{Fore.YELLOW}#", f'{Fore.CYAN} Resposta Certa ', f"{Fore.YELLOW}#")
    print(f"{Fore.YELLOW}#" * 20)
    print()
    time.sleep(1)


# Interação das perguntas e do input do usuario
# O interavel ps é nulo

for ps, rs in perguntas.items():

    if porcentagem and erros == '0':
        inicio()

    print(f'{rs["pergunta"]}')

    print('Respostas: ')
    for ps, rv in rs['respostas'].items():
        print(f'[{ps}] | {rv}')

    resp = input(f'{Fore.CYAN}Sua resposta: ').upper()
    time.sleep(1)
    os.system("clear")

    if resp == rs['rsp_certa'].upper():
        print(f'{Fore.GREEN}heheh vc acertou...')
        porcentagem += 1
    else:
        print(f'{Fore.RED}Voce errou')
        erros += 1

total_perguntas = len(perguntas)
porcentagem_resut = porcentagem / total_perguntas * 100
print(f'Você acertou: {porcentagem} | Você errou: {erros}')
print(f'Sue aproveitamento foi de {porcentagem_resut:.0f}%')
# Resultado final
