letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
user_input = list(input("write your data : "))
i = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = []
for g in user_input:
    ascii_no = 65 + letters.index(g)
    binary_no = bin(ascii_no).replace("0b", "0")
    number.append(binary_no)
a = 0
new_i = []
while a in range(len(number)):
    data = number[a]
    for k in i:
        if k % 2 == 1:
            if data[-1] == 0:
                k = k - 1
            else:
                k = k
        else:
            if data[-1] == 1:
                k = k + 1
            else:
                k = k
            a += 1
        new_i.append(k)
    print(new_i)