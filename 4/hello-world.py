from azure.storage.queue import QueueClient
import os
import docker

queue_connection_string = "<connection-string>"
queue_name = "myqueue"

def start_container(message):
    client = docker.from_env()
    container = client.containers.run("my-docker-registry/hello-world:latest", detach=True, environment=["MESSAGE=" + message])
    print("Started container: " + container.id)

def process_queue():
    queue_client = QueueClient.from_connection_string(queue_connection_string, queue_name)
    messages = queue_client.receive_messages()
    for message in messages:
        start_container(message.content)
        queue_client.delete_message(message)
        print("Processed message: " + message.content)

while True:
    process_queue()
