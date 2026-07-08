from redis_lock import RedisLock

lock = RedisLock("inventory_lock")

print("Lock Name :", lock.lock_name)

print("Owner ID  :", lock.owner_id)

print("Timeout   :", lock.timeout)