# test-aks-cluster
Test AKS cluster for technorely



manifest for deploying two containers in the same pod, each containing the AZURE_STORAGE_CONNECTION_STRING environment variable, which is used to connect to the Azure Storage Queue.
Docker images for containers are uploaded to the Docker repository using the my-registry-secret secret.



message-queue.py
We define the queue connection string queue_connection_string and the queue name queue_name and then use the send_message() method of the queue client to send the message. To delay sending a message, we use the sleep() function of the time module.



hello-world.py 
For each message, we call the start_container() function, which starts a container with the image my-docker-registry/hello-world:latest and passes the message from the queue to it as the MESSAGE environment variable. We then remove the message from the queue using the queue client's delete_message() method.


Both features can be deployed to Kubernetes using the manifest we defined above. Once the Kubernetes manifest has been deployed to Azure, the functions will work automatically and push and receive messages from the queue, as well as start containers with a "Hello World" message.


