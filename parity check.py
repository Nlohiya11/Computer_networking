data = (input("write your data to check parity: "))
parity = 0
for i in range(0,len(data)):
    a = int(data[i])
    parity += a
if parity % 2 == 0:
    print("it's an even parity")
else:
    print("it's an odd parity")
