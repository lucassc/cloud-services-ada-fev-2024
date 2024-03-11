from datetime import timedelta
from minio import Minio

minio_conn = Minio(
    endpoint="localhost:9000", 
    access_key="minioadmin", 
    secret_key="minioadmin",
    secure=False)

bucket_name = "meu-bucket"
bucket_exists = minio_conn.bucket_exists(bucket_name)
if bucket_exists:
    print(f"Bucket {bucket_name} já existe!")
else:
    minio_conn.make_bucket(bucket_name)
    print("Bucket criado com sucesso!")

nome_arquivo = "atividade_01_aula.py"

result = minio_conn.fput_object(
    bucket_name=bucket_name,
    object_name=nome_arquivo,
    file_path=nome_arquivo)

print(f"Versão do arquivo {nome_arquivo}: {result.version_id}")

get_url = minio_conn.get_presigned_url(
    method='GET',
    bucket_name=bucket_name,
    object_name= nome_arquivo, )

delete_url = minio_conn.get_presigned_url(
    method='DELETE',
    bucket_name=bucket_name,
    object_name= nome_arquivo, expires=120  )

print(f"Download URL: [GET]{get_url}")
print(f"Delete URL: [DELETE]{e_}")
