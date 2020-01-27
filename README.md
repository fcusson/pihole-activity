# Pihole-Activity

A Python project that manages an LED bar graph and two activity LED on a Raspberry Pi

## Getting Started

This project’s goal is to enclose a pi-hole server in a project box with added activity lights in the front panel. This project requires a raspberry pi with pi-hole already setup on it.

## Cloning the repository to your Pi-Hole

## Bill of material

### For the final build

| Description | Link | Quantity | Price |
| ----------- | ---- | -------- | ----- |
| 10 segments red LED Bar Graph | [AliExpress](https://www.aliexpress.com/item/32811943871.html?spm=a2g0o.productlist.0.0.385757df1b2Lr8&algo_pvid=81b6ea2e-bbe1-4634-9305-ca7d9543ac35&algo_expid=81b6ea2e-bbe1-4634-9305-ca7d9543ac35-16&btsid=0844ca98-45f0-41d7-bb55-1833f7978391&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 1 | $1.96 |
| Red LED | [AliExpress](https://www.aliexpress.com/item/32848810276.html?spm=a2g0o.productlist.0.0.171f3220F091HR&algo_pvid=c14c42e9-d51a-4a9e-89f0-08dd5290a215&algo_expid=c14c42e9-d51a-4a9e-89f0-08dd5290a215-0&btsid=ec5c1224-9eb1-462d-99e7-e5065f9670da&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 1 | $2.10 |
| Green LED | See Red LED link | 1 | ($2.10) |
| 220Ω resistor | [AliExpress](https://www.aliexpress.com/item/32847096736.html?spm=a2g0o.productlist.0.0.1e2d77f6E9aCcA&algo_pvid=6403fdcb-0516-4868-bc73-b871abaa2b44&algo_expid=6403fdcb-0516-4868-bc73-b871abaa2b44-0&btsid=119dfe71-7c7d-48ca-b24d-b4240f17a506&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 12 | $1.54 |
| Single Row Right Angle Pin Header | [AliExpress](https://www.aliexpress.com/item/33038720470.html?spm=a2g0o.productlist.0.0.330f7ee9NRZCNC&algo_pvid=20574285-c96f-4147-948a-941f24c17ea7&algo_expid=20574285-c96f-4147-948a-941f24c17ea7-2&btsid=46693f45-04d0-454a-83de-405c4bd38438&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 11 | $1.91 |
| Single Row Pin Header | [AliExpress](https://www.aliexpress.com/item/32864438850.html?spm=a2g0o.productlist.0.0.681450a7FeeBYB&algo_pvid=4957e0d2-7113-4cf3-a1c0-2b0ad1ee68f7&algo_expid=4957e0d2-7113-4cf3-a1c0-2b0ad1ee68f7-3&btsid=ea84bad1-90d4-40b7-b416-35f83d260430&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 3 | $1.15 |
| Female to Female Jumper wires<sup>1</sup> | [AliExpress](https://www.aliexpress.com/item/32970738923.html?spm=a2g0o.productlist.0.0.1a901f77473scE&algo_pvid=e09dda4f-6fd1-449f-b578-b6c221d9ad42&algo_expid=e09dda4f-6fd1-449f-b578-b6c221d9ad42-5&btsid=8983d517-3a9c-4c34-a5d8-cce2eef956f6&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 14 | $1.79 |
| PerfBoard | [AliExpress](https://www.aliexpress.com/item/4000070053237.html?spm=a2g0o.productlist.0.0.2eec3d788PBCPE&algo_pvid=cb5d2bc5-7cc8-4db8-90a0-cf39896c2e63&algo_expid=cb5d2bc5-7cc8-4db8-90a0-cf39896c2e63-0&btsid=57cc4798-1fe0-40f7-9108-75111384779f&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 1 | $4.34 |
| 125x80x32 Project Box<sup>2</sup> | [AliExpress](https://www.aliexpress.com/item/4000370053139.html?spm=a2g0o.productlist.0.0.408e192bQLTqkU&algo_pvid=97080f62-6f11-4e65-81b8-9a35ded55a47&algo_expid=97080f62-6f11-4e65-81b8-9a35ded55a47-11&btsid=e4c17289-1d4c-4c17-89ac-bb3a64ffd2d2&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 1 | $2,74 |
|  |  | Total | $17.53 |

<sup>1</sup>Ideally look for jumper cable in ribbon style so you can keep bundles together for each circuit.
<sup>2</sup>The size provided is based on a Raspberry Pi Zero W with an ethernet to micro USB adapter. I suggest you draw everything to size and make sure everything fits before commiting to a project box size.

All prices include shipping and most of them comes in far greater quantity than needed.

### For prototyping

If it's not your first Raspberry Pi project, you should have most of these item. They will not be permanent to the build and will be reusable afterward.

| Description | Link | Quantity | Price |
| ----------- | ---- | -------- | ----- |
| Male-to-Male Jumper wires |  | 16 |  |
| BreadBoard |  | 1 |  |
| Raspberry Pi GPIO Extender Shield<sup>1</sup> |  | 1 |  |
| BreadBoard power supply<sup>1</sup> |  | 1 |  |

<sup>1</sup>These two elements are optional, but helps a lot in the prototyping phase.

### General 

This list of item are purely equipment that will be need to do the build like I did. You can use any other methods of your likng to get to the same result.

- Soldering Iron
- Solde
- Flux
- Helping hand
- Electric drill
- Exacto
- Hot Glue Gun

### Raspberry Pi equipment

This is the Raspberry Pi that was used for my build. Any other Raspberry Pi could work for the build, but the size and way the wiring was made is based on this form factor.

- Raspberry Pi Zero W
- Ethernet to micro USB adapter
- 5v 2.5a micro USB power supply
- 32 Gb micro SD card
- 20x2 Pin Header (optionnal, but will simplify the connection to the Raspberry Pi Zero)<sup>1</sup>

<sup>1</sup>This part is not required but will make any upgrade or changes to the build much easier down the line, as you will not be soldering the jumper wires directly to the board itself.

## Circuit Board

This section will review the electronic components of the build. It will explain how the system works, how to prototype, test and make the permanent modules for the build.

### Electric Diagram

![Electric Diagram](Images/CircuitBoard/Pi-Hole_LED_System.png)
The circuit is made of two distinct elements. First there is the LED Bar graph and second, the activity light module.
The first module takes the 3.3V rail of the Raspberry Pi and provide power to all 10 LED of the bar graph. Each LED of the bar graph are then connected to a GPIO. In this module, the light of the LED will be powered on when the output of the GPIO pin is set to LOW as the GPIO pin will act as a ground in that case. Inversely, the LED will be off if the GPIO output is set to HIGH.
The second module works in the opposite way. The LED positive is connected to the GPIO. The negative is connected to ground. In this module, the LED is powered on when the output of the GPIO pin is set to HIGH.

### BreadBoard Prototype

#### Testting the prototype

![BreadBoard Diagram](Images/CircuitBoard/Pi-Hole_LED_Breadboard.png)

During the prototyping phase, make sure that everything is connected according to the exemple above and then connect to the Raspberry Pi.
Make sure to use an appropriate resistor in the circuit. Make sure that every LED as its own resistor. An LED can draw to much current which could damage the Raspberry Pi GPIO.
LEDs are a kind of diodes, which means that current can only go through a certain direction. For the circuit to work, you must make sure that the positive is connected on the side receiving current to work. The positive side of an LED is always the longer leg. In the case of the LED bar graph, there is no visual way to know the positive side other than testing. If at first the bar graph doesn’t light, simply rotate 180 degree and retest. (quick tip: mark the positive side of the LED bar graph for future reference).
When everything is connected and the Raspberry Pi is turned on, run the LEDCheck.py python code. This code will cycle through the 12 LED of the modules. The LED should light up in the following order: LED 1 to 10 of the LED bar graph (in order), green LED, red LED.

#### Troubleshooting

- **No lights from the LED bar graph:** First make sure that the 3.3V rail does connect with the resistors. The jumper wire from the 3.3v pin should be on the same line as the resistors. If it still doesn’t work the LED bar graph is probably mounted in reverse. Rotating 180 degree and rerun the code.
- **The Green or Red LED do not light up:** make sure that both lights connect to ground. Only one ground is used in the pins, but both lights should join on the negative side to eventually connect to the ground.

#### Running the scripts

Now it is time to test code in action. 

### Permanent

#### LED Bar Graph Module

| Front | Back |
| --- | --- |
| <img src="Images/CircuitBoard/Pi-Hole_LEDBarGraph-Front.png" alt="LED Bar Graph Module - Front" height="350"> | <img src="Images/CircuitBoard/Pi-Hole_LEDBarGraph-Back.png" alt="LED Bar Graph Module - Back" height="350"> |

#### Activity LED Module

| Front | Back |
| --- | --- |
| <img src="Images/CircuitBoard/Pi-Hole_ActivityLED-front.png" alt="Activity LED Module - Front" height="250"> | <img src="Images/CircuitBoard/Pi-Hole_ActivityLED-Back.png" alt="Activity LED Module - Back" height="250"> |

## Installation

## Author

- Felix Cusson - [Darkfull-Dante](https://github.com/Darkfull-Dante)