# %%
import requests as rq
import json


# %%
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

ret = rq.get(url)

# %%
if ret:  # se o retorno for 200
    print(ret.json())  # retorna o json do arq
else:  # senao
    print(f'erro {ret}')  # mostre o cod do erro

# %%
retorno = json.loads(ret.text)  # guardar todos os dados em um objeto como json
print(f"\n\n{retorno['USDBRL']['bid']}")  # imprimir so o necessario


# %%
# lendo arquivo como json direto do requests, capturando dado necessario direto
r2 = json.loads(ret.text)['USDBRL']['bid']
print(r2)
# %%
