# 06 Activity: Media Computation lab

## Solving Problems Using Decisions

### Pictures in the Terminal

You can make crude graphics drawings right in the terminal output, without the pillow library. Search the web for "ASCII art" to see lots of creative examples of pictures drawn using terminal text and monospaced-typeface fonts.

Here's some python code that draws a diamond on the terminal screen:

```
space = ' '
char = '#'

diamond = 4 * space + char + '\n'
diamond += 3 * space + 3 * char + '\n'
diamond += 2 * space + 5 * char + '\n'
diamond += space + 7 * char + '\n'
diamond += 9 * char + '\n'
diamond += space + 7 * char + '\n'
diamond += 2 * space + 5 * char + '\n'
diamond += 3 * space + 3 * char + '\n'
diamond += 4 * space + char
print(diamond)
```

```text
    #
   ###
  #####
 #######
#########
 #######
  #####
   ###
    #
```

By changing just one line, we can let the user choose a character to build the diamond:

```
space = ' '
char = input('With what character should I paint your diamond? ')

diamond = 4 * space + char + '\n'
diamond += 3 * space + 3 * char + '\n'
diamond += 2 * space + 5 * char + '\n'
diamond += space + 7 * char + '\n'
diamond += 9 * char + '\n'
diamond += space + 7 * char + '\n'
diamond += 2 * space + 5 * char + '\n'
diamond += 3 * space + 3 * char + '\n'
diamond += 4 * space + char
print(diamond)
```

Unfortunately, the input function doesn't limit the response to just one character, and the diamond doesn't look right if the input is longer than that.

```text
    python
   pythonpythonpython
  pythonpythonpythonpythonpython
 pythonpythonpythonpythonpythonpythonpython
pythonpythonpythonpythonpythonpythonpythonpythonpython
 pythonpythonpythonpythonpythonpythonpython
  pythonpythonpythonpythonpython
   pythonpythonpython
    python
```

Let's use an `if ... elif` selection structure to check the length of the input, and only draw the diamond if the input contains exactly one character:

```
space = ' '
char = input('With what character should I paint your diamond? ')

if len(char) > 1:
    print('Sorry, you typed more than one character. Aborting.')
elif len(char) == 1:
    diamond = 4 * space + char + '\n'
    diamond += 3 * space + 3 * char + '\n'
    diamond += 2 * space + 5 * char + '\n'
    diamond += space + 7 * char + '\n'
    diamond += 9 * char + '\n'
    diamond += space + 7 * char + '\n'
    diamond += 2 * space + 5 * char + '\n'
    diamond += 3 * space + 3 * char + '\n'
    diamond += 4 * space + char
    print(diamond)
```
