import requests
import json
d = {'numero_casas': 4, 'token': '36c185a3c5f023761c4fb212e769a2de24f747dc', 'cifrado': 'glygo rsvvmw hsiwr’x ks lyrxmrk. glygo rsvvmw ksiw omppmrk. yrorsar', 'decifrado': 'chuck norris doesn’t go hunting. chuck norris goes killing. unknown', 'resumo_criptografico': 'fc1502438d6682ea6779622b43f6c37a3d0e44eb'}
rs = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=36c185a3c5f023761c4fb212e769a2de24f747dc', data=d)
print(rs.text)
r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=36c185a3c5f023761c4fb212e769a2de24f747dc')
print(r.status_code)
print(r.json())
