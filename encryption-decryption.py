# Importing libraries
from tkinter import *
import base64

# Initialising the window
root = Tk()

root.geometry('570x570')
root.resizable(0,0)
root.title("DataFlair - Message Encode and Decode")

Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()

# Defining variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

# function definition section
def Encode(key,message):
    enc=[]

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

def encoded_output():
    Result.set(Encode(private_key.get(), Text.get()))

def decoded_output():
    Result.set(Decode(private_key.get(), Text.get()))

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


Label(root, font = 'arial 16 bold', text='TEXT').place(x= 60,y=60)
Entry(root, font = 'arial 16 bold', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

Label(root, font = 'arial 16 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 16 bold', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Button(root, font = 'arial 16 bold', text = 'ENCODE', width = 8, command = encoded_output, bg = 'Lightgrey', padx=2, pady=2).place(x = 110, y = 130)
Button(root, font = 'arial 16 bold', text = 'DECODE', width = 8, command = decoded_output, bg = 'Lightgrey', padx=2, pady=2).place(x = 290, y = 130)

Label(root, font = 'arial 16 bold', text ='RESULT').place(x=60, y = 195)
Entry(root, font = 'arial 16 bold', textvariable = Result , bg ='ghost white').place(x=290, y = 195)


Button(root, font = 'arial 16 bold', text = 'RESET', width = 8, command = Reset, bg = 'LimeGreen', padx=2, pady=2).place(x=110, y = 255)
Button(root, font = 'arial 16 bold', text = 'EXIT', width = 8, command = Exit, bg = 'OrangeRed', padx=2, pady=2).place(x=290, y = 255)

root.mainloop()