# Project-CTR Windows Builds

ctrtool - updated version of neimod's ctrtool

makerom - creates CTR cxi/cfa/cci/cia files


## Download

The executables can be downloaded from the [Release Page](https://github.com/Ich73/Project-CTR-WindowsBuilds/releases).

## Build

To build the tools for windows 32-bit and 64-bit using [Cygwin](https://www.cygwin.com/) you need to download the following packages:
  * `mingw64-i686-gcc-core`
  * `mingw64-i686-win-iconv`
  * `mingw64-x86_64-gcc-core`
  * `mingw64-x86_64-win-iconv`

Additionally if you want to use the [`build-all.py`](/build-all.py) script you need [Python 3.8.3](https://www.python.org/downloads/release/python-383/).

Then you simply need to run the `build-all.py` script and the four zip files with the executables will be in the `build` folder.
