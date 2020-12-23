import os

os.remove('profiles.txt')
os.system('netsh wlan show profiles >> profiles.txt')

profiles = []
with open('profiles.txt') as f:
    for line in f.readlines():
        if ":" in line:
            profiles.append(line.replace("\n", "")
)   
npro = []
for i, line in enumerate(profiles):
    if i != 0:
        for i, line in enumerate(line.split(":")):
            if i != 0:
                line.replace(" ","")
                npro.append(line[1:])
npro = list(set(npro))
profiles = []
try:
    os.remove("pass.txt")
except:
    pass
for line in npro:
    if line != "":
        profiles.append(line)
for line in profiles:
    os.system("netsh wlan show profile name=%s key=clear >> pass.txt" % line)


i = 0
with open('pass.txt', 'r') as f:
    for line in f.readlines():
        if  "clave" in line:
            print(profiles[i],line[25:])
            i += 1
