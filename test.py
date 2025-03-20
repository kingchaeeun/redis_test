import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

session_id = 'user123'

r.rpush(f'session:{session_id}:context', '안녕하세요')
r.rpush(f'session:{session_id}:context', '오늘 날씨가 좋네요')
r.rpush(f'session:{session_id}:context', '내일 계획은 어떻게 되세요?')

context = r.lrange(f'session:{session_id}:context', 0, -1)
print("현재 세션 대화 히스토리:", context)
