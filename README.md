# Image manipulator
uses Pillow (python image manipulator library) to merge images horizontall and add labels


### Installation

requires [Python](https://www.python.org/downloads/) v3.6+

Setup virtualenv and install dependencies

```sh
git clone https://github.com/mcfa77y/image_manipulator.git
cd image_manipulator
virtualenv -p python3 .
source bin/activate
pip install -r requirements.txt


# need pip?
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py


# need virtualenv?
pip install virtualenv

# need python 3?
brew install python

# need homebrew?
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

```
### Run

```sh
python src/main.py
```

