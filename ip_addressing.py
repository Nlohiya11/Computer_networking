ipAdd = str(input("enter IP address : "))
cl = 0
for i in range(5):
    x ='ABCDE'
    if ipAdd[i] == '0':
        cl = i+1
        print(f"class{x[i]}")
        break
ip = ""
for i in range(4):
    oct = ipAdd[8*i:8*(i+1)]
    sumi = 0
    for i in range(8):
        sumi = sumi + int(oct[7 - i])*(2**i)
    ip = ip + str(sumi) + "."
ip = ip[:-1]
if cl<4:
    ip = ip + "/" + str(cl*8)
print(ip)
