# TGH - THE GREAT (DIY) HANDHELD
So this is a project in which i aim to make my own custom retro handheld gaming device with a custom pcb powered by a pi zero 2w.
**BTW NOTE:** so um the case shall be printed from someone who was willing to print it from the slack channel - #printing-legion
#here are some specs - 
**Panelised PCB Dimensions**- 339.82 mm* 102.32 mm
- So the only KiCAD plugin i used was KiKit to panelise the board other than that the full board was designed by me!!! (this is my first major PCB project)

# Firmware- 
So i have made a custom python launcher so basically it runs on top of pi os lite allows one to play games using a controller. Since i have joysticks i needed a way for the software to actually recognise it and allow me to play on it properlly now retropie can do that but making a custom programe just is better. The software detects Game ROM's from the folder ROMS where one can add the Game ROMS depending on the type and the software detects it and allows u to open and play it on the pi as the PI OS LITE has - these great features - RetroArch (emulators) and Auto-start on boot so yes it shall give the perfect handheld feel. 
**Note - You will be unable to play the game ROM's on PC even with the software as the Game ROMS will open on the pi using the in built - RetroArch (emulators). On PC one will only be able to test the controlls using the arrow keys but will need a pi with Pi OS lite to run the games themselves.**

Here are the images of the Python launcher- 
<img width="596" height="380" alt="Screenshot 2026-05-16 101537" src="https://github.com/user-attachments/assets/50ca2aad-e048-461b-80f5-144a3527e523" />
<img width="594" height="373" alt="Screenshot 2026-05-16 101612" src="https://github.com/user-attachments/assets/fedb4bb0-56d2-4fdf-8226-c38b905662e9" />


# Here is the other stuff that i need to make the PCB including the components that are not included in the PCBA from JLC along with the links from where i plan on buying the parts - 
# Bill of Materials (BOM) - The Great (DIY) Handheld:
### Parts & Tools List

| Name | Purpose | Quantity | Total Cost (USD) | Link | Distributor |
|:---|:---|:---:|:---:|:---|:---|
| Isopropyl Alcohol | to clean the board after i solder the components so that the residue flux does not corrode the board slowly. | 1 | 2.69 | [Link](https://www.amazon.in/gp/aw/d/B0DXLCF467/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=c86f6646ab53e02a75d2c7936d94b9e8&hsa_cr_id=0&qid=1778756676&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&aref=ULcGLOQ6dH&ref_=sbx_s_sparkle_sbtcd_asin_0_title&pd_rd_w=HfChB&content-id=amzn1.sym.9269eab1-ae85-443b-9ec2-b2fa4ebaad05%3Aamzn1.sym.9269eab1-ae85-443b-9ec2-b2fa4ebaad05&pf_rd_p=9269eab1-ae85-443b-9ec2-b2fa4ebaad05&pf_rd_r=EFF0ZSWMT934R4D0TNBS&pd_rd_wg=doBkY&pd_rd_r=d02561c6-e886-41f6-b583-cc3dacaa126e&th=1) | Amazon |
| Tactile Push Button Switch Caps Multicolour | To cover the buttons and not hurt fingers. | 1 | 2.31 | [Link](https://www.amazon.in/gp/product/B0DCP7J7R7/ref=ox_sc_act_title_1?smid=AOG7U64E0DVL2&psc=1) | Amazon |
| TP4056 module | To charge | 1 | 0.17 | [Link](https://robu.in/product/tp4056-1a-li-ion-battery-charging-board-micro-usb-with-current-protection-type-c-connector/) | Robu.in |
| Jumper Wires | To connect the daughter Boards to the motherboard and also to connect the 2 pin connector header pin to the TP4056 module. | 1 | 1.63 | [Link](https://www.amazon.in/Electronic-Spices-Jumper-Female-Multicolor/dp/B0CPFCRCHB/) | Amazon |
| Solder | I cant solder witout solder and i have like 1cm or so left as i used the rest before my soldering iron short cicuited. | 1 | 7.75 | [Link](https://www.amazon.in/SONEAK-Solder-Rosin-Electrical-Soldering/dp/B084RZWVXY/) | Amazon |
| Soldering Flux | To help solder and not have cold solder joints. | 1 | 0.83 | [Link](https://www.amazon.in/UNIVERSAL-HUB-Soldering-Electronics-components/dp/B0FV8HHBTN/) | Amazon |
| Soldering Iron | Mine short circuited and i need to solder a buch of stuff on the pcb which i cant without the iron | 1 | 3.02 | [Link](https://www.amazon.in/Temperature-Adjustable-Soldering-Heating-Extra/dp/B0DPVMRTXG/) | amazon |
| Soldering Helping hands | Too see what i am soldering and to help solder properly without burning anything by mistake. | 1 | 5.35 | [Link](https://robu.in/product/te-801-multi-function-led-magnifier-pcb-soldering-iron-stand-holder-table-magnifying-glass-35x-12x-w-2-led-light/) | Robu.in |
| JST SH 2 pin Connector 2mm Pitch | to connect battery and also robu.in has a min order of 10 rupees or 0.10 usd for each component hence i had to add 9 in qty but it is still cheaper than others | 9 | 0.11 | [Link](https://robu.in/product/jst-sh-2-pin-connector-2mm-pitch/) | Robu.in |
| Mini HDMI To HDMI Cable | to connect pi to display | 1 | 1.3 | [Link](https://robu.in/product/mini-hdmi-hdmi-cable-1-8-meter-round-high-quality-copper-clad-steel-black/) | Robu.in |
| 40mm 8Ω (ohm) 0.5Watt Power Audio Speaker - Multicolor | to produce sound | 1 | 1.66 | [Link](https://www.amazon.in/Electronic-Spices-Wired-Sound-Speakers/dp/B07MTK843Z) | amazon |
| PS2 joystick module | Left and right joystick | 2 | 0.79 | [Link](https://www.flyrobo.in/ps2_game_joystick_module_for_arduino) | FlyRobo |
| 4000mAh 3.7V Micro LiPo Battery pack | To power the device | 1 | 5.64 | [Link](https://robu.in/product/nova-955465-4000mah-3-7v-lipo-battery-pack/) | Robu.in |
| 100 uF 10V Through Hole Electrolytic Capacitor | headphone blocking on PCB (Note: min order requirement included in qty) | 8 | 0.12 | [Link](https://robu.in/product/100-uf-10v-through-hole-electrolytic-capacitor-pack-of-20/) | Robu.in |
| 6mm Tactile Push Button Switch 6x6 (Pack of 10) | For buttoning | 1 | 0.14 | [Link](https://robu.in/product/6x6x5-tactile-push-button-switch/) | Robu.in |
| Slide switch SPDT | To switch on the device | 2 | 0.17 | [Link](https://robu.in/product/1-month-warranty-805/) | Robu.in |
| 1x5 2.54mm Female Right Angle Single Row Header Strip | For Connecting the left and right joystick Modules | 2 | 0.26 | [Link](https://www.sunrom.com/p/1x5-254mm-female-right-angle-single-row-header-strip) | sunrom.com |
| 1x2 male pin header 2.54mm | For connecting the TP4056 module and supplying power to display/speaker | 5 | 0.11 | [Link](https://robu.in/product/a2541wv-2p-9t-cjt-1x2-pin-2-54mm-180-single-row-pin-header-rohs/) | Robu.in |
| 2.54MM 2x20 Pin Female Double Row Straight Long Header Strip | To connect the Pi to the PCB | 1 | 0.86 | [Link](https://robu.in/product/2-54mm-2x20-pin-female-double-row-straight-long-header-strip/) | Robu.in |
| 5 Inch Touch Screen HDMI Interface | THE SCREEN To See what i am playing | 1 | 26.09 | [Link](https://robu.in/product/5-inch-touch-screen-hdmi-interface-display-module-tft-lcd-800x480-raspberry-pi-2-model-b-touch-pen) | Robu.in |
| Raspberry Pi Zero 2W | This is basically the Brain of the device | 1 | 18.81 | [Link](https://robu.in/product/raspberry-pi-zero-wireless-wh-pre-soldered-header) | Robu.in |
| PCBA for bottom SMD components on PCB | PCB SMD component assembly service | 2 | 14.15 | [Link](https://jlcpcb.com) | JLCPCB |
| PCB (Motherboard, and both daughter boards) | Custom PCBs to hold all components | 5 | 5.37 | [Link](https://jlcpcb.com) | JLCPCB |
| TOTAL- 199.44 USD | TAX- 2 USD || SHIPPING - 21.31 USD |||








# _____________________________________________________________________________________________________________________
- So i plan on using JLCPCB to actually get my boards manufactured and i will be using PCBA for the bottom SMD components
# _____________________________________________________________________________________________________________________

# NOTE FOR The CAD model -
**it has spacers that i will attatch the pcb to. The spacers are a little big as i can cut them if they are too big but cant do anything if they are too small so hence the spacers on the bottom case are 9mm in height as i can cut them as needed.** 

# BTW HERE ARE SOME PICS OF THE PCB THAT I TOOK THROUGHOUT DESIGNING IT(PCB and CAD CASE MODEL<img width="959" height="539" alt="Screenshot 2026-05-16 121953" src="https://github.com/user-attachments/assets/27385dfd-7aac-427e-ace4-fc55b9ab69fc" />
<img width="520" height="233" alt="Screenshot 2026-05-16 123145" src="https://github.com/user-attachments/assets/03c8cef9-d0f8-40bd-a7da-b712e0eb5b96" />
)- 
<img width="533" height="220" alt="Screenshot 2026-05-10 230008" src="https://github.com/user-attachments/assets/07351982-c047-4389-aff6-f1acf80b013c" />
<img width="795" height="300" alt="Screenshot 2026-05-09 170451" src="https://github.com/user-attachments/assets/d3c5e589-1971-4ace-8ef0-f19d54ade833" />
<img width="793" height="347" alt="Screenshot 2026-05-09 165009" src="https://github.com/user-attachments/assets/2fd9378b-740e-40db-beeb-ff2c1fc88893" />
<img width="722" height="238" alt="Screenshot 2026-05-09 164731" src="https://github.com/user-attachments/assets/7919f3ed-ffe4-4e6f-bf32-dd36c344b107" />
<img width="354" height="302" alt="Screenshot 2026-05-09 163952" src="https://github.com/user-attachments/assets/7560b851-7067-440e-bd96-9815e528fb82" />
<img width="591" height="307" alt="Screenshot 2026-05-09 162141" src="https://github.com/user-attachments/assets/caa44fb4-8e67-4365-84b5-602e523d2dbf" />
<img width="797" height="406" alt="Screenshot 2026-05-09 135802" src="https://github.com/user-attachments/assets/7b6ab872-daa7-4a54-b1f2-7dee7b510b91" />
<img width="800" height="440" alt="Screenshot 2026-05-08 181919" src="https://github.com/user-attachments/assets/3f739e95-050e-4902-926e-c2a0a8b94d33" />
<img width="689" height="340" alt="Screenshot 2026-05-08 181737" src="https://github.com/user-attachments/assets/db1eb948-331f-4e75-b27f-56d3c52fbf0e" />
<img width="476" height="242" alt="Screenshot 2026-05-08 181207" src="https://github.com/user-attachments/assets/e4d4ba49-dd32-4d69-93c2-a37ed84d5858" />
<img width="770" height="297" alt="Screenshot 2026-05-11 143934" src="https://github.com/user-attachments/assets/455fa56f-c145-4298-a841-3849336d20df" />
<img width="959" height="539" alt="Screenshot 2026-05-12 155912" src="https://github.com/user-attachments/assets/a4b4cce1-aa40-4764-9c79-e5f9145d9b48" />
<img width="770" height="297" alt="Screenshot 2026-05-11 143934" src="https://github.com/user-attachments/assets/409ad3ac-eea5-4b20-bd2c-a0910abd4d9e" />
<img width="533" height="220" alt="Screenshot 2026-05-10 230008" src="https://github.com/user-attachments/assets/ea0f5e50-8d48-49e9-8dea-8453b47f788c" />
<img width="795" height="300" alt="Screenshot 2026-05-09 170451" src="https://github.com/user-attachments/assets/3a21f371-d6ca-48ae-9128-9193d4ba2929" />
<img width="793" height="347" alt="Screenshot 2026-05-09 165009" src="https://github.com/user-attachments/assets/dc3d57c0-45b3-4213-9b85-4dc0505ee023" />
<img width="722" height="238" alt="Screenshot 2026-05-09 164731" src="https://github.com/user-attachments/assets/298b5716-0e93-4845-abad-82f214f5c102" />
<img width="354" height="302" alt="Screenshot 2026-05-09 163952" src="https://github.com/user-attachments/assets/3dce5168-8cd6-4e82-9fb3-fa08a704870c" />
<img width="591" height="307" alt="Screenshot 2026-05-09 162141" src="https://github.com/user-attachments/assets/4266252d-6c95-447e-803f-ca6e75e54b09" />
<img width="797" height="406" alt="Screenshot 2026-05-09 135802" src="https://github.com/user-attachments/assets/849a477f-b9e6-415d-9d3b-e3ec8678bc85" />
<img width="800" height="440" alt="Screenshot 2026-05-08 181919" src="https://github.com/user-attachments/assets/d8e0fc3b-99f9-4baa-9c8e-de6c7f63b91d" />
<img width="689" height="340" alt="Screenshot 2026-05-08 181737" src="https://github.com/user-attachments/assets/600eccb3-601b-4d82-814d-235f6ff7b1ff" />
<img width="476" height="242" alt="Screenshot 2026-05-08 181207" src="https://github.com/user-attachments/assets/c514bf2b-1438-4296-9809-de0209222177" />
<img width="959" height="539" alt="Screenshot 2026-05-12 155945" src="https://github.com/user-attachments/assets/7b81df71-cd8d-4bd0-ac16-8754970a15b1" />
<img width="748" height="476" alt="image" src="https://github.com/user-attachments/assets/cf7e77a1-3f0b-48f9-a412-a73bc8be4371" />
<img width="331" height="233" alt="image" src="https://github.com/user-attachments/assets/0330da81-b8cb-4026-9ec7-34858598c57d" />
<img width="303" height="341" alt="image" src="https://github.com/user-attachments/assets/4c7e0e76-06d4-4b56-8a6b-0bebd8b183ed" />

