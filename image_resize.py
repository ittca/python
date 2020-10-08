import PIL
from PIL import Image

img = Image.open('/home/tiago/imagens/usb.jpg')

img = img.resize((150,150), PIL.Image.ANTIALIAS)
img.save('resized.jpg')
