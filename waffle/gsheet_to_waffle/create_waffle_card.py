import requests, json

# no authentication method provided for waffle
url = 'https://api.waffle.io/udacity/robotics-beta-test-issues/cards?access_token=<?>'

#payload = open("request.json")
payload = '{"githubMetadata": {"source": "<github metadata>","title": "title"}'

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)
