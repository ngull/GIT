#import sys
HOST1 = '/home/ngull/Documents/GIT/ngull/local files/HOST1.txt'
outF = open(HOST1, "a")
#sys.stdout = open('HOST1.txt', 'wt')
with open("ipfile2.txt", "r") as f:
    ip1 = f.read().splitlines()
#print(ip)
for ip in ip1:
    print(" {")
    print(' "l3extSubnet": {')
    print(' "attributes": {')
    print(' "aggregate": "",')
    print(' "annotation": "",')
    print(' "descr": "",')
    print('"ip": ' + ip + ',')
    print('"name": "N-MS-OFFICE-365",')
    print('"nameAlias": "",')
    print('"scope": "import-security"')
    print(' }')
    print(' } ')
    print(' },')
    outF.write(ip)
