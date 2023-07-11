letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
to_continue = True
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
while to_continue:
    choice = input("type encode for encrypting and decode for decrypting : ")
    text = input("input your text : ")
    shift = 2
    list_text = list(map(str, text))

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
            encode(shift)
        else:
            shift *= -1
            text = input("input your text : ")
            list_text = list(map(str, text))
            encode(shift)
        to_continue = False

    else:
        print("wrong input so it will consider as no")
        to_continue = False