# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#Raspberry_Pi_Assignment_Template)
* [Onshape_Assignment_Template](#Onshape_Assignment_Template)
* [Pico Introduction](#Pico_Introduction)
* [Launchpad Part 1](#LaunchpadPart1)
* [Launchpad Part 2](#LaunchpadPart2)
* [Launchpad Part 3](#LaunchpadPart3)
* [Launchpad Part 4](#LaunchpadPart4)
&nbsp;

## Pico Introduction

### Assignment Description

Make the onboard LED blink indefinitly.

### Evidence 

![Blink LED](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/3462a996b2eeadcb00cb28079f79c7d27fd154db/images/ezgif-4-b8aa48933f.gif).

### Wiring

No wiring needed. 

### Code

[Pico Intro Code](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/a06cbe858f5325202adc689f890c5aeca1bd5031/raspberry-pi/LED_blink.py).

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

![Launchpad 2 Wiring Drawing](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/77326cba3618811c08de93ec3fce038bfa62e793/images/image0.jpeg)  

### Code

[Launchpad Part 2 Code](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/a06cbe858f5325202adc689f890c5aeca1bd5031/raspberry-pi/launchpad2.py).

### Reflection

I took this assignment very slow, because I didn't motivate myself to truly think about what I was doing, and just zoned out until I was offered help. That won't be happening anymore. The big thing I had a problem with was the second LED, because I didn't realize it was as simple as putting a 2 at the end of it.

## Launchpad Part 3

### Assignment Description

Make Launchpad 2 work when a push button is pressed. 

### Code 

[Launchpad Part 3 Code](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/a06cbe858f5325202adc689f890c5aeca1bd5031/raspberry-pi/launchpad3.py).

### Wiring

![Wiring](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/25d73a883c4e8b7e1fa21f4d1cd16303c1e65339/images/image0%20(1).jpeg)

### Evidence

![LaunchPad 3](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/25d73a883c4e8b7e1fa21f4d1cd16303c1e65339/images/Lunchpad3.gif)  

### Reflection

The wiring for the button was much more simple than I thought it would be, with only two wires and my LEDs positioning being a little bit different. I had everything I needed for my code, but I just needed to but them together in the right order and take my red LED out of my "if true" function. I also had a bad button at the beginning of the assignment, so it wouldn't work even when the code was right.

## Crash Avoidence 1

### Assignment Description

We had to wire and code a accelerometer, and have it return x, y, and z axes on the serial monitor. 

### Wiring

![Wiring](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/8abd39259cf7b85572dd580be2fdaa84f732f70d/images/image0%20(2).jpeg). 

### Evidence

![Crash Avoidence 1](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/392635e3cf613f8fd375e0e01cdf3363ec021379/images/Crash%20Avoidence%201.gif). 

### Code

[Crash Avoidence 1 Code](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/392635e3cf613f8fd375e0e01cdf3363ec021379/raspberry-pi/crashavoidance1.py). 

### Reflection

This assignment went much faster than the ones in the past, because I changed my mindset and have been able to take healthy breaks. The biggest help for this assignment was the bit of code I found that I was able to modify to fit the this assignment. 

## Crash Avoidence 2

### Assignment Description

We had to wire and code a accelerometer, and have it return x, y, and z axes on the serial monitor. We then make an LED turn on when it reches 90 degrees, and off when its no longer 90.

### Wiring

![Wiring](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/8abd39259cf7b85572dd580be2fdaa84f732f70d/images/image0%20(2).jpeg). 

### Evidence

![Crash Avoidence 2](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/9b5c7775aac40f9d3aaf9460bd1638e22e5eec97/images/ezgif-2-6e5c730d73.gif). 

### Code

[Crash Avoidence 2 Code](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/5a35ad9bb4ac099139cdebdd17e742fa8783c2ed/raspberry-pi/crashavoidance2.py). 

### Reflection

I had almost all the knowledge I needed to do this assignment, except for one key piece. I did not know how to issolate just the "Z" in mpu.acceleration. I asked Mr. Miller and he explained that it was like numbers, and Z was number 2. So I was able to Issolate and put an if statement on it, saying if Z is below 0, then turn on the LED. If Z is above 0, then keep LED off. 

## Crash Avoidence 3

### Assignment Description

We had to wire and code a accelerometer, and have it return x, y, and z axes on the serial monitor. We then make an LED turn on when it reches 90 degrees, and off when its no longer 90. Now you will add an onboard OLED screen to print live angular velocity values.
 
### Evidence 

![Crash Avoidence](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/313030343be63a21fc5e1c4afd14c3878c4f1db5/images/197930777-1497afab-6583-4bb5-b642-9440d67a251c.gif)

### Wiring

![Crash Avoidence 2](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/d3b36089335dc7114dcd764a1e850e65f6310a3f/images/Crash3.png).

### Code

[Crash Avoidence 3](https://github.com/Graham913/Engineering_4_Notebook/blob/7208b914c25832910204bc5fe51eefe4c7533c29/crash2.py).

### Reflection

wooooooooooooo

## Landing Area 1

### Assignment Description

Write a script that takes three coordinates and returns the area using a function

### Evidence 

![Landing Area 1](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/ed6efaa2795a91eda77a2d0836d38a7ba1c5db31/images/197931058-1bb237e0-489f-4738-b142-33b491400871.gif)

### Wiring

none

### Code

[Landing Area 1Code](https://github.com/Graham913/Engineering_4_Notebook/blob/7208b914c25832910204bc5fe51eefe4c7533c29/landingarea.py).

### Reflection

woooooooooooooooooooooo

## Landing Area 2

### Assignment Description

You have successfully written a script to calculate and return the area of each triangle. Now, your commander has asked that you include a small OLED screen to improve visualization of where the landing area is relative to the base.

### Evidence 

![Landing Area 2]()

### Wiring

woooooooooooooooooooooooo

### Code

[Landing Area 2 Code]().

### Reflection

woooooooooooooooooooooooooooo

## Morse Code 1

### Assignment Description

Write a morse code translator. This piece of code will translate text from the user into a set of dots and dashes. Print those dots and dashes to the serial monitor.

### Evidence 

![Morse Code 1]()

### Wiring

woooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

### Code

[Morse Code 1 Code]().

### Reflection

wooooooooooooooooooooooooooooooooooooo

## Morse Code 2

### Assignment Description

Now that you have a script that translates English into Morse Code, let’s add to it! You need to have your Pico flash out your Morse Code message using an LED.

### Evidence 

![Morse Code 2]()

### Wiring

woooooooooooooooooooooooooooooooooooooooooooooooooooooooo

### Code

[Morse Code 2 Code]().

### Reflection

wooooooooooooooooooooooooooooooooooooooooooooooooooooo lets gooooooooooooooooooooooooooooo

## Onshape_Assignment_Template

### Assignment Description

Each time the serial monitor prints a new number, blink a red LED. Once the countdown reaches Liftoff, turn on a green LED (not the onboard LED) and leave it on.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
 [test.pi](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/main/raspberry-pi/test.py)
### Test Image
![Burger Turtle](images/TurtleBurger.jfif)  
### Test GIF
![Picture Name Here](https://github.com/AnthonyMedina3654/Engineering_4_Notebook/blob/main/images/Dance.gif?raw=true)  
