from PIL import Image,ImageTk
for i in range(10):
	img =Image.open(f"{i+1}.jpg")
	img.thumbnail((300,400))
	img.save(f"resized_{i+1}.jpg")
