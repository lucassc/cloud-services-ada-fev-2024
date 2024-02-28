import datetime
import pika

# Connect to a RabbitMQ server running on the local machine
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost",
     port=5672,
     virtual_host="/"))

channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='my_first_queue')


# Message attributes
properties = pika.BasicProperties(
    content_type='application/json',      # MIME-type of the message body
    # content_encoding='utf-8',             # Encoding of the message body
    # delivery_mode=2,                      # Make message persistent
    # priority=5,                           # Priority level
    # correlation_id='example_correlation_id',  # Correlate replies with requests
    reply_to='hello',               # Queue name for replies
    expiration='10000',                     # Message expiration period (milliseconds)
    # message_id='unique_message_id',       # Unique identifier for the message
    # timestamp=datetime.now().timestamp(), # Message timestamp
    # type='example_type',                  # Type of the message
    # user_id='user',                       # User ID who sent the message
    # app_id='example_app',                 # Identifier for the application
    # headers={'key': 'value'}              # Application-specific attributes
)


# Publish a message to the 'hello' queue
channel.basic_publish(exchange='',
                      routing_key='my_first_queue',
                      body='{"message":"Hello World!"}',
                      properties=properties)

print(" [x] Sent 'Hello World!'")

# Close the connection
connection.close()