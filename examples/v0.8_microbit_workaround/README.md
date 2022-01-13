# Version 0.8 BBC micro:bit workaround

`PyTool USB Serial v0.8` is built with `usbserial4a v0.3.0`.
But `usbserial4a v0.3.0` does not support BBC micro:bit.

In `usbserial4a v0.4.0`, the CDC ACM driver is updated and now it supports BBC micro:bit.
And `usbserial4a v0.4.0` is tested with BBC micro:bit V1(nRF51).

To make `PyTool USB Serial v0.8` work with BBC micro:bit, there is a workaround.

## Instructions
* Copy `microbit_workaround.py` to a folder in the storage of the Android device.
  In my case, the folder name is `PyToolUSBSerial`

* Download [`usbserial4a` package](https://github.com/jacklinquan/usbserial4a) and copy it to the same folder.
  In my case, now both `microbit_workaround.py` and `usbserial4a` package are in `PyToolUSBSerial` folder.

* Connect BBC micro:bit with the Android device through USB On-The-Go cable.

* Open `PyTool USB Serial v0.8` and press `Script` tab.
  Do NOT connect BBC micro:bit now.

* Press `Load` button and load `microbit_workaround.py` from the storage.
  In my case, the path is `sdcard/PyToolUSBSerial/microbit_workaround.py`.

* Run this script and in the output it should show the version strings of both old and new versions:
  ```
  0.3.0
  0.4.0
  ```

* Clear both script field and output field.
  This is import because every time after the app start/restart, you need to load the script from the storage.
  The load process will add the path into Python system path.
  Otherwise it would not find the new version of `usbserial4a`.

* Press the `Scan` tab and scan USB devices. And then select the device to enter `Connection` page.

* In `Device Driver` select `CDC ACM` and set `Baud Rate` to 115200.

* Press `Connect` and now it should be ready to communicate with BBC micro:bit.
