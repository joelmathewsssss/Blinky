---
title: Blinky
author: Joel Mathews
description: Voice Actived Desk Lamp
created_at: 2025-07-19
---

Total: 11 Hrs


07/19/25:
1 Hour, 
Thought about hardware projects that would actually benefit my everyday life all day and realized as I was in bed, that I wished I could turn off my favourite desk lamp remotely. I then realized I had a voice active USB LED that I dont use. I realized that this must be my project.
![1000692522](https://github.com/user-attachments/assets/6f3f0cb2-ab60-4ec0-8092-e7df6e2b330d)
![1000692519](https://github.com/user-attachments/assets/00870554-7cb4-4140-8637-392abd33ee64)


7/21/25
2 Hours,
Researching how I can do this, what parts will I need, if I can do this with my Pico. Found that I can use a MOSFET transistor (IRF3708) connecting to the negative wire of the lamp.
![1000692618](https://github.com/user-attachments/assets/b0196283-38f1-4e9f-9141-004115d950e3)


7/24/25
4 Hours,
I spent time drawing up a wiring diagram with my components and rethinking the logic I would use. I originally thought that I can solder directly from my LED to Pico to read if the LED is on, but I tested it with my multimeter I bought for this project and it seems that the LED pins on the USB Voice Module don't have enough of a drop in voltage to register on the Pico, so I'll need to revise my wiring.
![1](https://github.com/user-attachments/assets/2a334570-50ee-46f3-bd19-c018b0d3d3c1)
![IMG_20250729_011208](https://github.com/user-attachments/assets/c97e591d-eb27-4dc1-b74e-456ecee49603)

7/28/25
6 Hours,
Thought about how to get around the problem and realized I could use a more robust system, using a photo resistor instead. The photo resistor will read if the LED is on or off. I updated my diagram for this change and wrote the micro python code that I'll run on my Pico. I also designed a sleeve to hold my photo resistor to the LED on fusion 360. ALso made full circuit assembly in fusion.
![Note Jul 26, 2025](https://github.com/user-attachments/assets/a65ddc37-1bd0-4cfb-9939-1c95062fc962)
<img width="549" height="746" alt="image" src="https://github.com/user-attachments/assets/308fd26f-9366-4699-aba9-e5a6ffdee62d" />
<img width="897" height="767" alt="image" src="https://github.com/user-attachments/assets/b5cb9b0d-6f52-4fad-acfc-d1704b1e430d" />

