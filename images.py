from PIL import Image,ImageFilter

img = Image.open('./pikachu.jpg')

filtered_img = img.convert('L')
#filtered_img = img.filter(ImageFilter.SHARPEN)
#crooked = filtered_img.rotate(180)
resize = filtered_img.resize((300,300))
resize.save("grey.png",'png') #PNG support filter

# .Crop filtered_image by box size 
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png",'png')

print(img)
print(img.format)
print(img.size)
print(img.mode)