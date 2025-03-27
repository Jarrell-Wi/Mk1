Ip = input()
Ip = Ip.split('.')
ctr = 0
for i in Ip:
    if int(i) > 255 or int(i) < 0:
        print('Invalid IP address')
        break
    if len(i) > 3:
        print('Invalid IP address')
        break
    else:
        ctr += 1
if ctr == len(Ip):
    print('Valid IP address')