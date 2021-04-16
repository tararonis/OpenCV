import requests

url = 'http://media.pastorchuck.com/russian/C2000/40_%D0%9E%D1%82%20%D0%9C%D0%B0%D1%82%D1%84%D0%B5%D1%8F%201-4_B.mp3'

r = requests.get(url, allow_redirects=True)

open('/home/roman/MyFiles/!temp/new_testament/Евангелие от Матфея 1-4_B.mp3', 'wb').write(r.content)