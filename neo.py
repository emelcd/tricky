import os
filepath = 'neo.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = -1
    while line:
        if "\"" in line:
            line_cn = line.replace(" ", "")
            os.system('neofetch.cmd --ascii_distro %s' % line_cn)
            line = fp.readline()
            cnt += 1
        else:
            line = fp.readline()
            cnt += 1
        
