import sys
import six

if sys.version_info >= (3, 12, 0):
    sys.modules["kafka.vendor.six.moves"] = six.moves

from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers="localhost:9092", api_version=(0, 11, 5))

while True:
    print("Sending message to Kafka")
    producer.send("my_favorite_topic", b"Hello, Kafka!")
    time.sleep(1)
