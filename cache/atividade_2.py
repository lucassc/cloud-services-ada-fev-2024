import redis
import datetime
import requests


start = datetime.datetime.now()

ip = "34.117.186.192"
ttl= 180 #segundos


url = f'https://ipinfo.io/{ip}/geo'

cache_key = url

resultado = ""

redis_conn = redis.Redis(host='localhost', port=6379, db=0)

valor_em_cache = redis_conn.get(cache_key)

if (valor_em_cache == None):
    response = requests.request("GET", url)

    if (response.status_code == 200):
        print(f"Valor recuperado da API")
        redis_conn.setex(cache_key, ttl, response.text)
        resultado = response.text
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        resultado = "Não foi recuperar/consultar o valor"
else:
    print("Valor em cache")
    resultado = valor_em_cache.decode("utf-8")


print(f'Resultado do script: {resultado}')
print(f'Tempo de execução: {datetime.datetime.now() - start}')