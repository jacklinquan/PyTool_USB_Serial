# Example 4
# Simple heater control. Try to regulate temperature at 25 degree Celsius.
# Message from heater:
# Byte 1: Preamble, always 0x5a.
# Byte 2~3: Temperature in Celsius degree, 2 bytes signed integer.
# Byte 4: Checksum, a simple sum of the first 3 bytes.
# Message to heater:
# Byte 1: Preamble, always 0xa5.
# Byte 2~3: ON/OFF command, 0x4646 for OFF and 0x4f4e for ON. 
# Byte 4: Checksum, a simple sum of the first 3 bytes.

from struct import unpack
from binascii import hexlify

# Preamble bytes.
preamble_from_heater = 0x5a
preamble_to_heater = 0xa5
# Initial message state.
msg_state = 0
# Target temperature in Celsius degree.
t_target = 25
# Initial temperature.
temperature = t_target
# Initial heater state.
heater_state = 'OFF'
# Heater control commands.
OFF_COMMAND = bytearray([preamble_to_heater, 0x46, 0x46])
OFF_COMMAND.append(sum(OFF_COMMAND) & 0xff)
ON_COMMAND = bytearray([preamble_to_heater, 0x4f, 0x4e])
ON_COMMAND.append(sum(ON_COMMAND) & 0xff)

while(app.running_script):
    # Try to fetch any data received in the buffer.
    data_rcv = app.receive_data()
    if data_rcv:
        # Process every byte of the received data.
        for data_byte in data_rcv:
            # Message states.
            if msg_state == 0:
                # Expecting preamble byte.
                if data_byte == preamble_from_heater:
                    raw_msg_in = bytearray([data_byte])
                    # Enter next state.
                    msg_state = 1
            elif msg_state == 1:
                # Expecting the first byte of the temperature.
                first_byte = data_byte
                raw_msg_in.append(data_byte)
                # Enter next state.
                msg_state = 2
            elif msg_state == 2:
                # Expecting the second byte of the temperature.
                second_byte = data_byte
                raw_msg_in.append(data_byte)
                # Enter next state.
                msg_state = 3
            elif msg_state == 3:
                # Expecting the checksum.
                checksum = data_byte
                if checksum == ((preamble_from_heater + first_byte + second_byte) & 0xff):
                    # This message is valid.
                    raw_msg_in.append(data_byte)
                    temperature = unpack('>h', bytes(bytearray([first_byte, second_byte])))[0]
                    if temperature < -273:
                        # Impossible temperature.
                        text_t = 'Temperature sensor error!'
                        # Turn off the heater.
                        heater_state = 'OFF'
                        raw_msg_out = OFF_COMMAND
                    else:
                        # Display temperature and send control command.
                        text_t = 'Temperature: {} degree Celsius'.format(temperature)
                        if temperature > t_target:
                            # Too hot, turn off the heater.
                            heater_state = 'OFF'
                            raw_msg_out = OFF_COMMAND
                        elif temperature < t_target:
                            # Too cold, turn on the heater.
                            heater_state = 'ON'
                            raw_msg_out = ON_COMMAND
                        else:
                            # Do not change heater state when temperature == t_target to prevent from cycling too fast.
                            raw_msg_out = ON_COMMAND if heater_state == 'ON' else OFF_COMMAND
                    app.send_data(raw_msg_out)
                    text_output = 'Received message: {}'.format(hexlify(raw_msg_in))
                    text_output += '\nSent message:     {}'.format(hexlify(raw_msg_out))
                    text_output += '\n\n{}'.format(text_t)
                    text_output += '\nHeater state: {}'.format(heater_state)    
                    app.set_output(text_output)
                # Reset message state.
                msg_state = 0
            else:
                # Wrong message state, reset it.
                msg_state = 0
                