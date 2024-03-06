# Cache


## Redis com IU

```BASH
docker run -it --rm --name redis -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

[Acessar Interface](http://localhost:8001)

## Redis open source

```BASH
docker run -it --rm --name redis -p 6379:6379 redis
```

## Acessar redis-cli 

```BASH
docker exec -it redis redis-cli
```

## MemCached

[Acesse aqui](./memCached.md)


## Atividade 06 Mar 2024

[Acesse aqui](./atividade_06_03_2024.md)

