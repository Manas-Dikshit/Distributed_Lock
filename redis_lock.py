import uuid

from config import redis_client


class RedisLock:

    def __init__(self, lock_name, timeout=10000):

        self.lock_name = lock_name

        self.timeout = timeout

        self.owner_id = str(uuid.uuid4())

        self.redis = redis_client