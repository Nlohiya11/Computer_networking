letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to_continue = True
while to_continue:
    choice = input("type encode for encrypting and decode for decrypting : ")
    text = input("input your text : ")
    q = int(input("input mod value :"))
    p = int(input("input base value :"))
    x = int(input("input x value :"))
    y = int(input("input y value :"))
    r1 = (p ** x) % q
    r2 = (p ** y) % q
    k1 = (r2 ** x) % q
    k2 = (r1 ** y) % q
    if k1 == k2:
        k = k1
    else:
        print("wrpng input")
    shift = k
    list_text = list(map(str, text))
    shift = shift % 26


    def encode(n):
        word = ""
        for i in list_text:
            if i in letters:
                word_position = letters.index(i)
                word_position += n
                letter = letters[word_position]
                word += letter
            else:
                word += i
        print(f"\nYour {choice}d text is {word}")


    if choice == "encode":
        encode(shift)
    if choice == "decode":
        shift *= -1
        encode(shift)
    resume = input("\ndo you want to continue the same process (yes/no) :")
    if resume == "no":
        to_continue = False
    elif resume == "yes":

        if input("type encode for encrypting and decode for decrypting : ") == "encode":
            encode(k)
        else:
            k *= -1
            text = input("input your text : ")
            list_text = list(map(str, text))
            encode(k)
        to_continue = False

    else:
        print("wrong input so it will consider as no")
        to_continue = False
