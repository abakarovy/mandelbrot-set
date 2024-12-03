from PIL import Image, ImageDraw
import time
import sys
from mandelbrot import mandelbrot, max_iters

args = sys.argv
if len(args) > 3:
    raise Exception(f"expected 2 arguments, got {len(args)}")

width, height = int(args[1]), int(args[2])

if not width > 0 and not height > 0:
    raise Exception(f"Expected integer values larger than 0")

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

            pointColor = (hue, saturation, value)
            draw.point([x,y], pointColor)
            print(f"{(x/width)*100}%", end="\r")

start = time.time()

mandel()

end = time.time()

print(f"generation took {(end - start)/60} minutes")

img.convert("RGB").show()
