# Example of how to use Kafka with Python

1. Start the Kafka server

```bash
docker-compose up -d
```

2. Install the dependencies

```bash
pip install kafka-python
```

3. Run the producer

```bash
python producer.py
```

4. Run the consumer

```bash
python consumer.py
```
