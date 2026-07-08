import uuid
from config import redis_client


class RedisLock:
    def __init__(self, lock_name, timeout=10000):
        self.lock_name = lock_name
        self.timeout = timeout
        self.owner_id = str(uuid.uuid4())
        self.redis = redis_client

    def acquire(self):
        acquired = self.redis.set(
            name=self.lock_name,
            value=self.owner_id,
            nx=True,   # Only set if not exists
            px=self.timeout  # Expire after timeout (ms)
        )
        return acquired is True

    def release(self):
        script = """
        if redis.call('GET', KEYS[1]) == ARGV[1] then
            return redis.call('DEL', KEYS[1])
        else
            return 0
        end
        """
        result = self.redis.eval(
            script,
            1,
            self.lock_name,
            self.owner_id
        )
        return result == 1
