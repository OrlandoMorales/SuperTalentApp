import http.client
import json
import ssl
import uuid
import gzip



class RestClient:
    def __init__(self, base_url, bearer_token):
        self.base_url = base_url
        self.bearer_token = bearer_token
        self.connection = None  # Initialize connection lazily

    def __enter__(self):
        self.connection = http.client.HTTPSConnection(self.base_url)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def _send_request(self, method, url, headers={}, data=None):
        if not self.connection:
            self.__enter__()

        headers["Authorization"] = f"Bearer {self.bearer_token}"
        headers["Cache-Control"] = "no-cache"
        headers["Postman-Token"] = str(uuid.uuid4()) 
        headers["Host"] = self.base_url
        headers["User-Agent"] = 'PostmanRuntime/7.37.0' 
        headers["Accept"] = "*/*"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Connection"] = "keep-alive"
        headers["Request-Id"] = str(uuid.uuid4())
        headers["Content-Type"] = "application/json; text/html; charset=UTF-8"
        headers.update(headers)  # Allow overriding headers

        try:
            if data:
                data = json.dumps(data)
                headers["Content-Type"] = "application/json"
                self.connection.request(method, url, body=data, headers=headers)
            else:
                self.connection.request(method, url, headers=headers)

            response = self.connection.getresponse()
           
            if response.getheader("Content-Encoding") == "gzip":
                data = gzip.decompress(response.read())
                return data.decode("utf-8"), response.status
            else:
                return response.read().decode("utf-8"), response.status


        except Exception as e:
            raise ConnectionError(f"Error sending request: {e}")

    def get(self, url, headers={}):
        response_body, status_code = self._send_request("GET", url, headers=headers)
        return self._handle_response(response_body, status_code)


    def post(self, url, data=None, headers={}):
        response_body, status_code = self._send_request("POST", url, headers=headers, data=data)
        return self._handle_response(response_body, status_code)


    def _handle_response(self, response_body, status_code):
        try:
            data = json.loads(response_body)
        except json.JSONDecodeError:
            data = response_body

        return data, status_code

