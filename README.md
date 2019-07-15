# PyTool USB Serial
 Android App for USB serial with Python script capability.

Please try the free version on Google Play: [PyTool USB Serial Free](https://play.google.com/store/apps/details?id=com.quanlin.pytoolusbserialfree).

And here is the paid version on Google Play: [PyTool USB Serial](https://play.google.com/store/apps/details?id=com.quanlin.pytoolusbserial).

PyTool USB Serial is a great tool for USB serial developing, debugging and monitoring.
It features Python script capability that gives you the greatest flexibility.

Why script capability is desirable for USB serial tool?
Electrical engineers find it handy to use a hand held device like Android phone or tablet to debug or monitor serial communication in the field, factory or lab.
But nearly every communication system got its own protocol or data format.
Searching in a sea of hex data like "02a5b4ca....ff000803" and trying to figure out what is happening is not pleasant at all.
That is where PyTool USB Serial comes to help.
With the ability to run custom Python script, PyTool USB Serial can read and parse any received data, display it in the way you want, and even reply when it is needed. 

There are script examples for quick start. Just copy and paste one of them to try them out.

There is also a handy USB serial terminal for general use.

It supports main stream USB serial drivers, including:
* FTDI driver
* CDC ACM driver
* CP210x driver
* CH34x driver
* PL2303 driver

## Script General Guide
* The Python version used in this app is 3.7.

* This app is not designed as script editor although script can be edited in the script field.
The best way is to use your favorite script editor and then copy and paste the script.

* The script field is not in Python global environment.
If custom function is needed, pass all the references as arguments of the function and import packages needed inside the function.

* Always use 4 spaces for indentation to avoid weird errors.

* Most of the packages in standard Python library are available to import.

* If while loop is needed, always use `app.running_script` as condition in order to stop the script properly.

* Use `app.get_output()` to get the script output field as string.

* Use `app.set_output(object)` to display `object` in the script output field as string.

* Use `app.send_data(bytearray)` to send `bytearray` through serial port.

* Use `app.receive_data()` to read the data from the buffer as bytearray.

Here is one script example from this app:
```Python
# Display received data in hex and echo back.

from binascii import hexlify
from codecs import decode

while(app.running_script):
    # Try to fetch any data received in the buffer.
    data_rcv = app.receive_data()
    if data_rcv:
        # Data represented in hex.
        data_hex = decode(hexlify(data_rcv), 'utf_8', 'ignore')
        # Display received data along with old data.
        app.set_output(app.get_output() + data_hex)
        # Echo back.
        app.send_data(data_rcv)
```
