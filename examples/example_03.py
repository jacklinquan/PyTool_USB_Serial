# Example 3
# Display received data in both hex and text, and send some data periodically.

from time import sleep
from codecs import encode, decode
from binascii import hexlify, unhexlify

timer_100ms = 0
while(app.running_script):
    # Sleep for 0.1s, so the code inside the loop runs every 0.1s.
    sleep(0.1)
    
    timer_100ms += 1
    if timer_100ms >= 10:
        timer_100ms = 0
        # Send the data every second.
        app.send_data(unhexlify('48656c6c6F'))
        app.send_data(encode(', world!', 'utf_8', 'ignore'))
        
    # Try to fetch any data received in the buffer.
    data_rcv = app.receive_data()
    if data_rcv:
        # If any data is received, display it in the output field.
        # Data represented in hex.
        data_hex = decode(hexlify(data_rcv), 'utf_8', 'ignore')
        # Data represented in text.
        data_txt = decode(data_rcv, 'utf_8', 'ignore')
        # Display received data along with old data.
        app.print_text(data_hex + '\n' + data_txt + '\n\n')
