import os
import logging
from flask import Flask, request

app = Flask(__name__)

# Get the absolute path of the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current directory:", current_dir)  # Print current directory for debugging

# Specify the absolute path for the log file
log_file_path = os.path.join(current_dir, 'waf.log')

# Configure logging to write to the absolute path specified
logging.basicConfig(filename=log_file_path, level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "This is the backup homepage"
    elif request.method == 'POST':
        data = request.get_json()
        # Log the received data
        logging.info(f"Received POST request with data: {data}")
        return "Request received and logged"
    else:
        return "Method not allowed"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8082)
