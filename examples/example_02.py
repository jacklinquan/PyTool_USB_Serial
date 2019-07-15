# Example 2
# Custom function.

# The script field is not in python global environment.
# Pass all the references as arguments of the function.
def func(app=app):
    # Import packages needed inside the function.
    from codecs import decode
    from binascii import unhexlify
    data_txt = decode(unhexlify('48656c6c6f210a'), 'utf_8', 'ignore')
    app.set_output(app.get_output() + data_txt)

func()
