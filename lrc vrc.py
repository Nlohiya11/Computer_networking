letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
user_input = list(input("write your data : "))
number = []
for i in user_input:
    ascii_no = 65 + letters.index(i)
    binary_no = bin(ascii_no).replace("0b", "0")
    number.append(binary_no)
print(number)
list_1 = []
for num in number:
    parity = list(num)
    res = [eval(i) for i in num]
    print(res)
    for x in range(0, len(num) - 1):
        lrc = res[x] + res[x + 1]
        res[x + 1] = lrc
    if lrc % 2 == 0:
        num = "0"
    else:
        num = "1"
    list_1.append(num)

vrc = list("0" * 8)
for y in range(len(number)):
    for z in range(8):
        if number[y][z] == "1":
            if vrc[z] == "0":
                vrc[z] = "1"
            else:
                vrc[z] = "0"

print("lrc : " + "".join(list_1))
print("vrc : " + "".join(vrc))




