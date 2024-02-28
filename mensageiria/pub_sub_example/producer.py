import datetime
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost",
     port=5672,
     virtual_host="/"))

channel = connection.channel()


body = '{"msg":"Hello World!", "data":"' + str(datetime.datetime.now()) + '"'

properties = pika.BasicProperties(
    # expiration="10000",
     priority= 7,
     app_id="",
     content_type="application/json",
     reply_to="replay_queue"           )

channel.basic_publish(exchange="amq.fanout",
                      routing_key="",
                      body=body,
                      properties=properties,
                      )

print(f"[x] Sent '{body}'")

channel.close()
