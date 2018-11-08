FROM python:3-alpine
COPY requirements.txt /tmp
RUN apk add gcc g++ libstdc++ musl-dev; pip install -r /tmp/requirements.txt; apk del gcc g++ musl-dev

RUN mkdir -p /opt/tester/protos
COPY *.py /opt/tester/
COPY protos/cloudkeeper.proto /opt/tester/protos/
WORKDIR /opt/tester
RUN python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. protos/cloudkeeper.proto

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/sh"]
EXPOSE 9876

