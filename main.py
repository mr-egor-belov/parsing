import requests
import pprint

response = requests.get('https://www.google.com')

print(response.status_code)  # Correct attribute

if response.ok:
    print('Запрос успешно выполнен')
else:
    print('Произошла ошибка')

# Print only the first 500 characters of response.content to avoid huge output
print(response.content[:500])

# Check if the response contains JSON before parsing
try:
    response_json = response.json()
    pprint.pprint(response_json)
except requests.exceptions.JSONDecodeError:
    print("Ответ не в формате JSON. Возможно, это HTML-страница.")
