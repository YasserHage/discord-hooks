import os
from flask import request
from services.bitbucket_service import process as process_bitbucket_request
from services.azure_service import process as process_azure_request


@app.route(os.getenv('AZURE_ENDPOINT_URL'), methods=['POST'])
def azure_webhook():
    data = request.get_json()
    response = process_azure_request(data)
    if response.status_code != 200:
        print(response.text)
    return response.text, response.status_code

@app.route(os.getenv('BITBUCKET_ENDPOINT_URL'), methods=['POST'])
def bitbucket_webhook():
    data = request.get_json()
    response = process_bitbucket_request(data)
    if response.status_code != 200:
        print(response.text)
    return response.text, response.status_code
