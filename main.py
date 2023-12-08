from PIL import Image, ImageDraw
import time
from mandelbrot import mandelbrot, max_iters

width = int(512*2)
height = int(512)

re_start = -2 #real
re_end = 1/2
im_start = -1 #imaginary
im_end = 1

img = Image.new("HSV", (width, height), (0,0,0))
draw = ImageDraw.Draw(img)

def mandel():    
    for x in range(0, width):
        for y in range(0, height):

            c = complex(re_start + (x / width) * (re_end - re_start), 
                        im_start + (y / height) *(im_end - im_start))
            
            m = mandelbrot(c)

            hue = int(255 * m / max_iters)
            saturation = 127
            value = 255 if m < max_iters else 0

            # r = int(hue)
            # g = int(saturation)
            # b = int(value)

            pointColor = (hue, saturation, value)
            draw.point([x,y], pointColor)
            print(f"{(x/width)*100}%", end="\r")

start = time.time()

mandel()

end = time.time()

print(f"generation took {(end - start)/60} minutes")

img.convert("RGB").show()
