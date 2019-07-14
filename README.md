# tpNameIt

Python module that manages the nomenclature of your DCC scenes:

* Nomenclature are based in the concept of rules and tokens. Those rules and tokens can be setup in a per-project basis.
* DCC agnostic way, the library works in any DCC supported by tpDccLib

## Dependencies
* **tpPyUtils**: https://github.com/tpoveda/tpPyUtils
* **tpDccLib**: https://github.com/tpoveda/tpDccLib
* **tpQtLib**: https://github.com/tpoveda/tpQtLib

Depending on the DCC you are going to use you will need to download and install one of the following repositories:
* **3ds Max**: https://github.com/tpoveda/tpMaxLib
* **Maya**: https://github.com/tpoveda/tpMayaLib
* **Houdini**: *Work in Progress*
* **Nuke**: *Work in Progress*
* **Blender**: *Work in Progress*

## Installation
### Manual
1. Clone/Download tpNameIt dependencies Python packages and follow instructions to install them.
2. Clone/Download tpNameIt anywhere in your PC (If you download the repo, you will need to extract
the contents of the .zip file).
3. Copy **tpNameIt** folder located inside **source** folder in a path added to **sys.path**

### Automatic
Automatic installation for tpNameIt is not finished yet.

## Usage

### Initialization Code

1. If you only want to use tpNameIt libraries functionality
```python
import tpDccLib
tpDccLib.init()

import tpQtLib
tpQtLib.init()

import tpNameIt
tpNameIt.init()
```

2. If you want to launch tpNameIt UI
```python
import tpDccLib
tpDccLib.init()

import tpQtLib
tpQtLib.init()

import tpNameIt
tpNameIt.run()
```