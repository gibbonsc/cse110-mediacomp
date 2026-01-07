# 05 Activity: Media Computation lab

## Decisions

### Save and Select Pictures

There are `save()` and `open()` methods in the pillow library for storing images in files and retrieving them later.

By changing the last line of our "smiling robot face" code, it's easy to save that drawing to a file:

```python
from PIL import Image, ImageDraw
# prepare an image and its drawing context
img=Image.new('RGB', (120,90))
context=ImageDraw.Draw(img)

# draw robot's mouth, nose, and eyes
context.rectangle([10,50,110,80], fill='blue', outline='yellow')
context.rectangle([50,35,70,55], fill='blue', outline='yellow')
context.rectangle([15,10,45,30], fill='red', outline='yellow')
context.rectangle([75,10,105,30], fill='red', outline='yellow')

# save the result
img.save("robot_smile.jpg")
```

Here's a similar program that draws and saves a picture of a three-leaf clover:

```python
from PIL import Image, ImageDraw
# prepare an image and drawing context
img2=Image.new('RGB', (100,100))
context2=ImageDraw.Draw(img2)

# draw a clover's stem and petals
context2.rectangle([45,50,55,90], fill='green', outline='black')
context2.ellipse([10,30,50,70], fill='green', outline='black')
context2.ellipse([30,10,70,50], fill='green', outline='black')
context2.ellipse([50,30,90,70], fill='green', outline='black')

# save the result
img2.save("clover.jpg")
```

After running these programs to draw and save those imgages, we can write code to retrieve and use them. Here's a python program that uses an `if ... else` decision structure to decide which picture to display:

```python
from PIL import Image

# Ask the user to choose yes or no, then retrieve a file depending on the response.
response = input('Would you like to see a friendly robot face? (y/n) ')
if response.lower() == 'y':
    print('Very well, here comes a smiling robot to greet you.')
    selected_pic = Image.open("robot_smile.jpg")
else:
    print('Okay, please accept this clover instead with my compliments.')
    selected_pic = Image.open("clover.jpg")

# display whichever file was chosen
selected_pic.show()
```

### Challenge

As you work on your "Adventure Game" program, it might be fun to include code that draws and saves an illustration of one of the situations in the game, then opens and displays that drawing if a player inputs the choices that lead to that situation.
