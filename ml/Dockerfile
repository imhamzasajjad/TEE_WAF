# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the ML server code into the container
COPY ml.py .

# Install Flask
RUN pip install Flask

# Command to run the ML server code
CMD ["python", "ml.py"]
