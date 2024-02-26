'''
    neste algoritmo, eu transformei o algoritmo anterior em uma funcao
    passei os paramentros da moeda e valor para ver quanto vale convertido
    gerei tratativas de erros imprimindo qual o erro gerado 
'''


# %%
import requests
import json


# transformar o cod anterior em funcao para cotar moedas


# %%
# a funcao cotacao captura todos os dados e depois retorna somente o dado necessário
def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    arq = ret.json()

    v = float(arq[moeda.replace('-', '')]['bid'])
    final = v * valor
    print(f"{valor} {moeda[:3]} hoje custam {final:.2f} {moeda[-3:]}")


cotacao(2, 'USD-BRL')

# %%


def cotar(valor, moeda):
    # a funcao cotar captura somente o dado necessario direto com json.loads()
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    bid = float(json.loads(ret.text)[moeda.replace('-', '')]['bid'])
    print(f"{(bid * valor):.2f}")


# %%
cotar(2, 'USD-BRL')

# TRATATIVAS DE ERRO

# tratativa com try imprimindo erro específico
# %%
try:
    cotacao(2, 'USD-BRL')
except Exception as e:
    print('Erro: ', e)  # imprimir erro ocorrido
else:
    print('nenhum erro ocorreu')
# %%

# ilustrando a tratativa de erro acima
# %%
try:
    10/0  # ocorrerá o erro de divisao por zero
except Exception as e:
    print(e)  # imprimir o erro
else:
    print('nenhum erro ocorrido')
# %%
