FROM debian:bullseye-slim

RUN groupadd -r rsyslog && useradd -r -g rsyslog rsyslog

RUN apt-get update && apt-get install -y rsyslog \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /sb/logs/incoming

RUN chown -R rsyslog:rsyslog /sb/logs

EXPOSE 5514/udp 5514/tcp

USER rsyslog

CMD ["rsyslogd", "-n"]
