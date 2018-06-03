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

This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/mathix420/NimingCypher/blob/master/LICENSE) file for details
