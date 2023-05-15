# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

 
# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 



# Copy the source code to the working directory
COPY . .
RUN mkdir csv_files

# Set the environment variable for running the application
ENV PYTHONUNBUFFERED=1

 

# Set the command to run the consumer script
CMD [ "python", "./consumer.py" ]
