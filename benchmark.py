import redis
import time
import random
import string

# Redis 연결
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def benchmark(set_length, iterations=1000):
    total_set_time = 0
    total_get_time = 0

    for i in range(iterations):
        key = f"key:{i}"
        value = random_string(set_length)

        # SET 시간 측정
        start = time.time()
        r.set(key, value)
        total_set_time += (time.time() - start)

        # GET 시간 측정
        start = time.time()
        r.get(key)
        total_get_time += (time.time() - start)

    avg_set_time = total_set_time / iterations
    avg_get_time = total_get_time / iterations
    print(f"Length: {set_length} chars → Avg SET: {avg_set_time:.6f}s, Avg GET: {avg_get_time:.6f}s")

# 테스트 케이스
benchmark(50)     # Case 1: 50 chars
benchmark(500)    # Case 2: 500 chars
benchmark(3000)   # Case 3: 3000 chars
