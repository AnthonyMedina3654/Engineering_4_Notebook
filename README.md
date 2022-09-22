# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#Raspberry_Pi_Assignment_Template)
* [Onshape_Assignment_Template](#Onshape_Assignment_Template)

&nbsp;

## Pico Introduction

### Assignment Description

Make the onboard LED blink indefinitly.

### Evidence 

![Blink LED](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/3462a996b2eeadcb00cb28079f79c7d27fd154db/images/ezgif-4-b8aa48933f.gif).

### Wiring

No wiring needed. 

### Code

[Pico Intro Code]().

### Reflection

very easy assignment, was able to find a site with exactly what i needed.  

## Launchpad Part 1

### Assignment Description

In Launch Pad Part 1, you need to make a countdown from 10 seconds down to Liftoff (at 0 seconds). That countdown must be printed to the serial monitor in VS Code.

### Evidence 

![Countdown](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/abcac30f267bf01eaf861d7e6ab640e1989f2bf6/images/ezgif-4-6daeb68d3f.gif)

### Wiring

No wiring for this assignment.

### Code

[Launchpad Part 1 Code](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad1.py).

### Reflection

This Function will be very useful for me in the future, the ability to count down is very important. I had the time.sleep in the wrong place and was confused why it wasn't working, until Mr: Miller helped me understand why it needs to be in the loop and not seperate. 

## Launchpad Part 2

### Assignment Description

In Launch Pad Part 2, you need to make a countdown from 10 seconds down to Liftoff (at 0 seconds). That countdown must be printed to the serial monitor in VS Code. A green light should blink throughout the countdown, then a red light is turned on until liftoff

### Evidence 

![Countdown+LED Blink](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/4217ac6e8c316182bb8462d92f958a942b95f084/images/ezgif-2-4109dd0a23.gif)

### Wiring

No wiring for this assignment.

### Code

[Launchpad Part 1 Code]().

### Reflection

This Function will be very useful for me in the future, the ability to count down is very important. I had the time.sleep in the wrong place and was confused why it wasn't working, until Mr: Miller helped me understand why it needs to be in the loop and not seperate. 


## Onshape_Assignment_Template

### Assignment Description

Each time the serial monitor prints a new number, blink a red LED. Once the countdown reaches Liftoff, turn on a green LED (not the onboard LED) and leave it on.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

## Launchpad 2

### Assignment Description

Each time the serial monitor prints a new number, blink a red LED. Once the countdown reaches Liftoff, turn on a green LED (not the onboard LED) and leave it on.

### Code 

```python

import time
import board
import digitalio
led = digitalio.DigitalInOut(board.GP21)
led2 = digitalio.DigitalInOut(board.GP22)
led.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
for x in range(10, 0, -1):
    print(x) 
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
led2.value = True
time.sleep(10)

```


### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

yes

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
 [test.pi](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/main/raspberry-pi/test.py)
### Test Image
![Burger Turtle](images/TurtleBurger.jfif)  
### Test GIF
![Picture Name Here](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/main/images/Dance.gif?raw=true)  
