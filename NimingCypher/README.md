<img src="http://i.imgur.com/p26bFim.png" width="150" align="right" alt="IconNiming">

# Niming Cypher

**Encryption module for instant messaging**

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

All the prerequisites are installed with the command below !

### Installing

This is the way to install Niming Cypher

> Code :
```
$ pip install NimingCypher
```
Now you know the way !

## Usage

### Encrypt a string

Only tested with python >= 3.5

For more example see [Wiki](https://github.com/mathix420/NimingCypher/wiki)

> Code :
```python
from NimingCypher import NCrypter
crypter = NCrypter("https://key.com")
encrypted_str = crypter.crypt_text("simple string")
print(encrypted_str)

if crypter.setkey("https://newkey.com") == True:
    print("Successful !")
```
## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Parsing module

## Author

* **Gissinger Arnaud** - *also known as Mathix*

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">NimingCypher</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/mathix420/NimingCypher" property="cc:attributionName" rel="cc:attributionURL">Gissinger Arnaud</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
