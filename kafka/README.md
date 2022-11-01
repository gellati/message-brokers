# Kafka

Files for setting up the Kafka streaming service. Sets up two Docker containers, Kafka and Zookeeper. Kafka is a message broker, and Zookeeper contains the metadata from Kafka's streams.

Start the containers with

    docker-compose up

If you want to rebuild the containers from zero

    docker-compose buld --no-cache

List all running containers with

    docker ps

Stop the containers with

```shell
docker-compose down
```

## Networks

Create the network used by the containers with

```shell
docker network create kafka-network
```

# Configuration files

Kafka is configured with the server.properties file located in `config`, and Zookeeper is configured with the file `zoo.cfg` in `conf`.

For communication between the containers, the `kafka-network` network is used.

Kafka uses the following ports:

|Number  | Purpose |
|--------|---------|
|9092    | Communication between services in containers |
|9093    | Communication on localhost |


# Libraries
The services use the Kafka and Zookeepr libraries.

Kafka can be downloaded with
```shell
wget https://downloads.apache.org/kafka/3.3.1/kafka_2.13-3.3.1.tgz
```

Zookeeper can be downloaded with
```shell
wget http://mirror.vorboss.net/apache/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz
```

## Testing with python

Two Python scripts, `producer.py` and `consumer.py` can be used to send and read messages in the Kafka message queue. Install the required dependencies in `requirements.txt` or `pyproject.toml` and run the programs. `data.py` contains shared data. The library used is [`kafka-python`](https://github.com/dpkp/kafka-python). Keep in mind it is asynchronous.

# Debugging

Check if Kafka is alive with [`kcat`](https://github.com/edenhill/kcat)

Write a message to the broker
```shell
echo "hello" | kcat -P -b localhost:9093 -t kafkaz
```

Read a message from the broker
```shell
kcat -C -t kafkaz -b localhost:9093
```

Check if the [connection is](https://brandur.org/fragments/test-kafka) live with `telnet`
```shell
telnet localhost 9093
```

# REFERENCES

[Zookeeper quickstart guide](https://zookeeper.apache.org/doc/r3.5.10/zookeeperStarted.html)
