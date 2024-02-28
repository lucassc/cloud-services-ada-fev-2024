import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Establish connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost",
     port=5672,
     virtual_host="/"))

channel = connection.channel()

# Make sure the queue exists
channel.queue_declare(queue='my_first_queue')

# Tell RabbitMQ that this callback function should receive messages from our 'hello' queue
channel.basic_consume(queue='my_first_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()