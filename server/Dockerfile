# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the server code into the container
COPY server.py .

# Install Flask and requests library
RUN pip install Flask requests

# Command to run the server code
CMD ["python", "server.py"]
