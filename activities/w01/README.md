# 01 Activity: Media Computation lab

## Getting Started

### Pillow Library

This semester, most of your coding assignments follow a console application design pattern that follows this sequence:

INPUT >> PROCESS >> OUTPUT

- Input always comes from keyboard entry a line at a time, and
- Output goes to a scrolling text display, usually also a line at a time.

This is a very old application model, dating back several decades to the earliest days of electronic computing machinery. But it isn't the only programming pattern. For these "media computation" labs we will change the pattern slightly as we process graphical images and other media files, instead of just inputting and outputting text. To prepare for these exercises, please install a Python library called "pillow" by following these instructions:

1. In Visual Studio Code, open a terminal.
2. Use Python3's "pip" module to install pillow. Here's the terminal command to do this -- replace [your Python3 command] with whatever path your computer requires:

> `[your Python3 command] -m pip install pillow --user`

- Example: on my Windows computer my Python3 command is `py`, so I typed this:

> `py -m pip install pillow --user`

- Example: on an Apple macOS computer the command is usually `python3`:

> `python3 -m pip install pillow --user`

Figure out what command works for you. Ask for help if you get stuck.

3. Verify the installation. This can be accomplished with this two-line Python program:

```python
from PIL import Image
print('The library was successfully imported')
```

I named my program file `verify_pillow.py` but you can choose a different file name if you want, as long as it ends in `.py`. If you have trouble, please ask your instructor or teaching assistant for help.

### Challenge

Do you have an image file somewhere on your computer? If it has a file format that the pillow library knows about (such as JPG, PNG, GIF, etc.) try this: add a couple of lines to your verify program to make it display your picture. Here's an example that worked for me:

```python
from PIL import Image
print('The library was successfully imported')
picture = Image.open('C:/Users/cgibbons/Pictures/darkside.png')
picture.show()
```

![Darth Jar Jar](darkside.png)

### Interactive Python

Python has an interactive mode. We won't use it often, because we're learning to *write programs*, not just interact with Python.

Sometimes a student accidentally gets stuck inside an interactive Python session and can't figure out what happened. Try this: type your Python command (`py` or `python3` or whatever) by itself and press [Enter]. You will see a "triple angle" prompt that looks like this:

```
>>>
```

That's what Python's interactive mode looks like. If that happens to you, to get back out of interactive mode just type `exit` or `quit` (and if it shows more instructions after you type that, just do what it says).

(Another way to deal with a terminal window that isn't responding to you is to tap the "trash can" button somewhere near the top right of your VS Code terminal pane.)
