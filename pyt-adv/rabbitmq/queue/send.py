#!/usr/bin/env python

"""
Das Python-Programm stellt eine Verbindung zu RabbitMQ her und sendet eine Nachricht. Hauptschritte:

1. Verbindung zum RabbitMQ-Server aufbauen (`localhost`)
2. Queue "hello" deklarieren
3. Nachricht "Hello World!" über den Default-Exchange an die Queue senden
4. Verbindung sauber schließen

Wichtige Konzepte:
- Nachrichten müssen immer über einen Exchange laufen
- Der Default-Exchange (leerer String) leitet Nachrichten direkt an die angegebene Queue weiter
- Die Queue muss vor dem Senden existieren

Der Code nutzt die pika-Bibliothek für die RabbitMQ-Kommunikation.

Referenz: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import pika

message = 'Hello, World!'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f' [✓] Sent {message}')
connection.close()
