FROM debian:bullseye-slim

ARG SCALA_VERSION
ARG KAFKA_VERSION
ARG KAFKA_ZOOKEEPER_CONNECT
ARG KAFKA_BROKER_ID
ARG KAFKA_LISTENERS
ARG KAFKA_ADVERTISED_LISTENERS
ARG KAFKA_LISTENER_SECURITY_PROTOCOL_MAP
ARG KAFKA_INTER_BROKER_LISTENER_NAME

RUN apt update && apt install --yes build-essential \
  openjdk-11-jre-headless

COPY kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz /tmp/

RUN tar -xzf /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt \
  && mv /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka

RUN sed -i "s/^zookeeper.connect=localhost:2181/zookeeper.connect=${KAFKA_ZOOKEEPER_CONNECT}/" "/opt/kafka/config/server.properties"
RUN sed -i "s/^broker.id=0/broker.id=${KAFKA_BROKER_ID}/" "/opt/kafka/config/server.properties"


RUN echo "listeners=${KAFKA_LISTENERS}" >> /opt/kafka/config/server.properties
RUN echo "advertised.listeners=${KAFKA_ADVERTISED_LISTENERS}" >> /opt/kafka/config/server.properties
RUN echo "listener.security.protocol.map=${KAFKA_LISTENER_SECURITY_PROTOCOL_MAP}" >> /opt/kafka/config/server.properties
RUN echo "inter.broker.listener.name=${KAFKA_INTER_BROKER_LISTENER_NAME}" >> /opt/kafka/config/server.properties

# Uncomment the following lines to enable zookeeper admin server
# go in the browser to localhost:8080/commands
# RUN sed -i "s/^admin.enableServer=false/admin.enableServer=true/" "/opt/kafka/config/zookeeper.properties"
# RUN echo "admin.serverPort=8080" >> /opt/kafka/config/zookeeper.properties

CMD [ "/opt/kafka/bin/kafka-server-start.sh", "/opt/kafka/config/server.properties" ]