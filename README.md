# AlHeprin--Driver-Drowsiness-Detecion 

This repository contains AlHeprin-Driver-Drowsiness-Detecion Prject with a GUI made using Tkinter.

Inspired from person named 'AlHeprin' who spent his entire lifetime with out sleeping.

AlHeprin besides alerting driver,this can be used to record travel dairies.

Videos will be saved in desired directory, so that they can be used for future purpose ( if something un expected happens)

## Requirements
--->numpy\
--->opencv\
--->playsound\
--->time\
--->tkinter

This conisists of a python file 'AlHeprin.py'

This file contains python code for generating detecting eyeblink.

We will use custom eyeblink haarcascade files for eye blink detection

GUI is completely developed using Tkinter.

## Running/Usage

Open commandprompt and change direcrtory to project nad run'AlHeprin.py'.
this will open a GUI which consists of 3 buttons.\
1.Record Vlog\
2.Start Detection\
3.EXIT

#### Record Vlog
When we click on Record Vlog, then this will record a video and save in the project directory.

#### Start Detection
When we click on Start Detection button, It will access the camera and will start recording. Drivier tries to sleep, then AlHeprin detects and plays a big beep sound to alert the driver and passenger. The detected video will aso be saved.

#### Exit
When we click on exit button then AlHeprin will get destroyed( Closed).
