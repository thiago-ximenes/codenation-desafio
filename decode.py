import hashlib
cif = 'glygo rsvvmw hsiwr’x ks lyrxmrk. glygo rsvvmw ksiw omppmrk. yrorsar'
alfa = 'abcdefghijklmnopqrstuvwxyz'
n = 4
decif = ' '
for c in range(0, len(cif)):
    if cif[c] in alfa:
        d = alfa.find(cif[c])
        dec = (d - n) % len(alfa)
        decif += alfa[dec]
    else:
        decif += cif[c]
print(decif)
print()
m = hashlib.sha1('chuck norris doesn’t go hunting. chuck norris goes killing. unknown'.encode('utf-8'))
print(m.hexdigest())