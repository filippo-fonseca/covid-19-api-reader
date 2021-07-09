import requests

api = "https://disease.sh/v3/covid-19/all"
json_data = requests.get(api).json()
total_cases = str(json_data['cases'])

# not even close to finishing xD

print(total_cases)
