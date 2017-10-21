# BiCrypt

Encrypt files with two differents AES Keys.

## Getting Started

These instructions will get you a copy of the project up and running on your local machne for development and testing purposes. This program actually **CAN NOT** be used on general purposes.

### Prerequisites

```
Python 3.x
Pyaes>=1.6.1
```

### Installing

* Clone the repository `git clone https://github.com/moige/BiCrypt.git`
* Install dependences running `pip install -r requirements.txt`

## Instructions

For encrypt you file you will need to provied **two** passprhase and a file. Is recommend to use strongs passprhases using a combination of symbols, numbers and upper-lower case letters.

The syntax in command line is:

```
python BiCrypt.py FileName FirstPassphrase SecondPassprhase
```

When you do that, the program generate a new file called 
`YOU_FILE_NAME.crypt` which is no more that you encrypted file.

For decrypt the file would be:

```
python BiCrypt.py FileName.crypt FirstPassphrase SecondPassphrase
```

**Note** that you need to put yours passprhrases in order, that is, just in the order as you put them when you encrypted the file, to can decrypt the file with sucess.

Also yo can append `#!/usr/bin/env python` to the header on `BiCrypt.py` 
file, delete the file type (BiCrypt ~~.py~~), and then put that file in 
you `/usr/bin` folder for avoid use the whole `python` command.

## Contributing

You are free to contribute to this project if you want. You can send suggest or changes via pull requests.

## Versioning

I use [SemVer](http://semver.org) for versioning.

## Authors

* **Moisés González**

See also the lisft of [contributors](https://github.com/moige/BiDecrypt/contributors) who participated in this project.

## License

This project is licensed under the Apache 2.0 License - See the [LICENSE](LICENSE) file for details.
