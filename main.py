import requests

# Sensitive information in Python code
AWS_SECRET_KEY = 'AKIA1234567890123456'  # AWS Secret Key
PAYPAL_API_KEY = 'A21AA2PQtT2jXyTk4bW8wSP2QkTLQ5'  # PayPal API Key

def send_request(data):
    url = "https://api.example.com/data"
    headers = {
        'Authorization': f'Bearer {AWS_SECRET_KEY}'  # Using AWS key in headers
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Example data
data = {
    'user_id': 101,
    'amount': 250,
    'paypal_key': PAYPAL_API_KEY  # PayPal Key hardcoded
}

response = send_request(data)
print(response)
