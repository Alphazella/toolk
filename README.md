<img src="github/logo@2x.png" alt="Toolk Logo" width="149" height="93" />

Toolk
============
![Version](https://img.shields.io/badge/Version-0.0.8-green.svg?style=flat)
![license](https://img.shields.io/github/license/mashape/apistatus.svg)

`Toolk` is a toolkit for iOS to automate tedious tasks like generating boilerplate for Swift projects in Xcode.

## Installation
```bash
pip3 install toolk
```

## Usage

### Generating Components

You can use the `toolk generate` (or just `toolk g`) command to generate a Swift/iOS components:

```bash
toolk generate viewcontroller my-new-component
toolk g vc my-new-component # using the alias
```
You can find all possible blueprints in the table below:

Scaffold  | Usage
---       | ---
[ViewController](https://github.com/Alphazella/toolk) | `toolk g vc my-new-component`


## Tests and release
If you've cloned this project, and want to install the library (*and all
development dependencies*), the command you'll want to run is::

    $ pip install -e .[test]

If you'd like to run all tests for this project, you would run the following command::

    $ python setup.py test
