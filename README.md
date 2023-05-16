# Multi-Container Service with RabbitMQ

This project demonstrates a multi-container service using Docker and RabbitMQ. It consists of three containers: `image_predict` as Producer, `RabbitMQ` as queue, and `data_processor` as Consumer. The `image_predict` container accepts JSON POST requests, validates the data, and pushes the messages to the RabbitMQ queue. The `data_processor` container reads messages from the queue, transforms them, and appends them to a CSV file.

## Prerequisites

Make sure you have the following software installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure
          vision_pipeline/
          ├── data_processor (CONSUMER)/
          │ ├── Dockerfile
          │ ├── requirements.txt
          │ └── consumer.py
          ├── image_predict (PRODUCER)/
          │ ├── Dockerfile
          │ ├── conf
          │ └── snap etc.
          ├── test_script/
          │ ├── vevnv
          │ ├── test.py
          │ └── requirements.txt
          ├── csv_file/
          │ ├── results.xlsx
          │
          └── docker-compose.yml

## Getting Started

1. Clone the repository:

  
         git clone https://github.com/rubayetanjumjoy/vision_pipeline.git
1. Enter into the project:

   
         cd vision_pipeline
1. Start the multicontainer serverice

   
         docker-compose up --build

## Accessing the Producer API

The Producer API is exposed on port 8000. To test the service, you can send POST requests to the endpoint http://localhost:8000/api/predictions/. Please note that you need to provide the data in the following format:

Timestamp: The timestamp should be in the format YYYY-MM-DD HH:MM:SS.MMMMMM, for example, 2023-02-07 14:56:49.386042.

Image frame: The image frame should be provided as a base64-encoded string. Ensure that you properly encode the image before including it in the request payload.

If you do not provide the timestamp in the correct format or if the image frame is not base64-encoded, you will encounter a content type error with receive a 404 response from the API.
Example Request:
         
            curl --location 'http://127.0.0.1:8000/api/predictions/' \
          --header 'Content-Type: application/json' \
          --data '{
                    "device_id": "12211142",
                    "client_id": "11232",
                    "created_at": "2023-02-07 14:56:49.386042", 
                    "data": {
                              "license_id": "012391",
                              "preds": [
                                        {
                                                  "image_frame": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                                                  "prob": 0.24,
                                                  "tags": []
                                        },
                      {
                                                  "image_frame": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                                                  "prob": 5,
                                                  "tags": []
                                        }

                              ] 
                    }
          }'


## Checking the Output CSV File
The csv container (Consumer) appends the transformed messages to a CSV file. The file is located inside the csv container (Consumer) at the path `/app/csv_files/results.xlsx`. It is also mounted by Docker, and on the local machine, it is saved at `vision_pipeline/csv_files/results.xlsx`.

## Stopping the Service
To stop the service and remove the containers, run the following command:

      
      docker-compose down
This will stop the containers and remove the network and volumes associated with the service.

## Running the Test Script
If you want to run the test script to send a 1000 randomly generated requests to the Producer API, follow these steps:

Make sure the containers are running (docker-compose up ).

         cd test_script


Activate Vertual Enviorment and Install the required Python packages:

         
         pip install -r requirements.txt

Run the test script:

        
         python test.py
            
This script will send 1000 randomly generated JSON requests to the Producer API.

Note: The resulting CSV file will contain preds_per_message * num_messages rows and return test case OK response.








