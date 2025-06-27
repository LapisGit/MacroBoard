# MacroBoard

## Features:
- 6 Keys
- Customizable config without having to change the firmware (technically)
- USB-C
- Powered by a XIAO-RP2040

## CAD:

My case was made using **AutoDesk Fusion Personal.** I started out with making the bottom of the case, and then the top, and that ended in a faliure. So I went ahead and redesigned the entire board, including the PCB and wound up with this!

![cad](https://github.com/user-attachments/assets/1067523d-bb8b-42d3-b1ad-b1e1a1852abe)

## PCB:

My PCB was made in KiCad 9, and I decided to add some personal *flair* to the PCB, aswell as the Hack Club logo for *obvious* reasons.

![pcb](https://github.com/user-attachments/assets/36fb2947-64ea-49b6-99dc-8c1e01328610)


![schematic](https://github.com/user-attachments/assets/94e80910-016a-4c44-97fa-2f5c5305c093)


***Here's the model with some of the parts placed in too!***

![someparts](https://github.com/user-attachments/assets/0b67986d-20c0-4ac6-bd12-6c6c101d0d9b)

## Firmware:
I haven't worked on the firmware, pretty much at all, just because I would have zero way to test, my current changes are loading the keymapping via a json file, so no laggy IDE's have to be open everytime. I'm hoping to soon make a GUI for changing the json easier.

Once I have my MacroBoard assembled physically, I will continue making the firmware, but for now, it'll stay in it's current state :)

## BOM:
Seeed XIAO RP2040
MX-Style switches (6x)
SK6812 MINI-E LEDs (2x)
Blank DSA keycaps (6x)
M3x16mm screws
M3x5mx4mm heatset inserts
