import cv2

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
user_input = list(input("write your data : "))
number = []
for g in user_input:
    if g not in letters:
        number.append('null')
    else:
        ascii_no = 65 + letters.index(g)
        binary_no = bin(ascii_no).replace("0b", "0")
        number.append(binary_no)


img_name = input("Enter image name (with extension): ")
img = cv2.imread(img_name)
b = img.copy()
print("The shape of the image is: ", img.shape)
resizedImg = cv2.resize(img, (500, 500))
m, n, p = b.shape
print(m, n, p)
nBytes = img.shape[0] * img.shape[1] * 3 // 8
a = []
print("Maximum Bytes for encoding:", nBytes)
print(b)
is_continue = True
while is_continue:
    for i in range(0, p):
        for j in b[i]:
            for k in j:
                if len(a) != len(number):
                    a.append(k)
                else:
                    is_continue = False
print(a)
new_a = []
for num in range(len(a)):
    if a[num] % 2 == 1:
        if number[num][-1] == '0':
            cv = a[num] - 1

            new_a.append(cv)
        else:
            cv = a[num]
            new_a.append(cv)
    else:
        if number[num][-1] == '1':
            cv = a[num] + 1
            new_a.append(cv)
        else:
            cv = a[num]
            new_a.append(cv)
new_a.replace(b[0])

print(b)