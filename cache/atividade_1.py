import redis
import datetime

# Connect to Redis
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

now = datetime.datetime.now()

# Set a key
redis_conn.set("my-key", f'valor-do-cache {now}')
print("Cache created with key my-key")

# Get the value of a key
result = redis_conn.get("my-key")
# Print value
print(result)
