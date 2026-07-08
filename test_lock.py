# from redis_lock import RedisLock

# lock = RedisLock("inventory_lock")

# print("Lock Name :", lock.lock_name)

# print("Owner ID  :", lock.owner_id)

# print("Timeout   :", lock.timeout)





# from redis_lock import RedisLock

# lock = RedisLock("inventory_lock")

# if lock.acquire():
#     print("Lock acquired successfully!")
# else:
#     print("Failed to acquire lock.")




# from redis_lock import RedisLock
# import time

# lock = RedisLock("inventory_lock")

# if lock.acquire():
#     print("Lock acquired successfully!")
#     print("Sleeping for 20 seconds...")
#     time.sleep(20)
# else:
#     print("Failed to acquire lock.")




from redis_lock import RedisLock
import time

lock = RedisLock("inventory_lock")

if lock.acquire():
    print("Lock acquired!")

    time.sleep(5)

    if lock.release():
        print("Lock released!")
    else:
        print("Failed to release lock.")
else:
    print("Could not acquire lock.")