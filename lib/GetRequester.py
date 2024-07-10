import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Use response.content to get bytes data

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body.decode('utf-8'))  # Decode bytes to UTF-8 and parse JSON
