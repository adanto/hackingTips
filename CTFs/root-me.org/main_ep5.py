#!/usr/bin/env python 

import requests
from PIL import Image
import pytesseract
from pytesseract import image_to_string
from base64 import b64decode
import re

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def main():
	
	URL = 'http://challenge01.root-me.org/programmation/ch8/'

	session = requests.Session()

	r = session.get(url = URL) 

	if r.status_code == 200:
		content = r.content

		img = content[content.index("image/png;base64,") + len("image/png;base64,"):content.index("\" /><br><br><form actio")]
		with open('image_ep5.jpg', 'w+') as f:
			f.write(b64decode(img))


		d = image_to_string(Image.open("image_ep5.jpg"))

		regex = re.compile('[^a-zA-Z0-9]')
		a = regex.sub('', "".join(d.split()).strip())

		r2 = session.post(URL, data = {
				"cametu": a
			})

		if r2.status_code == 200:
			print a

			content = r2.content
			content[content.index("image/png;base64,") + len("image/png;base64,"):content.index("\" /><br><br><form actio")]

			with open('image_ep52.jpg', 'w+') as f:
				f.write(b64decode(img))




if __name__ == "__main__":
	main()