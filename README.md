# SimpleGraphics
A small wrapper for Pygame to make things easier!

# How To
Your Python program needs to be structured like this:
```python
import SimpleGraphics

def Create():
    return
def Update(elapsed):
    return
def OnKeyPress(elapsed, key):
    return
def OnKeyPressed(elapsed, key):
    return
def OnKeyRelease(elapsed, key):
    return
def Draw(elapsed):
    return
def OnMouseMove(elapsed, x, y):
    return
def OnExit(elapsed):
    return

SimpleGraphics.Run(800, 600, 800, 600, Create, Update, Draw, OnKeyPress, OnKeyPressed, OnKeyRelease, OnMouseMove, OnExit)
SimpleGraphics.Quit()
```

## 1. The functions to provide
The ```Create()``` function is called right on initialisation. You may initialise resources, global variables, and so on here.<br>
The ```Update(elapsed)``` function is called every frame. The "elapsed" argument is the time in milliseconds since the last frame.<br>
The ```OnKeyPress(elapsed, key)``` function is called when a key is pressed. See the key table below for the values for ```key```<br>
The ```OnKeyPressed(elapsed, key)``` function is called when a key REMAINS pressed.<br>
The ```OnKeyRelease(elapsed, key)``` function is called when a key is released.<br>
The ```Draw(elapsed)``` function is called every frame, after ```Update```. This is where your drawing commands must go.<br>
The ```OnMouseMove(elapsed, x, y)``` function is called when there is mouse movement detected, with x and y being the coordinates of the mouse pointer.<br>
The ```OnExit(elapsed)``` function is called when the user quits the run.<br>

## 2. Initialisation
The main game loop is provided by ```SimpleGraphics.Run(screen_width, screen_height, window_width, window_height, create_function, update_function, draw_function, onkeypress_function, onkeypressed_function, onkeyrelease_function, onmousemove_function, onexit_function)```. The following arguments are expected to be given to this function:
* screen_width: This is the height dimension of the screen you wish to draw on.
* screen_height: This is the width dimension of the screen you wish to draw on.
* window_width: This is the window width. After you draw on the screen, your program's graphical output will be copied to the window and rendered there. 
* window_height: This is the window height. Same as above.<br>
Note: <i>It may not seem obvious for the choice of asking the user two different screen dimensions, but it proves very useful. Suppose you want to render on a 320x240 screen, but your display is very large,
to accomdate for this, you may choose 320x240 as screen_width and screen_height, but instead choose something like 960x720 as the window_width and window_height. Effectively, the rendered image would be stretched
and then output to the window buffer.</i>
* ```create_function, update_function, draw_function, onkeypress_function, onkeypressed_function, onkeyrelease_function, onmousemove_function, onexit_function```: See <b>(1)</b>.

## 3. The Function List

* ```IsPressed(key)```: Returns if key is pressed. ```key``` must be a value which is prefixed by ```SimpleGraphics.BTN_```. For simplicity, only UP, DOWN, LEFT, RIGHT, Z, X, C, SHIFT, CTRL and ENTER are supported.
* ```SetCaption(string)```: Sets string as the window caption.
* ```GetHeight()```: Returns the <b>screen</b> height.
* ```GetWidth()```: Returns the <b>screen</b> width.
* ```Clear(r,g,b)```: Clears the screen with color as described by (r,g,b) values.
* ```PutPixel(x,y,r,g,b)```: Puts pixel at screen coordinates (x,y) with color (r,g,b).
* ```DrawCircle(x, y, radius, r, g, b, filled = false, linewidth = 1)```: Draws a circle with center at (x,y) with radius "radius", and color (r,g,b). If "filled" is set to True (false by default), then circle draw is filled with color (r,g,b). The linewidth parameter is used when filled is set to False, and it is the thickness of the border of the empty circle.
* ```DrawTriangle(x1, y1, x2, y2, x3, y3, r, g, b, filled = False, linewidth = 1)```: Draws a triangle with coordinates (x1,y1), (x2,y2), (x3,y3) as points. Rest two parameters are same as above.
* ```DrawBlock(x, y, w, h, r, g, b, filled = False, linewidth = 1)```: Draws a block with top left corner at (x,y) and width "w" and height "h" with color (r,g,b). Rest two parameters are same as above.
* ```DrawLine(x1, y1, x2, y2, r, g, b, linewidth=1)```: Draws a line from (x1, y1) to (x2, y2) on the screen of color (r,g,b). linewidth parameter same as above.
* ```LoadImage(file)```: "file" is the file name of the image to load. Returns an ```Image``` class.
* ```DuplicateImage(img)```: "img" is the ```Image``` class returned by either LoadImage or a previous DuplicateImage. Duplicates an image, and returns an independent "Image" class.
* ```DrawImage(img, x, y)```: Draws the image to screen with it's top left corner placed on (x,y).
* ```CropImage(img, x, y, w, h)```: Crops the given image, with the top left of the crop selection at (x,y) on the image, and width "w" and height "h". Returns a fresh image class containing the cropped version of the image.
* ```MakeTransparentImage(img, r, g, b)```: Removes color (r,g,b) from image. Returns a fresh image class.
* ```ResizeImage(img, w, h)```: Resizes the given image to dimensions w x h. Returns a fresh image class.
* ```DrawString(string, x, y, r, g, b)```: Draws the given string at (x,y) on the screen with color (r,g,b).
* ```FrameCap(fps)```: Limits the frame rate of the program. Should be called at the end of Draw() if one wishes to limit the FPS to say, 30 or 60. "fps" is the limiting frames per second.
* ```Quit()```: Closes the application.


