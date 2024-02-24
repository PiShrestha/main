import requests

api_key = 'N4rqFNpsuEDA13BoBHWqpyYhyCHir2TxXwJe7FFP'
upc = '016000264694'
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key={}&query={}'.format(api_key, upc))

print(response.status_code)
print(response.json())    