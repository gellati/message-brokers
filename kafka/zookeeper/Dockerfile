FROM debian:bullseye-slim

ARG ZOOKEEPER_VERSION

RUN apt update && apt install --yes build-essential \
  openjdk-11-jre-headless

COPY apache-zookeeper-${ZOOKEEPER_VERSION}-bin.tar.gz .

RUN tar -xzf apache-zookeeper-${ZOOKEEPER_VERSION}-bin.tar.gz -C /opt
RUN mv /opt/apache-zookeeper-${ZOOKEEPER_VERSION}-bin /opt/apache-zookeeper

RUN mkdir /opt/apache-zookeeper/data
COPY zoo.cfg log4j.properties /opt/apache-zookeeper/conf/

EXPOSE 2181 2888 3888

CMD [ "/opt/apache-zookeeper/bin/zkServer.sh", "start-foreground" ]
