import requests,json

# url = 'https://hooks.slack.com/services/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'
# headers = {'Content-type: application/json'}
# res = requests.post(url,json.dumps({"text":"Hello, World!"}))
# print(res.text)
url = 'http://127.0.0.1:5000/api/v1/todos'
headers = {'Content-type: application/json'}
res = requests.post(url,json.dumps({"text":"Hello, World!"}))
print(res.text)