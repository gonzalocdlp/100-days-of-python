alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, direction, shift):
    #resetting
    alphabet2=[]
    x=0
    order=[]
    many=len(alphabet)
    #finding the numbers for the letters
    for letters in alphabet:
        x=x+1
        for l in text:
            if l==letters:
                print(x)   
                order.append(str(x))
                print(order)
    #reordering it
    for letter in alphabet:
        shift=int(shift)
        shift=int(shift)+1
        if shift>=many:
            shift=0
        letter=alphabet[shift]
        alphabet2.append(letter)
        print(alphabet2)
    new=""
    for let2 in order:
        new=new+alphabet2[int(let2)]
    print(new)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
    print('true')
    encrypt(text, direction, shift)


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 