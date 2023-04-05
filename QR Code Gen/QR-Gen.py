import png
import pyqrcode
import os

global counter
counter = 0
path = './QRCode{}.png'.format(counter)
    
def get_url():
    global web_url
    web_url = input("Please enter URL: ")

def check_url():
        if web_url.isdigit():
            raise TypeError("Please enter a valid URL")
def get_qr():
    global qr_code
    qr_code = pyqrcode.create(web_url)

def get_image():
        global counter
        if not os.path.isfile(path) == True:
            qr_code.png('QRCode{}.png'.format(counter), scale=8)
        else:
            counter += 1
            qr_code.png('QRCode{}.png'.format(counter), scale=8)
        
def opt():
        user_opt = input("Would you like to generate another QR Code? [Y/N]: ")
        if user_opt == 'Y':
            steps()
        else:
            print('Goodbye...')
            exit()

def steps():
     get_url()
     check_url()
     get_qr()
     get_image()
     opt()
    

   
while True:
    steps()
    counter += 1