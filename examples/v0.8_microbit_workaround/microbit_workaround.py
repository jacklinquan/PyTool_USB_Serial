import importlib
import usbserial4a

app.print_text(usbserial4a.__version__ + "\n")
usbserial4a = importlib.reload(usbserial4a)
cdcacmserial4a = importlib.reload(usbserial4a.cdcacmserial4a)
app.print_text(usbserial4a.__version__ + "\n")

_CdcAcmSerial = cdcacmserial4a.CdcAcmSerial
