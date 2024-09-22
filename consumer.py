import sys
import six

if sys.version_info >= (3, 12, 0):
    sys.modules["kafka.vendor.six.moves"] = six.moves

from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

consumer = KafkaConsumer("my_favorite_topic", bootstrap_servers="localhost:9092", api_version=(0, 11, 5))

for msg in consumer:
    msg: ConsumerRecord

    data = msg.value.decode("utf-8")

    print(data)
