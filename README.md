# MacroBoard

## Features:
- 6 Keys
- Customizable config without having to change the firmware (technically)
- USB-C
- Powered by a XIAO-RP2040

## CAD:

My case was made using **AutoDesk Fusion Personal.** I started out with making the bottom of the case, and then the top, and that ended in a faliure. So I went ahead and redesigned the entire board, including the PCB and wound up with this!

![cad](https://github.com/user-attachments/assets/6313bf8c-0603-4936-99c1-c3ac9fbeb0c7)


## PCB:

My PCB was made in KiCad 9, and I decided to add some personal *flair* to the PCB, aswell as the Hack Club logo for *obvious* reasons.

![Screenshot 2025-06-28 111006](https://github.com/user-attachments/assets/1d2beadc-fedc-46ee-aad0-ba6e5554483d)


![Screenshot 2025-06-28 111019](https://github.com/user-attachments/assets/f3f360bd-ca75-4593-819d-224a75051f1d)

***Here's the model with some of the parts placed in too!***

![someparts](https://github.com/user-attachments/assets/1ae58967-ae85-443c-899a-83bc3c4d1e7a)

## Firmware:
I haven't worked on the firmware, pretty much at all, just because I would have zero way to test, my current changes are loading the keymapping via a json file, so no laggy IDE's have to be open everytime. I'm hoping to soon make a GUI for changing the json easier.

Once I have my MacroBoard assembled physically, I will continue making the firmware, but for now, it'll stay in it's current state :)

## BOM:
- Seeed XIAO RP2040
- MX-Style switches (6x)
- SK6812 MINI-E LEDs (2x)
- Blank DSA keycaps (6x)
- M3x16mm screws
- M3x5mx4mm heatset inserts
