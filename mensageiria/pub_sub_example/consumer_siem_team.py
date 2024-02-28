import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost",
     port=5672,
     virtual_host="/"))

channel = connection.channel()

channel.queue_declare(queue="queue_siem_team", arguments={"x-max-priority": 10})
channel.queue_bind(exchange="amq.fanout", queue="queue_siem_team")


def chamado_quando_uma_mensagem_eh_consumida(channel, method_frame, header_frame, body):
    try:
        print("Mensagem: ", body)
        print("LOG gerado para ferramenta de SIEM")
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)

    except Exception as e:
        print("Erro: ", e)
        channel.basic_nack(delivery_tag=method_frame.delivery_tag, requeue=False)

channel.basic_consume(queue="queue_siem_team", 
                      on_message_callback=chamado_quando_uma_mensagem_eh_consumida, auto_ack=False)


print("Esperando por mensagens. Para sair pressione CTRL+C")
channel.start_consuming()