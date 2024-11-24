import pika
import json
from rabbit_config import RabbitConfig, get_rabbit_connection

def article_notification_consumer():
    """Mendengarkan notifikasi artikel."""
    connection = get_rabbit_connection()
    channel = connection.channel()

    channel.queue_declare(queue=RabbitConfig.ARTICLE_QUEUE, durable=True)
    channel.queue_bind(
        exchange=RabbitConfig.ARTICLE_EXCHANGE,
        queue=RabbitConfig.ARTICLE_QUEUE,
        routing_key=RabbitConfig.ARTICLE_ROUTING_KEY
    )

    def callback(ch, method, properties, body):
        message = json.loads(body)
        print("original msg:", message)
        print(f"Artikel diterima: {message['title']} oleh {message['author_id']}")

    channel.basic_consume(queue=RabbitConfig.ARTICLE_QUEUE, on_message_callback=callback, auto_ack=True)
    print("Listening for article notifications...")
    channel.start_consuming()

def user_registration_consumer():
    """Mendengarkan notifikasi registrasi pengguna."""
    connection = get_rabbit_connection()
    channel = connection.channel()

    channel.queue_declare(queue=RabbitConfig.USER_QUEUE, durable=True)
    channel.queue_bind(
        exchange=RabbitConfig.USER_EXCHANGE,
        queue=RabbitConfig.USER_QUEUE,
        routing_key=RabbitConfig.USER_ROUTING_KEY
    )

    def callback(ch, method, properties, body):
        message = json.loads(body)
        print(f"Registrasi pengguna diterima: {message['username']} dengan email {message['email']}")

    channel.basic_consume(queue=RabbitConfig.USER_QUEUE, on_message_callback=callback, auto_ack=True)
    print("Listening for user registration notifications...")
    channel.start_consuming()
