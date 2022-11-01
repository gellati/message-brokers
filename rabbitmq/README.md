# RabbitMQ message broker

RabbitMQ image from docker hub: https://hub.docker.com/_/rabbitmq

## Running

Start the container with

    docker-compose up

Stop the container with

    docker-compose down

Once the container is running, you can log into it with

    docker exec -it rabbit bash

Inside the container different command line utilities can used. These include

|Command              | Function                                      |
|---------------------|-----------------------------------------------|
|rabbitmqctl          | administrative tasks                          |
|rabbitmq-plugins     | administer plugins                            |
|rabbitmq-diagnostics | information about status of RabbitMQ server   |
|rabbitmq-queues      | working with queues                           |
|rabbitmq-upgrade     | upgrade related tasks                         |


Default port of RabbitMQ is 5672. Default port for management plugin is 15672.

The manager can be accessed from a browser in the address `http://localhost:15672/`.


Find names of available queues with

    curl -s -i -u guest:guest http://localhost:15672/api/queues

A successful request returns a status code of 200 and the queues in JSON format.

## Interfacing with Python

Install the dependencies in `pyproject.toml` with `poetry`.

With Python RabbitMQ can be interfaced with the [pika](https://github.com/pika/pika) module.

To send a message
```shell
python producer.py
```


To read messages in the queue
```shell
python consumer.py
```


### Setup

Create a virtual environment for development with

    python -m venv env

`env` is the name of the virtual environment and can be any of your liking. Initialize the virtual environment with `source ./env/bin/activate`. The virtual environment can be exited with the command `deactivate`.

Then install packages in `requirements.txt` with

    pip install -r requirements.txt

After that, the packages in the poetry installation file `pyproject.toml` can be installed with

    poetry install


### References

Based on the RabbitMQ tutorial in LXF278, August 2021.