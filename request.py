import requests
r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=36c185a3c5f023761c4fb212e769a2de24f747dc')
print(r.status_code)
print(r.text)