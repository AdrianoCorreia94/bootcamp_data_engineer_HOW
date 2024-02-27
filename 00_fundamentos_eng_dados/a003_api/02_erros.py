import requests
import json


lista_moedas = [
    'USD-BRL',
    'EUR-BRL',
    'ERR-BRL',
    'BTC-BRL',
    'JPY-BRL'
]


def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url).json()
    bid = float(ret[moeda.replace('-', '')]['bid'])
    print(f"{valor} {moeda[:3]} hoje custam {(bid * valor):.2f} {moeda[-3:]}")


# for moeda in lista_moedas:
#    cotacao(10, moeda)
'''
    se executar na forma acima, na moeda que houver erro 
    o programa encerrara sem ir para a proxima,
    ou seja ira encerrar na terceira moeda

    para que o programa execute todas mesmo havendo erro
    devemos fazer conforme abaixo:

    tirar o tratamento do loop e inseri-lo na funcao
    ou tratar dentro do for a cada moeda iterada
'''


def cotar(valor, moeda):
    try:  # tratar dentro da funcao
        url = f'https://economia.awesomeapi.com.br/last/{moeda}'
        ret = requests.get(url).json()
        bid = float(ret[moeda.replace('-', '')]['bid'])
        print(
            f"{valor} {moeda[:3]} hoje custam {(bid * valor):.2f} {moeda[-3:]}")
    except Exception as e:
        print(f'Erro ao buscar moeda {e}')
        pass
    else:
        pass


for moeda in lista_moedas:
    cotar(10, moeda)


def c2(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url).json()
    bid = float(ret[moeda.replace('-', '')]['bid'])
    print(
        f"{valor} {moeda[:3]} hoje custam {(bid * valor):.2f} {moeda[-3:]}")


print('\nnovo teste\n')

for moeda in lista_moedas:
    try:  # tratar a cada moeda iterada
        c2(10, moeda)
    except Exception as e:
        print(f'Erro ao buscar moeda {e}')
    else:
        pass
