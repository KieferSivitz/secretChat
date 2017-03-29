# Secret Chat
The goal of this project is to create an open source peer to peer encrypted chat client. The goal of which is to have a simple, reliable chat client that is known to be secure. I'm creating this because I want to be able to talk to people and know that my client is uncompromised, and I want to maintain the integrity of my messages. And I want others to be able to do the same thing.

## Installation Instructions (Linux)
This program uses pyqt5 and python 3, and as such both of these must be installed for it to work.
If one or both of these are already installed on the machine, these steps can be skipped.

To install python3 the command is:

	sudo apt-get install python3

To install pyqt5 the command is:

	sudo apt-get install python3-pyqt5

If git is not already installed on your machine, it can be installed with the following command:

	sudo apt-get install git

Once you have downloaded everything necessary to run the program, clone this repository onto your machine
using the following command:

	git clone https://github.com/KieferSivitz/secretChat.git

Then navigate into the directory containing the files:

	cd secretChat


### Create a Self-Signed SSL Certificate:

Check if you have openssl installed:

	which openssl

If this does not return a path you must install openssl:

	apt-get install openssl

#### Generateing a Private key and signing request

	openssl genrsa -des3 -passout pass:x -out server.pass.key 2048

	openssl rsa -passin pass:x -in server.pass.key -out server.key

	rm server.pass.key

	openssl req -new -key server.key -out server.csr

	openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt

And the following command will start the program:

	python3 secretChat.py


