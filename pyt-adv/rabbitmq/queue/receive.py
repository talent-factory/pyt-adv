#!/usr/bin/env python

"""
Das Programm empfängt und verarbeitet Nachrichten aus einer Queue:

1. Verbindung aufbauen und Queue deklarieren (wie beim Sender)
2. Callback-Funktion definieren, die empfangene Nachrichten ausgibt
3. Callback an Queue binden mit `basic_consume`
4. Endlosschleife starten zum Warten auf Nachrichten

Wichtige Konzepte:
- Queue-Deklaration ist idempotent - mehrfache Deklaration schadet nicht
- Empfang läuft asynchron über Callback-Funktion
- Programm läuft bis zum manuellen Abbruch (CTRL+C)
- Queues können mit `rabbitmqctl list_queues` inspiziert werden

Der Code nutzt exception handling für sauberes Beenden des Programms.

Referenz: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import sys

import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [✓] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
