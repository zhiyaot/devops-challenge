#!/usr/bin/env python
import os

from flask import Flask
from flask_redis import FlaskRedis
from redis.exceptions import ConnectionError

# Configure Flask + Redis
app = Flask(__name__)
app.config["REDIS_URL"] = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
redis_client = FlaskRedis(app)

# Determine if connected to Redis
try:
    redis_client.set("visitors", 0)
    redis_connected = True
except ConnectionError:
    redis_connected = False

# Routes
@app.route("/")
def index():
    if redis_connected:
        visitors = int(redis_client.get('visitors'))
        formatted_visitors = "1 visitor" if visitors == 1 else f"{visitors} visitors"
        redis_client.set("visitors", visitors + 1)
        return f"We have had: {formatted_visitors}"
    else:
        return "Not connected to redis"


if __name__ == "__main__":
    app.run()
