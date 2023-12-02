from PIL import Image, ImageDraw
import time
from mandelbrot import mandelbrot, max_iters

#28800 22400

width = int(512)
height = int(512)

re_start = -2 #real
re_end = 1
im_start = -1 #imaginary
im_end = 1 

palette = []

img = Image.new("RGB", (width, height), (0,0,0))
draw = ImageDraw.Draw(img)

def mandel():    
    for x in range(0, width):
        for y in range(0, height):

            c = complex(re_start + (x / width) * (re_end - re_start), 
                        im_start + (y / height) *(im_end - im_start))
            m = mandelbrot(c)
            if m:
                color = 255 - int(m * 255/max_iters) 
            else:
                color = 0 
            r = color
            g = color
            b = color
            draw.point([x,y], (int(r), int(g), int(b)))
            print(f"{x*y} {(x/width)*100}%", end="\r")

start = time.time()

mandel()

end = time.time()

print((end - start)/60, " minutes")

img.show()