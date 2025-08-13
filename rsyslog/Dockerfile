FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y rsyslog

RUN mkdir -p /sb/logs/incoming

EXPOSE 5514/udp 5514/tcp

CMD ["rsyslogd", "-n"]
