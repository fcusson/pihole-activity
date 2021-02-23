# Pihole-Activity

A Python project that manages an LED bar graph and two activity LED on a Raspberry Pi

## Getting Started

This project’s goal is to enclose a pi-hole server in a project box with added activity lights in the front panel. This project requires a raspberry pi with pi-hole already setup on it.

## Preparation

### Cloning the repository to your Pi-Hole

Access your pi-hole terminal via your prefered way. In the case of my setup, I access it through SSH

```
git clone https://github.com/Darkfull-Dante/pihole-activity.git
```

### Installing Dependencies

The following dependencies are required to run the program. Make sure all dependencies are installed with the lines of code bellow before continuing on.

#### Wiring Pi

WiringPi is a utility for Raspberry Pi to control GPIO. This project is built around the use of this utility. For more details on the project see [wiringPi](http://wiringpi.com/).

#### Python 3

Python 3 is the most up to date version of Python (at the time of writing the code) and is the version used for the code. Everything could work with Python 2 but this tutorial will not delve into the change required to make it work.

#### Python 3 RPi.GPIO

Python 3 does not include RPi.GPIO out of the box. It is included in the python3-dev package, but, in order to keep this install lightweight, the dev version was not installed. Required for the correct access of GPIO pins with the python code.

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install wiringpi python3 python3-rpi.gpio
```

## Bill of material

### For the final build

| Description                               | Link                                                                                                                                                                                                                                                                                                                | Quantity |   Price |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------: |
| 10 segments red LED Bar Graph             | [AliExpress](https://www.aliexpress.com/item/32811943871.html?spm=a2g0o.productlist.0.0.385757df1b2Lr8&algo_pvid=81b6ea2e-bbe1-4634-9305-ca7d9543ac35&algo_expid=81b6ea2e-bbe1-4634-9305-ca7d9543ac35-16&btsid=0844ca98-45f0-41d7-bb55-1833f7978391&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55)   | 1        |   $1.96 |
| Red LED                                   | [AliExpress](https://www.aliexpress.com/item/32848810276.html?spm=a2g0o.productlist.0.0.171f3220F091HR&algo_pvid=c14c42e9-d51a-4a9e-89f0-08dd5290a215&algo_expid=c14c42e9-d51a-4a9e-89f0-08dd5290a215-0&btsid=ec5c1224-9eb1-462d-99e7-e5065f9670da&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55)    | 1        |   $2.10 |
| Green LED                                 | See Red LED link                                                                                                                                                                                                                                                                                                    | 1        | ($2.10) |
| 220Ω resistor                             | [AliExpress](https://www.aliexpress.com/item/32847096736.html?spm=a2g0o.productlist.0.0.1e2d77f6E9aCcA&algo_pvid=6403fdcb-0516-4868-bc73-b871abaa2b44&algo_expid=6403fdcb-0516-4868-bc73-b871abaa2b44-0&btsid=119dfe71-7c7d-48ca-b24d-b4240f17a506&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55)    | 12       |   $1.54 |
| Single Row Right Angle Pin Header         | [AliExpress](https://www.aliexpress.com/item/33038720470.html?spm=a2g0o.productlist.0.0.330f7ee9NRZCNC&algo_pvid=20574285-c96f-4147-948a-941f24c17ea7&algo_expid=20574285-c96f-4147-948a-941f24c17ea7-2&btsid=46693f45-04d0-454a-83de-405c4bd38438&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55)    | 11       |   $1.91 |
| Single Row Pin Header                     | [AliExpress](https://www.aliexpress.com/item/32864438850.html?spm=a2g0o.productlist.0.0.681450a7FeeBYB&algo_pvid=4957e0d2-7113-4cf3-a1c0-2b0ad1ee68f7&algo_expid=4957e0d2-7113-4cf3-a1c0-2b0ad1ee68f7-3&btsid=ea84bad1-90d4-40b7-b416-35f83d260430&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55)    | 6        |   $1.15 |
| Female to Female Jumper wires<sup>1</sup> | [AliExpress](https://www.aliexpress.com/item/32970738923.html?spm=a2g0o.productlist.0.0.1a901f77473scE&algo_pvid=e09dda4f-6fd1-449f-b578-b6c221d9ad42&algo_expid=e09dda4f-6fd1-449f-b578-b6c221d9ad42-5&btsid=8983d517-3a9c-4c34-a5d8-cce2eef956f6&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55)    | 15       |   $1.79 |
| PerfBoard                                 | [AliExpress](https://www.aliexpress.com/item/4000070053237.html?spm=a2g0o.productlist.0.0.2eec3d788PBCPE&algo_pvid=cb5d2bc5-7cc8-4db8-90a0-cf39896c2e63&algo_expid=cb5d2bc5-7cc8-4db8-90a0-cf39896c2e63-0&btsid=57cc4798-1fe0-40f7-9108-75111384779f&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55)  | 1        |   $4.34 |
| Nylon 4mm M3 spacer                       | [AliExpress](https://www.aliexpress.com/item/33031794972.html?spm=a2g0o.productlist.0.0.739c41826C2hgY&algo_pvid=4b6e1ee1-2f2c-49f4-9651-4bccf7e3d93d&algo_expid=4b6e1ee1-2f2c-49f4-9651-4bccf7e3d93d-2&btsid=2d11f107-9498-429e-9b07-46bcceeb9a30&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55)    | 6        |   $3.75 |
| 125x80x32 Project Box<sup>2</sup>         | [AliExpress](https://www.aliexpress.com/item/4000370053139.html?spm=a2g0o.productlist.0.0.408e192bQLTqkU&algo_pvid=97080f62-6f11-4e65-81b8-9a35ded55a47&algo_expid=97080f62-6f11-4e65-81b8-9a35ded55a47-11&btsid=e4c17289-1d4c-4c17-89ac-bb3a64ffd2d2&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 1        |   $2.74 |
|                                           |                                                                                                                                                                                                                                                                                                                     | Total    |  $21.28 |

<sup>1</sup>Ideally look for jumper cable in ribbon style so you can keep bundles together for each circuit.
<sup>2</sup>The size provided is based on a Raspberry Pi Zero W with an ethernet to micro USB adapter. I suggest you draw everything to size and make sure everything fits before commiting to a project box size.

All prices include shipping and most of them comes in far greater quantity than needed.

### For prototyping

If it's not your first Raspberry Pi project, you should have most of these item. They will not be permanent to the build and will be reusable afterward.

| Description                                   | Link                                                                                                                                                                                                                                                                                                             | Quantity |   Price |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------: |
| BreadBoard                                    | [AliExpress](https://www.aliexpress.com/item/32785972837.html?spm=a2g0o.productlist.0.0.588066889qfiHt&algo_pvid=35c004a7-f7ef-4c65-97eb-02e0c75670ad&algo_expid=35c004a7-f7ef-4c65-97eb-02e0c75670ad-1&btsid=50ac37d2-b7ec-47da-886d-6547f8840089&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 1        |   $3.17 |
| Male-to-Male Jumper wires                     | See BreadBoard link                                                                                                                                                                                                                                                                                              | 16       | ($3.17) |
| Raspberry Pi GPIO Extender Shield<sup>1</sup> | [AliExpress](https://www.aliexpress.com/item/32848985668.html?spm=a2g0o.productlist.0.0.7e095c217oIqpL&algo_pvid=4b476850-da21-4508-becb-ca6b5207066e&algo_expid=4b476850-da21-4508-becb-ca6b5207066e-0&btsid=bd865da9-0e32-4812-8084-7d21c8173138&ws_ab_test=searchweb0_0,searchweb201602_7,searchweb201603_55) | 1        |   $1.80 |
| BreadBoard power supply<sup>1</sup>           | See BreadBoard link                                                                                                                                                                                                                                                                                              | 1        | ($3.17) |
|                                               |                                                                                                                                                                                                                                                                                                                  | Total    |   $4.97 |

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
- Multimeter

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

![Electric Diagram](assets/img/CircuitBoard/Pi-Hole_LED_System.png)

The circuit is made of two distinct elements. First there is the LED Bar graph and second, the activity light module.
The two modules receive power from the GPIO and connect to ground.

> If you were running V1.0.2 or earlier of the code, the LED Bar Graph was setup for LED on when GPIO was set to LOW. A rewiring of your setup will be required moving foward.

> There are multiple advantages to the change in the setup. Mostly, a simpler way to eventually use PWM in the LED Bar Graph. Also, the new circuit does not use the 3.3V rail which releases the PIN for other use.

### BreadBoard Prototype

#### Testing the prototype

![BreadBoard Diagram](assets/img/CircuitBoard/Pi-Hole_LED_Breadboard.png)

During the prototyping phase, make sure that everything is connected according to the exemple above and then connect to the Raspberry Pi.
Make sure to use an appropriate resistor in the circuit. Make sure that every LED as its own resistor. An LED can draw to much current which could damage the Raspberry Pi GPIO.
LEDs are a kind of diodes, which means that current can only go through a certain direction. For the circuit to work, you must make sure that the positive is connected on the side receiving current to work. The positive side of an LED is always the longer leg. In the case of the LED bar graph, there is no visual way to know the positive side other than testing. If at first the bar graph doesn’t light, simply rotate 180 degree and retest.

> quick tip: mark the positive side of the LED bar graph for future reference.

When everything is connected and the Raspberry Pi is turned on, run the LEDCheck.py python code. This code will cycle through the 12 LED of the modules. The LED should light up in the following order: LED 1 to 10 of the LED bar graph (in order), green LED, red LED.

When everything is connected to your liking, move to the test folder of the repository

```
cd ~/pihole-activity/test
```

then run the python script called LEDCycle

```
python3 LEDCycle.py
```

you should get the following result without errors

```
Bar Graph LED 1 on
Bar Graph LED 2 on
Bar Graph LED 3 on
Bar Graph LED 4 on
Bar Graph LED 5 on
Bar Graph LED 6 on
Bar Graph LED 7 on
Bar Graph LED 8 on
Bar Graph LED 9 on
Bar Graph LED 10 on
Status LED on
ad Blocked LED on
```

While the code run, make sure that all the LED turn on correctly and in the right order. Make the necessary changes if need be.

#### Troubleshooting

- **No lights from the LED bar graph:** The LED bar graph is probably mounted in reverse. Rotate 180 degree and rerun the code.
- **The Green or Red LED do not light up:** make sure that both lights connect to ground. Only one ground is used in the pins, but both lights should join on the negative side to eventually connect to the ground.

#### Running the scripts

##### percentCheck.py

Now it is time to test code in action. The first code we will test is percentCheck.py. That code is responsible for Turning on the LED Bar Graph in accordance to the percentage of ads blocked today and also activating the green LED if the status of the Pi-Hole is "enabled". You can run the test code with the following command.

> Make sure you are still in the test folder of the repo

```
python3 percentCheck.py
```

You should get a similar result as this:

```
enabled
58
pin 1 on, pin no : 11
pin 2 on, pin no : 12
pin 3 on, pin no : 13
pin 4 on, pin no : 15
pin 5 on, pin no : 16
pin 6 on, pin no : 18
pin 8 off, pin no : 3
pin 9 off, pin no : 5
pin 10 off, pin no : 24
Pi-Hole is enabled
enabled
58
enabled
58
...
```

Make sure the result and the LED lights are consistent. Try disabling the Pi-Hole to see if the light goes off. When you are done testing, press `Ctrl+C` to deactivate the code. All LED should go off.

##### adBlocked.py

The second test code is adBlocked.py. This script is responsible for flashin the red LED every (ish) time an ad is blocked. Due t concern for epyleptics, the refresh rate is currently capted at 2 seconds (the script check if new ads have been blocked every 2 seonds). To test the code, run the following command:

```
python3 adBlocked.py
```

Force your pi-hole to block ads. My personnal test is [speedtest.net](https://www.speedtest.net/). You should get result like that:

```
ad Blocked
ad Blocked
ad Blocked
ad Blocked
ad Blocked
...
```

When you are done testing this element, press `Ctrl+C` to stop the script.

### Permanent

The following are the permenant modules that we will install in the build. Be carefull at this point as the module are made to be permanent. Make sure the design fits for your particular case and that the wiring replicate the prototype we made.

> If you know how to use a multimeter, I recommend you test the circuit, making sure there is no unwanted bridge in your module. It simplifies a lot trouble shooting afterward.

#### LED Bar Graph Module

| Front                                                                                                             | Back                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| <img src="assets/img/CircuitBoard/Pi-Hole_LEDBarGraph-Front.png" alt="LED Bar Graph Module - Front" height="350"> | <img src="assets/img/CircuitBoard/Pi-Hole_LEDBarGraph-Back.png" alt="LED Bar Graph Module - Back" height="350"> |

For the LED Bar Graph, make sure that you know which side is the positive. Remember that an LED is a diode and diode will only let current pass from the positive to the negative and not the other way around. I suggest you place all the complonent in the perfBoard without solder first to verify if you are confortable with the design. After you feel ready to start the soldering, go at it one piece at a time. Always start by securing the corners of parts that have more than two pins.

Don't be affraid to bend the metal legs, they will help keep the parts in place when soldering. When your done soldering the parts, cut the excess from the metal legs of the parts.

When you are ready to do the back tracing, make sure to reference where you are soldering as to not make mistake in the soldering lines you'll make. All the resistors should be connected on the same line connecting to one single right angle pin header. That will be were we connect the 3.3v rail.

After that make sure to connect the resistor>LED and then LED>Pin Header in distinct line. Each LED should have its one unique line of solder directing the current to the pins header.

#### Activity LED Module

| Front                                                                                                            | Back                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| <img src="assets/img/CircuitBoard/Pi-Hole_ActivityLED-front.png" alt="Activity LED Module - Front" height="250"> | <img src="assets/img/CircuitBoard/Pi-Hole_ActivityLED-Back.png" alt="Activity LED Module - Back" height="250"> |

For this module, a slight modification is required to the straight pin header. On a flat surface, press the short pin side until it slip right up to the plastic part. This mod will let us mount the pin header under the perfBoard leting us connect fro the back instead of the front of the module.

Making the module is very similar to the LED Bar Graph. Make sure the module makes sense to you and that you are confortable soldering the parts. This one might be more difficult as it is more compact. A helping hand comes in very handy.

#### Ground Converger Module

|                                                         Front                                                          |                                                         Back                                                         |
| :--------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |
| <img src="assets/img/CircuitBoard/Pi-Hole_GroundConverter-Front.png" alt="Ground Converger Module Front" height="150"> | <img src="assets/img/CircuitBoard\Pi-Hole_GroundConverter-Back.png" alt="Ground Converger Module Back" height="150"> |

This is the simplest of the module. This one is completely optionnal and is only to reduce the footprint on the Raspberry Pi. Basically, we want a module that will simply take all our ground connection into one main ground that will connect to one ground GPIO.

> If you do not want that soluttion you can simply use two ground pin on your Raspberry Pi

For this build, the minimum is 3 pins, 2 inputs, 1 output. If you think of any possible expension in the future tu your build, I suggest you already add more ground pins. My build is setup with 5 inputs and 1 output.

## Installation

### Change boot option

Change boot option to make sure that the user "pi" is autologged-in at boot to force scrypt to run:

```
sudo raspi-config
```

From there go in System 1 Options/S2 Boot & Auto Login/B2 Console AutoLogin

### Run script at startup

We will be using the etc/profile to run the 2 scripts at boot. To do so, first open the profile file

```
sudo nano /etc/profile
```

then add the 2 following line of code at the end of the file

```
sudo python /home/pi/pihole-activity/src/percentCheck.py &
sudo python /home/pi/pihole-activity/src/adBlocked.py &
```

When ready, reboot your pi-hole

```
sudo reboot
```

Let the Pi-Hole boot, it can take sometime, but the LED will eventually light up.

### Config.ini

This section will go through the different settings possible in the config.ini file. (I know there is just one right now, I wrote the paragraph for future settings to come)

#### LEDBarGraph

| option             | description                                                                                                                                                                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| reverseLEDBarGraph | Lets you reverse the order of the pins for the LED bar graph. If you were to mount the bar graph in reverse by accident or solder backward the connection to your raspberry pi, this setting lets you reverse the order (pin one becomes 10, 2 becomes 9, etc.). Saves you some resoldering. (I'm obviously not talking by experience) |
| highModeBarGraph   | Lets you change the power mode of the LED bar graph. High Mode means that an input most be high to turn On the LED. Set to true for this behavior. If your circuit expect a low signal to turn on, set to false.                                                                                                                       |

#### StatusLED

| option         | description                                                                                                                                                                                                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| reverseStatus  | Lets you reverse the order of the pins for the status module. If you were to mount the leds in reverse by accident or solder backward the connection to your raspberry pi, this setting lets you reverse the order (pin 37 becomes 35). Saves you some resoldering. (I'm obviously not talking by experience) |
| highModeStatus | Lets you change the power mode of the status module. High Mode means that an input most be high to turn On the LED. Set to true for this behavior. If your circuit expect a low signal to turn on, set to false.                                                                                              |

## Enclosing the project

This part will guide you though the steps of enclosing your project inside a project box. If you are using a different Raspberry Pi thant the Zero W, the placement of the parts, the cable management and holes required may differ.

The parts you have might be different than mine, always measure and carefully cut. You can always cut more in a small hole, it's a lot harder to add material to a bigger hole

### 1. Trace the project on paper

![HandDrawn Tracing](assets/img/Enclosed/HandDrawn.png)

Take time to measure everything as much as you can. A suggestion, make sure you have evrything appart from the project box first so you can have precise measurements. Make sure the design and cable management make sense.

### 2. Place without glueing or screwing

### 3. Mark the places where holes are needed

### 4. Remove the material

### 5. Fix the components

![Inside the case](assets/img/Enclosed/Inside.png)

## Contribution

## Author

- Felix Cusson - [Darkfull-Dante](https://github.com/Darkfull-Dante)
