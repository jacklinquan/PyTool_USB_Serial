# Example 5
# Log text in storage.

# The log file is located here [Storage Directory]/PyToolUSBSerial/log_[UTC Timestamp].txt.
full_file_path = app.log_file(
    'Data1, 100\\n' + 
    'Data2, 200\\n' + 
    'Data3, 300\\n' + 
    'Data4, 400\\n' + 
    'Data5, 500\\n'
)

app.set_output('Log file is saved: {}'.format(full_file_path))
