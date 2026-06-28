<img width="1983" height="793" alt="image" src="https://github.com/user-attachments/assets/2fd84730-6a83-4686-bd75-53d2d06e5003" />



# TGH - THE GREAT (DIY) HANDHELD
So yeah this is me trying to make my own custom retro handheld gaming device with a custom pcb powered by a pi zero 2w.


**BTW NOTE:** the case shall be printed by someone who was willing to print it from the slack channel - #printing-legion.


***very VERY IMPORTANT NOTE TO STASIS REVIWER ---> SO IN THE BOM U MIGHT SEE THAT THE QTY OF SOME OF THE COMPONENTS FROM ROBU.IN IS MORE THAN REQUIRED THIS IS BECAUSE ROBU.IN HAS A MINIMUM ORDER QTY OF 10 INDIAN RUPEES PER COMPONENT SO HENCE I HAD TO LIKE INCREASE THE QTY OF SOME OF THE PASIVE COMPOENNTS TO LIKE FOLLOW THIS. BTW ITS STILL LIKE WAY WAY CHEAPER THAN JLCPCB'S PCBA THAT WOULD HAVE BROUGHT THE TOTAL COST TO 199.56 USD EXCLUDING TAX (I CHECKED)***

***SO PLEASE PLEASE DONT REJECT THE PROJECT DUE TO THIS since if it is rejected again i dont think i will be able to make the changes and ship it again as its probably gonna get reviewed like after 30th anyways.***

## project layout
```
.
├── Assembly Layered.step
├── Assembly.step
├── Custom Firmware!!!!!!!!!!/
│   ├── Launcher.py
│   ├── roms/
│   │   ├── GB/
│   │   ├── GBA/
│   │   ├── GBC/
│   │   ├── GEN/
│   │   ├── NES/
│   │   ├── SMS/
│   │   └── SNES/
│   ├── saves/
│   └── states/
├── production files/
│   ├── CAD/
│   │   ├── Bottom Case.step
│   │   └── Top Case.step
│   └── PCB/
│       ├── MAIN PANELISED PCB (TO BE MANUFACTURED)/
│       │   └── CPL.csv
│       ├── Mother board (not to be manufactured)/
│       │   └── CPL Motherboard.csv
│       ├── left daughter board (not to be manufactured)/
│       │   └── CPL LEFT BOARD.csv
│       └── right daughter board (not to be manufactured)/
│           └── CPL RIGHT BOARD.csv
└── src/
		├── FreeCAD/
		│   ├── Assembly Layered.FCStd
		│   ├── Assembly.FCStd
		│   ├── Bottom case.FCStd
		│   ├── Top Case.FCStd
		│   └── dual-axis-xy-joystick-module-with-push-button-1.snapshot.1/
		└── PCB/
				├── Non Panelised PCB/
				│   ├── Handheld Gaming device PCB.kicad_pcb
				│   ├── Handheld Gaming device PCB.kicad_pro
				│   ├── Handheld Gaming device PCB.kicad_sch
				│   ├── Left_Daughter_Board.kicad_sch
				│   └── Right_Daughter_Board.kicad_sch
				└── Panelised PCB/
						├── Handheld_Panel.kicad_pcb
						├── Handheld_Panel.kicad_pro
						└── Handheld_Panel.kicad_sch
```

## quick specs
- Panelised PCB Dimensions - 339.82 mm x 102.32 mm
- the only KiCAD plugin i used was KiKit to panelise the board, everything else was designed by me (this is my first major PCB project)

## BOM/BILL OF MATERIALS (PARTS I NEED FUNDING FOR)

| Name | Purpose | Quantity | Total Cost (USD) | Link | Distributor |
|---|---|---|---|---|---|
| PCB from JLCPCB  | it is the main PCB and will connect all components to each other. (btw JLCPCB has min order qty for PCB as 5 so yeah) | 5 | 18.4 | https://cart.jlcpcb.com/ | JLCPCB |
| Raspberry Pi Zero | its basically the core of the whole project it shall basically run everything. | 1 | 19.08 | https://robu.in/product/raspberry-pi-zero-wireless-wh-pre-soldered-header/ | robu.in |
| 5 Inch Touch Screen HDMI Interface TFT LCD | to display. | 1 | 26.18 | https://robu.in/product/5-inch-touch-screen-hdmi-interface-display-module-tft-lcd-800x480-raspberry-pi-2-model-b-touch-pen/ | robu.in |
| Mini HDMI To HDMI Cable | to connect pi to display | 1 | 1.08 | https://robu.in/product/mini-hdmi-hdmi-cable-1-8-meter-round-high-quality-copper-clad-steel-black/ | robu.in |
| 10 uF capacitor | to decouple more  | 15 | 0.14 | https://robu.in/product/cs2012x7r106m100nre-samwha-10v-10uf-x7r-%c2%b120-0805-multilayer-ceramic-capacitors-mlcc-smd-smt-rohs/ | robu.in |
| 100nF capacitor | to decouple | 20 | 0.14 | https://robu.in/product/tcc0805x7r104k500dt-cctc-smt-ceramic-capacitors-0805-x7r-104k100nf%c2%b110-rated-voltage50v-thickness0-85mmtape/ | robu.in |
| 6x6x5mm tactile switches | to well be used as switches and for the buttons controlling everything. | 10 | 0.14 | https://robu.in/product/6x6x5mm-tactile-push-button-switch-pack-of-20/ | robu.in |
| MAX98358ETE | audio amplifier | 1 | 2.62 | https://robu.in/product/1-month-warranty-560/ | robu.in |
| MT3608  IC | to take a lower DC voltage and steps it up to a higher, adjustable DC voltage | 2 | 0.28 | https://robu.in/product/mt3608-xian-aerosemi-tech-boost-type-adjustable-2a-2v24v-sot-23-6-dc-dc-converters-rohs/ | robu.in |
| 33 µH BOURNS-SRR1260-330M-Power Inductor (SMD) | to stores energy in a magnetic field and resists changes in electrical current. | 1 | 0.67 | https://robu.in/product/srr1260-330m-bourns-srr1260-330m-power-inductor-smd-33-%c2%b5h-3-a-shielded-2-8-a-srr1260-series/ | robu.in |
| SOD-123 Schottky Diodes ROHS | used to allow current to flow in one direction. | 2 | 0.12 | https://robu.in/product/1n5819w-kexin-40v-600mv1a-1a-sod-123-schottky-diodes-rohs/ | robu.in |
| 100 ohm resistor | to resist current | 25 | 0.12 | https://robu.in/product/rc0805jr-07100rl-yageo-res-thick-film-0805-100-ohm-5-0-125w1-8w-%c2%b1100ppm-c-pad-smd-t-r/ | robu.in |
| 4.7k ohm resistor | to resist  | 29 | 0.12 | https://robu.in/product/yageo-4-7k-ohm-1-4w-0805-surface-mount-resistor-pack-of-50/ | robu.in |
| 10k ohm resistor | im legit tired of writing the same thing again for all the resistor but anyways ---> IT resists the flow of current. | 20 | 0.12 | https://robu.in/product/rc0805fr-0710kl-yageo-res-thick-film-0805-10k-ohm-1-0-125w1-8w-%c2%b1100ppm-c-pad-smd-t-r/ | robu.in |
| 20k ohm resistor | u are not gonna belive what this does ---> IT resists the flow of current.... | 29 | 0.12 | https://robu.in/product/rc0805fr-0720kl-yageo-res-thick-film-0805-20k-ohm-1-0-125w1-8w-%c2%b1100ppm-c-pad-smd-t-r/ | robu.in |
| 33k ohm resistor | to resist!!!!! | 20 | 0.12 | https://robu.in/product/rc0805fr-0733kl-yageo-res-thick-film-0805-33k-ohm-1-0-125w1-8w-%c2%b1100ppm-c-pad-smd-t-r/ | robu.in |
| 100k ohm 0805 resistor | to resist flow of current? | 23 | 0.12 | https://robu.in/product/yageo-100k-ohm-1-2w-0805-surface-mount-resistor-pack-of-50/ | robu.in |
| D6.3xL11mm Aluminum Electrolytic Capacitors | its a capacitor dude like it provides capacitance (idk what do i write under Purpose) | 4 | 0.18 | https://robu.in/product/16yxf100mefct16-3x11-rubycon-100uf-16v-%c2%b120-plugind6-3xl11mm-aluminum-electrolytic-capacitors-leaded-rohs/ | robu.in |
| 22µF SMT 0805 capacitor | To provide capacitance | 10 | 0.18 | https://robu.in/product/tcc0805x5r226k100ft-cctc-smt-ceramic-capacitors-0805-x5r-226k22%c2%b5f%c2%b110-rated-voltage10v-thickness1-25mmtape/ | robu.in |
| TP4056 1A Li-Ion Battery Charging Board | To charge the battery  | 1 | 0.17 | https://robu.in/product/tp4056-1a-li-ion-battery-charging-board-micro-usb-with-current-protection-type-c-connector/ | Robu.in |
| 1mm Pitch Pin headers | These are seperate as the previous headers are not 1mm pitch pin headers. | 1 | 0.21 | https://robu.in/product/1-month-warranty-884/ | Robu.in |
| 3.5mm Female Audio Jack Connector  | to attach headphones | 1 | 0.47 | https://evelta.com/3-5mm-female-audio-jack-connector-6pin-1/ | Evelta.com |
| ADS1115IDGSR - 16-Bit ADC 2, 4 Input 1 Sigma-Delta IC VSSOP-10 | to convert analog voltage signals into digital data  | 1 | 1.94 | https://evelta.com/ads1115idgsr-16-bit-adc-2-4-input-1-sigma-delta-ic-vssop-10/ | Evelta.com |
| PS2 Game Joystick Module | For the Joysticks | 2 | 0.82 | https://www.flyrobo.in/ps2_game_joystick_module_for_arduino | FlyRobo |
| Male and Female Header Connector Strip, Pack of 10, Breakable Strip | For the pin Headers (btw this was a cheap pack of 10 and is actually cheaper than buying each header individually) | 1 | 1.27 | https://www.amazon.in/gp/product/B0FQP3SN7H/ref=ox_sc_act_image_8?smid=ATNZHHWX66S9H&psc=1 | Amazon |
| SPDT Slide Switch Right Angle | TO turn on and off | 1 | 1.0 | https://www.amazon.in/gp/product/B0B434R6QF/ref=ox_sc_act_image_7?smid=A2JDRZEGU1IDE2&psc=1 | Amazon |
| 0.5Watt Power Audio Speaker | For sound | 1 | 1.21 | https://www.amazon.in/gp/product/B07MTK843Z/ref=ox_sc_act_image_6?smid=AJ6SIZC8YQDZX&psc=1 | Amazon |
| Isopropyl Alcohol | For cleaning Board after soldering. | 1 | 2.95 | https://www.amazon.in/gp/product/B0DXLCF467/ref=ox_sc_act_image_5?smid=A66YHFPLB5NLO&th=1 | Amazon |
| Tactile Push Button Switch Caps | To button | 1 | 2.34 | https://www.amazon.in/gp/product/B0DCP7J7R7/ref=ox_sc_act_image_4?smid=AOG7U64E0DVL2&psc=1 | Amazon |
| Jumper Wires | For fine adjustment if required | 1 | 1.66 | https://www.amazon.in/gp/product/B0CPFCRCHB/ref=ox_sc_act_image_3?smid=AJ6SIZC8YQDZX&th=1 | Amazon |
| Solder  | to solder | 1 | 8.37 | https://www.amazon.in/gp/product/B084RZWVXY/ref=ox_sc_act_image_2?smid=AVIYBMAJK8N56&th=1 | Amazon |
| Soldering Flux | Helping to solder. | 1 | 0.84 | https://www.amazon.in/gp/product/B0FV8HHBTN/ref=ox_sc_act_image_1?smid=A366YFPXO3CTI5&psc=1 | Amazon |




## fab note
- so i plan on using JLCPCB to actually get my boards manufactured but will be ASSEMBLING THE COMPONENTS BY HAND!!!!

## pics from while i was designing it
<img width="533" height="220" alt="Screenshot 2026-05-10 230008" src="https://github.com/user-attachments/assets/07351982-c047-4389-aff6-f1acf80b013c" />
<img width="795" height="300" alt="Screenshot 2026-05-09 170451" src="https://github.com/user-attachments/assets/d3c5e589-1971-4ace-8ef0-f19d54ade833" />
<img width="722" height="238" alt="Screenshot 2026-05-09 164731" src="https://github.com/user-attachments/assets/7919f3ed-ffe4-4e6f-bf32-dd36c344b107" />
<img width="354" height="302" alt="Screenshot 2026-05-09 163952" src="https://github.com/user-attachments/assets/7560b851-7067-440e-bd96-9815e528fb82" />
<img width="591" height="307" alt="Screenshot 2026-05-09 162141" src="https://github.com/user-attachments/assets/caa44fb4-8e67-4365-84b5-602e523d2dbf" />
<img width="797" height="406" alt="Screenshot 2026-05-09 135802" src="https://github.com/user-attachments/assets/7b6ab872-daa7-4a54-b1f2-7dee7b510b91" />
<img width="800" height="440" alt="Screenshot 2026-05-08 181919" src="https://github.com/user-attachments/assets/3f739e95-050e-4902-926e-c2a0a8b94d33" />
<img width="689" height="340" alt="Screenshot 2026-05-08 181737" src="https://github.com/user-attachments/assets/db1eb948-331f-4e75-b27f-56d3c52fbf0e" />
<img width="476" height="242" alt="Screenshot 2026-05-08 181207" src="https://github.com/user-attachments/assets/e4d4ba49-dd32-4d69-93c2-a37ed84d5858" />
<img width="770" height="297" alt="Screenshot 2026-05-11 143934" src="https://github.com/user-attachments/assets/455fa56f-c145-4298-a841-3849336d20df" />
<img width="959" height="539" alt="Screenshot 2026-05-12 155912" src="https://github.com/user-attachments/assets/a4b4cce1-aa40-4764-9c79-e5f9145d9b48" />
<img width="959" height="539" alt="Screenshot 2026-05-12 155945" src="https://github.com/user-attachments/assets/7b81df71-cd8d-4bd0-ac16-8754970a15b1" />
<img width="748" height="476" alt="image" src="https://github.com/user-attachments/assets/cf7e77a1-3f0b-48f9-a412-a73bc8be4371" />
<img width="331" height="233" alt="image" src="https://github.com/user-attachments/assets/0330da81-b8cb-4026-9ec7-34858598c57d" />
<img width="303" height="341" alt="image" src="https://github.com/user-attachments/assets/4c7e0e76-06d4-4b56-8a6b-0bebd8b183ed" />
