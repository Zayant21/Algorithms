from PIL import Image, ImageFilter
before = Image.open("imagename.type")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("newimagename.type")
