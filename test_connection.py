from config import redis_client

print("Connecting to Redis...")

print(redis_client.ping())