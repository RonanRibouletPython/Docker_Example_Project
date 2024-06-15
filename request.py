import requests

# Define the URL of your Flask API
url = 'http://127.0.0.1:5000/prediction'

# Define the input data as a dictionary
data = {
    "variance": [0.3],
    "skewness": [3.3],
    "curtosis": [-4.6],
    "entropy": [-5.1]
}

# Send a POST request to the API with the input data
response = requests.post(url, json=data)

# Check the HTTP response status code
try :
    response.status_code == 200

    # Parse and print the JSON response (assuming it contains the prediction)
    prediction = response.json()
    print(f"The prediction is {prediction}")

except:
    # Handle the case where the API request failed
    print(f'API Request Failed with Status Code: {response.status_code}')
    print(f'Response Content: {response.text}')

