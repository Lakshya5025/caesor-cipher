alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(direction , text, shift):
    new_text = ""
    if direction == "decode":
        shift = shift * -1
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift
            new_char = alphabets[new_position]
            new_text += new_char
        else:
            new_text += char
    print(new_text)
end = False
while end == False:
    direction = input("Enter 'encode' for Encrypt, Enter 'decode' for Decrypt: ")
    text = input("Enter the Text: ")
    shift = int(input("Enter the shift amount: "))
    shift = shift % 26
    caesar(direction , text, shift)
    decision = input("Type 'yes' for exit, else type 'no': ")
    if decision == 'yes':
        end = True
        print("Good bye")