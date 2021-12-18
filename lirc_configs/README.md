# lirc_configs

Contains LIRC config files that work, sharp.conf works for the Sharp TV we tested with and ur5u-8790l-twc.lircd.conf works with the Vizio TV we tested with. sharp.conf was found in the online database for LIRC found [here](http://lirc.sourceforge.net/remotes), ur5u-8790l-twc.lircd.conf was manually created by Maksym using the irrecord feature of LIRC allowing the recording of IR signals into a config file.

How to use: Instal LIRC, can use apt if on a Debian-type Linux with apt install lirc.

Configure the proper pins in /boot/config.txt if using raspberrian, uncommenting the gpio-tx lines from the default config.txt.

Place these config files in /etc/lircd/lircd.conf.d/

Run command irsend SEND_ONCE \<REMOTENAME\> \<command\> to issue IR signal. 

Primarily adapted from: https://www.hackster.io/austin-stanton/creating-a-raspberry-pi-universal-remote-with-lirc-2fd581
