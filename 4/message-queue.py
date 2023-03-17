from azure.storage.queue import QueueClient
import time

queue_connection_string = "<connection-string>"
queue_name = "myqueue"

def send_message_to_queue():
    queue_client = QueueClient.from_connection_string(queue_connection_string, queue_name)
    message = "Hello from Azure Functions!"
    queue_client.send_message(message)
    print("Sent message: " + message)

while True:
    send_message_to_queue()
    time.sleep(60)
