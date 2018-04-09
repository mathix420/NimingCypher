
# Niming Cypher

**High security encryption module for instant messaging**

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You should need to install BeautifulSoup

> Code :

		$ pip install beautifulsoup4

### Installing

This is the way to install Niming Cypher

> Code :

		$ pip install NimingCypher

Now you know the way !

## Usage

### Encrypt a string

Only tested with python >= 3.5

> Code :

	import NimingCypher as nc
	crypter = nc.NCrypter("https://key.com")
	encrypted_str = crypter.crypt_text("simple string")
	print(encrypted_str)

## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Parsing module

## Author

* **Gissinger Arnaud** - *also known as Mathix*

## Licence

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
