import qrcode as qr         # import qrcode python moddule that helps to generate and save the QR
from PIL import Image       # from PIL library import image that help us to modify or changes in the qr code 

# now we going to start code
# Usual Qr code 

img=qr.make("Your message might be link or String")  # here make function help to create qr code
img.save("name_of_image.png")       # here we store the image with save function. you can choose extention according requirement.



# Now we generate QR code with few changes according to the requirements.

qrr=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=6)   # here we declare the box size of qrcode and their border as well.
qrr.add_data("Your message might be link or String")            # we add message it should be any link or message
qrr.make(fit=True)              # here QR code Generate with qrr data and qrr properties.
img=qrr.make_image(fill_color="red",back_color="yellow")   # here we decide the image color as per need.
img.save("name_of_image.png")   # here we store the image with save function. you can choose extention according requirement.


#Thanx
