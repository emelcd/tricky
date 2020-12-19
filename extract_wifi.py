import os

os.system('netsh wlan show profiles >> wifis.txt')

wifis = []
wifis_p = []
passwords = []
result = []
with open('wifis.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        if "todos" in line:
            wifis.append(line)


for wifi in wifis:
    wifis_p.append(wifi[38:].replace("\n","").replace(" ",""))
wifis_p = list(dict.fromkeys(wifis_p))
print(wifis_p)
for bbsid in wifis_p:
    os.system('netsh wlan show profiles name=%s key=clear | findstr "clave" >> tmp_wifi.txt' % bbsid)
    with open('tmp_wifi.txt') as f:
        for line in f.readlines():
            passwords.append(line[28:].replace(" ","" ))

            
passwords = list(dict.fromkeys(passwords))

for i in range(len(wifis_p)):

    result_x = wifis_p[i] +" ==> "+  passwords[i]
    result.append(result_x)


os.remove('wifis.txt')
os.remove('tmp_wifi.txt')

# print(len(result))
# print(range(len(result)))

f = open("results.txt", "w")

for line in result:
    f.writelines(line)

f.close()



