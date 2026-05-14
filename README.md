# TGH - THE GREAT (DIY) HANDHELD
So this is a project in which i aim to make my own custom retro handheld gaming device with a custom pcb powered by a pi zero 2w.
**BTW NOTE:** so um the case shall be printed from someone who was willing to print it from the slack channel - #printing-legion
#here are some specs - 
**Panelised PCB Dimensions**- 339.82 mm* 102.32 mm
- So the only KiCAD plugin i used was KiKit to panelise the board other than that the full board was designed by me!!! (this is my first major PCB project)
Here are all the components of the PCB from the BOM i generated from KiCAD -
## Bill of Materials From KICAD (BOM):
### Panel Components (PCB Parts)

| Qty | Component / Value | Designators | Footprint |
|:---:|:------------------|:------------|:----------|
| 1 | Conn_01x02 | Battery_3.7V1 | PinHeader_1x02_P2.54mm_Vertical |
| 1 | 22µF | C3 | C_0805_2012Metric |
| 1 | 22uF | C4 | C_0805_2012Metric |
| 1 | 10uF | C5 | C_0805_2012Metric |
| 1 | 100nF | C6 | C_0402_1005Metric |
| 2 | 100µF | C7, C8 | CP_Radial_D6.3mm_P2.50mm |
| 1 | 1N5819 | D3 | D_SOD-123 |
| 1 | Conn_02x20 (Odd/Even) | J1 | PinHeader_2x20_P2.54mm_Vertical |
| 1 | TP4056_Module | J2 | PinHeader_1x02_P2.54mm_Vertical |
| 1 | Joystick_Left | J3 | PinSocket_1x05_P2.54mm_Horizontal |
| 1 | Joystick_Right | J4 | PinSocket_1x05_P2.54mm_Horizontal |
| 1 | Display_5V | J5 | PinHeader_1x02_P2.54mm_Vertical |
| 1 | Speaker | J6 | PinHeader_1x02_P2.54mm_Vertical |
| 1 | AudioJack3_3.5mm | J7 | Jack_3.5mm_CUI_SJ-3523-SMT_Horizontal |
| 2 | Connector Left Board | J10, J13 | PinHeader_1x12_P1.00mm_Vertical |
| 1 | Connector Right Board | J11 | PinHeader_1x12_P1.00mm_Vertical |
| 1 | Connector Right Board | J12 | PinHeader_1x12_P1.00mm_Vertical |
| 1 | Joystick Module (L) | JM1 | Joystick Module 40x27mm |
| 1 | Joystick Module (R) | JM2 | Joystick Module 40x27mm |
| 1 | 22uH | L1 | L_Bourns_SRR1260 |
| 1 | 100k Resistor | R4 | R_0402_1005Metric |
| 1 | 33k Resistor | R5 | R_0402_1005Metric |
| 14| 10k Resistor | R6-15, R22-23, R28-29 | R_0402_1005Metric |
| 2 | 5.1k Resistor | R16, R17 | R_0402_1005Metric |
| 2 | 4.7k Resistor | R18, R19 | R_0402_1005Metric |
| 2 | 100R Resistor | R20, R21 | R_0402_1005Metric |
| 4 | 20k Resistor | R24, R25, R26, R27 | R_0402_1005Metric |
| 1 | SW_SPDT | SW1 | SW_Slide_SPDT_Angled |
| 1 | Button_A | SW2 | SW_PUSH_6mm_H5mm |
| 1 | Button_B | SW3 | SW_PUSH_6mm_H5mm |
| 1 | Button_X | SW4 | SW_PUSH_6mm_H5mm |
| 1 | Button_Y | SW5 | SW_PUSH_6mm_H5mm |
| 1 | D-pad UP | SW6 | SW_PUSH_6mm_H5mm |
| 1 | D-pad DOWN | SW7 | SW_PUSH_6mm_H5mm |
| 1 | D-pad LEFT | SW8 | SW_PUSH_6mm_H5mm |
| 1 | D-pad RIGHT | SW9 | SW_PUSH_6mm_H5mm |
| 1 | Start | SW12 | SW_PUSH_6mm_H5mm |
| 1 | Select | SW13 | SW_PUSH_6mm_H5mm |
| 1 | ADS1115IDGS | U3 | TSSOP-10_3x3mm_P0.5mm |
| 1 | MAX98357A | U4 | TQFN-16-1EP_3x3mm_P0.5mm |







# _____________________________________________________________________________________________________________________
- So i plan on using JLCPCB to actually get my boards manufactured and i will be using PCBA for the bottom SMD components
# _____________________________________________________________________________________________________________________

# Here is the other stuff that i need to make the PCB including the components that are not included in the PCBA from JLC along with the links from where i plan on buying the parts - 
# Bill of Materials (BOM) - The Great (DIY) Handheld:
### Parts & Tools List

| Qty | Name | Purpose | Link |
|:---:|:---|:---|:---|
| 1 | TP4056 module | To charge | [Link](https://robu.in/product/tp4056-1a-li-ion-battery-charging-board-micro-usb-with-current-protection-type-c-connector/) |
| 1 | Jumper Wires | To connect daughter boards and the TP4056 module | [Link](https://www.amazon.in/Electronic-Spices-Jumper-Female-Multicolor/dp/B0CPFCRCHB/) |
| 1 | Solder | Soldering material | [Link](https://www.amazon.in/SONEAK-Solder-Rosin-Electrical-Soldering/dp/B084RZWVXY/) |
| 1 | Soldering Flux | Helps prevent cold solder joints | [Link](https://www.amazon.in/UNIVERSAL-HUB-Soldering-Electronics-components/dp/B0FV8HHBTN/) |
| 1 | Soldering Iron | Temperature adjustable iron | [Link](https://www.amazon.in/Temperature-Adjustable-Soldering-Heating-Extra/dp/B0DPVMRTXG/) |
| 1 | Soldering Helping hands | Magnifier and PCB holder | [Link](https://robu.in/product/te-801-multi-function-led-magnifier-pcb-soldering-iron-stand-holder-table-magnifying-glass-35x-12x-w-2-led-light/) |
| 9 | JST SH 2-pin Connector | Battery connection (2mm Pitch) | [Link](https://robu.in/product/jst-sh-2-pin-connector-2mm-pitch/) |
| 1 | Mini HDMI to HDMI Cable | Connect Pi to display | [Link](https://robu.in/product/mini-hdmi-hdmi-cable-1-8-meter-round-high-quality-copper-clad-steel-black/) |
| 1 | 40mm 8Ω Speaker | Audio output | [Link](https://www.amazon.in/Electronic-Spices-Wired-Sound-Speakers/dp/B07MTK843Z) |
| 2 | PS2 joystick module | Left and right analog sticks | [Link](https://www.flyrobo.in/ps2_game_joystick_module_for_arduino) |
| 1 | 4000mAh 3.7V LiPo Battery | Main power source | [Link](https://robu.in/product/nova-955465-4000mah-3-7v-lipo-battery-pack/) |
| 8 | 100 uF 10V Capacitor | Audio/Headphone blocking | [Link](https://robu.in/product/100-uf-10v-through-hole-electrolytic-capacitor-pack-of-20/) |
| 1 | 6mm Tactile Buttons (10pk)| to click click | [Link](https://robu.in/product/6x6x5-tactile-push-button-switch/) |
| 2 | Slide switch SPDT | Power switch | [Link](https://robu.in/product/1-month-warranty-805/) |
| 2 | 1x5 Female Header (RA) | Joystick module connectors | [Link](https://www.sunrom.com/p/1x5-254mm-female-right-angle-single-row-header-strip) |
| 5 | 1x2 Male Pin Header | Power and peripheral connection | [Link](https://robu.in/product/a2541wv-2p-9t-cjt-1x2-pin-2-54mm-180-single-row-pin-header-rohs/) |
| 1 | 2x20 Female Header | Raspberry Pi GPIO connection | [Link](https://robu.in/product/2-54mm-2x20-pin-female-double-row-straight-long-header-strip/) |
| 1 | 5 Inch Touch Screen | Display unit | [Link](https://robu.in/product/5-inch-touch-screen-hdmi-interface-display-module-tft-lcd-800x480-raspberry-pi-2-model-b-touch-pen) |
| 1 | Raspberry Pi Zero 2W | Main processor/Brain | [Link](https://robu.in/product/raspberry-pi-zero-wireless-wh-pre-soldered-header) |
| 2 | PCBA (SMD Assembly) | Pre-assembled SMD components | [Link](https://jlcpcb.com) |
| 5 | Custom PCBs | Motherboard and daughter boards | [Link](https://jlcpcb.com) |



# BTW HERE ARE SOME PICS OF THE PCB THAT I TOOK THROUGHOUT DESIGNING IT(PCB and CAD CASE MODEL)- 
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

