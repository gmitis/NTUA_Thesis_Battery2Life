from paho.mqtt import client as mqtt
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s-%(levelname)s: %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('mosquitto.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s: %(message)s' ,
    handlers=[
        logging.FileHandler('./log.txt'),
        logging.StreamHandler()
    ]
)

logger.debug('Starting Mosquitto Client...')

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        logging.debug('Client connected successfully to mosquitto...')
        mqtt_client.subscribe('hello/topic')
        logging.debug('Subscribed successfully')
    else:
        logging.debug(f'Bad Connection. Code: {rc}')

def on_message(mqtt_client, userdata, msg):
    logging.info(f"Got message with payload: {msg.payload} from topic: {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(
    os.environ.get("MQTT_USER"), 
    os.environ.get("MQTT_PASSWORD")
)
client.connect(
    host=os.environ.get("MQTT_BROKER"),
    port=int(os.environ.get("MQTT_PORT")),
    keepalive=int(os.environ.get("MQTT_KEEPALIVE"))
)

client.loop_forever()
