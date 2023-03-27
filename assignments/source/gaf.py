# Generate a frame
#   Params:
#       _dbd - data block d
#       _div - divisor

def gaf(dbd, div):
    _dbd = dbd
    _div = div
    _ndd = len(_dbd) + len(_div) - 1 # obtain value of n from data block and divisor
    _frm = _dbd + "0" * (_ndd - len(_dbd)) # frame

    _rmd = pdv(_frm, _div)[1]
    _crc = bin(int(_rmd, 2))[2:].zfill(len(_div) - 1)
    _frm = _frm[:len(_frm) - len(_crc)] + _crc
    return _frm

def pdv(dvd, div):
    # To process polynomial division on two binary polynomials
    _div = div
    _dvd = dvd

    _dvd = _dvd.lstrip("0")
    _div = _div.lstrip("0")

    _div = _div + "0" * (len(_dvd) - len(_div))

    # Process polynomial division
    _rmd = ""
    for _i in range(len(_dvd)):
        if _rmd and _rmd[0] == "1":
            _rmd = _rmd[1:]
        else:
            _rmd += _dvd[_i]

        if len(_rmd) == len(_div):
            _rmd = bin(int(_rmd, 2) ^ int(_div, 2))[:]

    return (_dvd + _rmd, _rmd)

print("------------------------------")

# Sample test inputs
print("Sample test inputs")
_dbd = "1110001111"
_div = "1011"
_frm = gaf(_dbd, _div)
print(f"The data block is: {_dbd}")
print(f"Divisor is: {_div}")
print(f"Frame is {_frm}")

print("------------------------------")

# Sample test inputs
print("Sample test inputs")
_dbd = "1011010010"
_div = "110101"
_frm = gaf(_dbd, _div)
print(f"The data block is: {_dbd}")
print(f"Divisor is: {_div}")
print(f"Frame is {_frm}")

print("------------------------------")
