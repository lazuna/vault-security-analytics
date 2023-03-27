# Transmitted frames with errors
import random

_frm = "101010101010011"

# Introducing 3 errors at random positions in the frame.
_erp = random.sample(range(len(_frm)), 3)

for _i in _erp:
    _frm = _frm[:_i] + str(int(_frm[_i]) ^ 1) + _frm[_i + 1:]

print("Trabsmitted frame with errors is: ", _frm)
