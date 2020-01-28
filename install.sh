#! /bin/sh

#####################################################################
## This script is used for the installation of the pihole-activity ##
## project on your machine                                         ##
#####################################################################

# Set list of packages required
PACKAGES = "wiringPi python3-dev libffi-dev libssl-dev"

# update/grade aptget
apt-get update
apt-get upgrade -y
apt-get $PACKAGES -y

# Set location of profile file and file to launch at boot
PROFILE = "/home/pi/profile"
BOOT1 = "sudo python3 /home/pi/pihole-activity/src/percentCheck.py &"
BOOT2 = "sudo python3 /home/pi/pihole-activity/src/adBlocked.py &"

# Check if percentCheck.py is set at launch
if grep -Fq $BOOT1 $PROFILE
then

# If not, write the command to the profile file
else
    echo $BOOT1 >> $PROFILE
fi

# Check if adBlocked.py is set at launch
if grep -Fq $BOOT2 $PROFILE
then

# If not write the command to the profile file
else
    eco $BOOT2 >> $PROFILE
fi