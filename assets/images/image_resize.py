from PIL import Image
img = Image.open('amsterdam.png')
img.thumbnail((1300,2000))
img.save('amster.png')
