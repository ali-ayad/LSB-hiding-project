import numpy as np
from PIL import Image


def encode():
    message = input("Enter the text to be hidden: ")
    # Encode the message in a serie of 8-bit values
    b_message = ''.join(["{:08b}".format(ord(x)) for x in message])
    b_message = [int(x) for x in b_message]
    # print(b_message)
    b_message_lenght = len(b_message)
    # Get the image pixel arrays
    imge=input("Enter the image name (with extension): ")
    img = Image.open(imge,'r')
    width, height = img.size
    data = np.array(img)

    # write the pixel arraysy
    data = np.reshape(data, width*height*3)
    #  writing LSB
    data[:b_message_lenght] = data[:b_message_lenght] & ~1 | b_message

    # Reshape back to an image pixel array
    data = np.reshape(data, (height, width, 3))

    new_img = Image.fromarray(data)
    new_img.save("cover-1.png")
    new_img.show()



def decode():
    imge=input("Enter the cover image: ")
    img = Image.open(imge,"r")
    width, height = img.size
    data = np.array(img)
    
    data = np.reshape(data, width*height*3)
     # extract lsb
    data = data & 1 
    print(data)
    # Packs binary-valued array into 8-bits array.
    data = np.packbits(data)
    # Read and convert integer to Unicode characters until hitting a non-printable character
    for x  in data:
        l = chr(x)
        #if not l.isprintable():
        if(l=='0'):
            break
         
        print(l, end='')

def main():
    a =int(input("##   Welcome to the Steganography   ##\n"
     "1. Encode\n""2. Decode\n"))

    if(a==1):
        encode()

    elif(a==2):
       decode()
        
    else:
        raise Exception("Enter correct input")
        

if __name__== '__main__':

     main()    




    

   




