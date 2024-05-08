import requests

# URL of the server
SERVER_URL = 'http://server:8080/'

# Function to send a GET request to the server
def send_get_request():
    response = requests.get(SERVER_URL)
    print("Response from server:", response.text)

# Function to send a POST request to the server
def send_post_request(data):
    response = requests.post(SERVER_URL, json=data)
    print("Response from server:", response.text)

if __name__ == '__main__':
    # Sending a GET request to the server
    print("Sending GET request to the server...")
    send_get_request()

    # Sending a POST request to the server
    print("Sending POST request to the server...")
    data = {'name': 'John', 'age': 30}
    send_post_request(data)
