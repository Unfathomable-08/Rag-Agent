import redis
import os

redis_client = redis.Redis.from_url(os.getenv("REDIS_URL"))

def get_chat_history(session_id):
    messages = redis_client.lrange(session_id, 0, -1)
    return [m.decode("utf-8") for m in messages]

def save_chat_message(session_id, message):
    redis_client.rpush(session_id, message)
    redis_client.expire(session_id, 86400)  # 24 hours