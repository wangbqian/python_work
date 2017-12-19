# from PIL import Image

# im = Image.open('pillowpg.jpg')

# w,h = im.size
# print('Original image size: %s * %s' %(w,h))

# im.thumbnail((w//2,h//2))
# print('Resize image to %s * %s ' %(w//2,h//2))

# im.save('thumbnail.jpg','jpeg')

#--------图片剪辑--------#

# from PIL import Image,ImageFilter
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')

#--------图片模糊-------------#

from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random

#随机字母：

def rndChar():
    return chr(random.randint(65,90))

#随机颜色1：
def rndColor():
    return (random.randint(152,224),random.randint(116,251),random.randint(184,249))


def rndColor2():
    return (random.randint(251,254),random.randint(240,251),random.randint(196,251))

#240*60
width = 60*4
height = 60

image = Image.new('RGB',(width,height),(255,255,255))

font = ImageFont.truetype('Arial.ttf',36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y), fill = rndColor())


for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(),font = font,fill = rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')

