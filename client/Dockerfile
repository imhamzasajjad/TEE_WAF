# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the client code into the container
COPY client.py .

# Install requests library
RUN pip install requests

# Command to run the client code
CMD ["python", "client.py"]