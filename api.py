import requests
import json
import pandas as pd
# API URL
url="https://api.socialverseapp.com/users/get_all?page=1&page_size=1000"
# Authorization token
headers = {
    "Flic-Token": "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"
}
#
# Send a GET request with the authorization token in the headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse the response as JSON
      # Optional: Print the data to see the respsonse
    
    # Store the data in a JSON file
    with open('user.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print("Data saved to like.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

data=data['users']
df=pd.DataFrame(data)
df.to_csv('user.csv', index=False)

