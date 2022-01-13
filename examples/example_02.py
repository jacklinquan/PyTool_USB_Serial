# Example 2
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
        app.print_text(data_hex)
        # Echo back.
        app.send_data(data_rcv)
