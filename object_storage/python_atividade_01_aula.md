# Object Storage - Python

## MinIO

### Para rodar MinIO

```BASH
docker run  --name minio --rm -p 9000:9000 -p 9001:9001 quay.io/minio/minio server /data --console-address ":9001"
```
[Acesse UI aqui](http://localhost:9001)

### atividade_01_aula.py 

```BASH
pip install minio

python atividade_01_aula.py
```

### Links

- https://min.io/docs/minio/linux/developers/python/API.html
