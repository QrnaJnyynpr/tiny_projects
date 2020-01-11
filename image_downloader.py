import requests

image_url = input("\nPlease enter the URL of the image you would like to download:\n")

r = requests.get(image_url)

with open(r'image.png', 'wb') as f:
	f.write(r.content)