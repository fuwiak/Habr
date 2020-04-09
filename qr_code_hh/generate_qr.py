import qrcode


img_name = "habr.png"

def generate(data="https://habr.com", img_name="habr.png"):
	img = qrcode.make(data) #generate QRcode
	img.save(img_name)
	return img

generate()


def read_qr(img_name):
	import cv2
	img = cv2.imread(img_name)
	return img

qr = read_qr(img_name)