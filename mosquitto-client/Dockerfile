FROM alpine:3.20.3

WORKDIR /usr/src/mosquitto-client

RUN apk update && \
    apk add --no-cache python3 py3-paho-mqtt

    
COPY . .

CMD [ "python3",  "mosquitto_client.py" ]
