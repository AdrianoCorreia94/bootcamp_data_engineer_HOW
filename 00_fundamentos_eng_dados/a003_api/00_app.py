# %%
import requests as rq
import json


# %%
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

ret = rq.get(url).json()

# %%
if ret:  # se o retorno for 200
    print(ret)  # retorna o json do arq
else:  # senao
    print(f'erro {ret}')  # mostre o cod do erro

# %%
print(f"\n\n{ret['USDBRL']['bid']}")  # imprimir so o necessario


# %%
# lendo arquivo como json direto do requests, capturando dado necessario direto
r2 = ret['USDBRL']['bid']
print(r2)
# %%
