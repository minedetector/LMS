FROM grafana/loki:2.6.0

USER root

RUN mkdir -p /wal /loki/wal /loki/chunks /loki/boltdb-shipper-active \
    /loki/boltdb-shipper-cache /loki/compactor /loki/rules /loki/rules-temp

RUN chown -R loki:loki /wal /loki

USER loki
