# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the WAF server code into the container
COPY waf.py .

# Install Flask
RUN pip install Flask

# Command to run the WAF server code
CMD ["python", "waf.py"]
