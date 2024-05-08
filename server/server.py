import os
import logging
from flask import Flask, request
import requests

app = Flask(__name__)

ML_SERVER_URL = 'http://ml:8081/'
WAF_SERVER_URL = 'http://waf:8082/'

# Get the absolute path of the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the absolute path for the log file
log_file_path = os.path.join(current_dir, 'server.log')

# Configure logging to write to the absolute path specified
logging.basicConfig(filename=log_file_path, level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "This is the homepage"
    elif request.method == 'POST':
        data = request.get_json()
        # Log the received data
        logging.info(f"Received POST request with data: {data}")
        
        # Forward the received request to ML server
        ml_response = requests.post(ML_SERVER_URL, json=data)
        # Forward the received request to WAF server
        waf_response = requests.post(WAF_SERVER_URL, json=data)

        # Log the response from ML server
        logging.info(f"Response from ML server: {ml_response.text}")
        # Log the response from WAF server
        logging.info(f"Response from WAF server: {waf_response.text}")
        
        return "Request received and forwarded to ML server and WAF"
    else:
        return "Method not allowed"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
