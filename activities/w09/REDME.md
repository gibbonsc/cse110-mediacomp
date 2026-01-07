# 09 Activity: Media Computation lab

## Lists

### Drawing Polygons

Some of the "drawing context" tools of pillow's `ImageDraw` module use a list parameter. Here's a program to draw a five-pointed star. It does so by sending a `polygon()` message to the drawing context. The corners of the shape are programmed as a list of ten x,y coordinates:

```python
from PIL import Image, ImageDraw
img=Image.new('RGB', (200,200))
context=ImageDraw.Draw(img)

star_vertices = [100,4, 116,76, 188,68, 132,108, 156,180, 100,132, 44,180, 68,108, 12,68, 84,76]
context.polygon(star_vertices, fill='white')
img.show()
```

The Python interpeter doesn't really care about how list elements are spaced in your code. In this program, the extra space after every y-coordinate in the list helps keep it organized, for the benefit of humans reading or reviewing the code.

![star](star.gif)

## Challenge

Think of another polygon shape you like. Figure out the `x,y` coordinates of the corners of that shape. Then try to draw it in a different color on this picture, so that it appears layered atop the star. If you can, also make a picture that makes it appear behind the star.
